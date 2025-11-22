# Image Print Integration Plan

## Goal

Enable a standard (non-root) user to print images to the MC582H thermal printer using a Python script without requiring `sudo`.

## Current State

- ✅ USB printer detected at `0x4b43:0x3538`
- ✅ Working script (`print_image.py`) that prints images
- ❌ Requires `sudo` to access USB device
- ✅ Python dependencies in virtual environment

## Required Changes

### 1. USB Device Permissions (udev Rules)

**Problem:** Linux restricts direct USB device access to root by default.

**Solution:** Create a udev rule to grant access to the specific printer for users in the `lp` group.

#### Step-by-Step Implementation

**Create udev rule file:**
```bash
sudo nano /etc/udev/rules.d/99-thermal-printer.rules
```

**Add this rule:**
```
# MC582H Thermal Printer (Caysn)
SUBSYSTEM=="usb", ATTR{idVendor}=="4b43", ATTR{idProduct}=="3538", MODE="0666", GROUP="lp"
```

**Explanation:**
- `SUBSYSTEM=="usb"`: Apply to USB devices
- `ATTR{idVendor}=="4b43"`: Match our printer's vendor ID
- `ATTR{idProduct}=="3538"`: Match our printer's product ID
- `MODE="0666"`: Grant read/write permissions to all users
- `GROUP="lp"`: Assign device to `lp` (line printer) group

**Alternative (more restrictive):**
```
# MC582H Thermal Printer - lp group only
SUBSYSTEM=="usb", ATTR{idVendor}=="4b43", ATTR{idProduct}=="3538", MODE="0660", GROUP="lp"
```
This restricts access to only users in the `lp` group (`MODE="0660"`).

**Reload udev rules:**
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

**Verify user is in lp group:**
```bash
groups $USER
```

If `lp` is not listed:
```bash
sudo usermod -a -G lp $USER
# Log out and log back in
```

**Test without sudo:**
```bash
# Unplug and replug the printer, then:
ls -l /dev/bus/usb/001/002  # Replace with actual bus/device numbers from lsusb
# Should show group 'lp' and permissions allowing group write
```

### 2. Python Environment Setup

Once USB permissions are solved, the script needs access to the virtual environment's packages.

#### Option A: Use Virtual Environment Directly

**Activate venv before running:**
```bash
source venv/bin/activate
python3 print_image.py image.png
```

**Or specify full path without activation:**
```bash
./venv/bin/python3 print_image.py image.png
```

#### Option B: System-Wide Installation

**Install packages system-wide** (not recommended for development):
```bash
pip3 install python-escpos pyusb
python3 print_image.py image.png
```

#### Option C: Wrapper Script

Create a wrapper that activates the venv automatically:

**File:** `print_thermal.sh`
```bash
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$SCRIPT_DIR/venv/bin/python3" "$SCRIPT_DIR/project_planning_documents/print_image.py" "$@"
```

**Make executable:**
```bash
chmod +x print_thermal.sh
```

**Usage:**
```bash
./print_thermal.sh image.png
```

### 3. Updated Print Script (Non-sudo Version)

The existing `print_image.py` will work without modification once permissions are fixed. However, here's an improved version with better error handling:

**File:** `print_image_user.py`
```python
import sys
import os
from escpos.printer import Usb
from escpos.exceptions import DeviceNotFoundError, USBNotFoundError

def print_image(image_path):
    # Vendor: 0x4b43, Product: 0x3538
    # Out Endpoint: 0x03
    # In Endpoint: 0x81
    try:
        # Initialize printer with the specific endpoints found earlier
        p = Usb(0x4b43, 0x3538, in_ep=0x81, out_ep=0x03)
        
        # Fix for "media.width.pixel field not set" warning
        # The MC582H is a 58mm printer with 384 dots of resolution (203 DPI)
        p.profile.profile_data['media'] = {
            'width': {'pixels': 384},
            'dpi': 203
        }
        
        print(f"Printing image: {image_path}")
        
        # Print the image
        p.image(image_path)
        
        # Feed paper to ensure the image clears the cutter
        p.text("\n" * 5)
        
        p.cut()
        print("Success")
        
    except (DeviceNotFoundError, USBNotFoundError) as e:
        print(f"Printer not found: {e}")
        print("\nTroubleshooting:")
        print("1. Check if printer is powered on and connected via USB")
        print("2. Run 'lsusb' to verify device is detected")
        print("3. Check if udev rules are configured (see documentation)")
        print("4. Verify you are in the 'lp' group: groups $USER")
        sys.exit(1)
    except PermissionError as e:
        print(f"Permission denied: {e}")
        print("\nYou need permission to access the USB device.")
        print("Either:")
        print("1. Run with sudo (not recommended for regular use)")
        print("2. Set up udev rules (see documentation)")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 print_image_user.py <path_to_image.png>")
        print("       ./venv/bin/python3 print_image_user.py <path_to_image.png>")
        sys.exit(1)
    
    img_path = sys.argv[1]
    if not os.path.exists(img_path):
        print(f"Error: File not found: {img_path}")
        sys.exit(1)
        
    print_image(img_path)
```

## Implementation Checklist

- [ ] Create udev rules file in `/etc/udev/rules.d/99-thermal-printer.rules`
- [ ] Reload udev rules
- [ ] Add user to `lp` group (if not already)
- [ ] Log out and log back in (for group membership to take effect)
- [ ] Unplug and replug printer (to apply new udev rules)
- [ ] Verify device permissions: `ls -l /dev/bus/usb/...`
- [ ] Test script without sudo: `./venv/bin/python3 print_image.py test.png`

## Verification

**Check if setup is correct:**

1. **User in correct group:**
   ```bash
   groups | grep lp
   ```

2. **USB device has correct permissions:**
   ```bash
   lsusb  # Note bus and device numbers
   ls -l /dev/bus/usb/001/002  # Replace with your bus/device
   # Should show: crw-rw-rw- 1 root lp ...
   #              or: crw-rw---- 1 root lp ... (if MODE="0660")
   ```

3. **Python can access without sudo:**
   ```bash
   ./venv/bin/python3 -c "import usb.core; print(usb.core.find(idVendor=0x4b43, idProduct=0x3538))"
   # Should print device info, not "None" or permission error
   ```

## Summary

**Yes, after fixing permissions, it's just a question of venv dependencies.**

The two requirements are:

1. **USB Permissions:** udev rules + user in `lp` group
2. **Python Dependencies:** Use virtual environment or install system-wide

Once both are satisfied, a standard user can run:
```bash
./venv/bin/python3 print_image.py image.png
```

No sudo required.
