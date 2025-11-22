# MC582H Thermal Printer - Raspberry Pi Setup Guide

Complete setup instructions for the MC582H Embedded Thermal Receipt Printer on Raspberry Pi (Ubuntu Linux).

## Hardware Specifications

- **Model:** MC582H Embedded Thermal Receipt Printer
- **Interfaces:** RS232+TTL+USB
- **Paper Width:** 58mm (384 dots/pixels)
- **Resolution:** 203 DPI
- **Power:** 12V-24V DC, 3A (independent power supply required)
- **Communication:** USB (Vendor ID: `0x4b43`, Product ID: `0x3538`)

## Quick Start

### 1. Hardware Connection

**Power:**
- Connect an external 12V-24V 3A power supply to the red 2-pin power connector
- Pin 1 (left): GND (-)
- Pin 2 (right): VH (+)
- **WARNING:** Do not exceed 24V or you will damage the printer

**USB Connection:**
1. Connect the printer's USB port to your Raspberry Pi
2. The USB connection is for data only, not power
3. Power on the printer

### 2. Software Setup

**Install System Dependencies:**
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-venv libusb-1.0-0-dev
```

**Add User to Necessary Groups:**
```bash
sudo usermod -a -G dialout,lp $USER
# Log out and log back in for this to take effect
```

**Create Python Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Install Python Dependencies:**
```bash
pip install python-escpos pyusb
```

### 3. Verify Connection

**Check if printer is detected:**
```bash
lsusb
```

You should see: `Bus XXX Device XXX: ID 4b43:3538 Caysn Thermal Printer`

### 4. Configure USB Permissions (Recommended)

To avoid requiring `sudo` for every print operation, set up udev rules:

**Create udev rule:**
```bash
sudo nano /etc/udev/rules.d/99-thermal-printer.rules
```

**Add this line:**
```
# MC582H Thermal Printer (Caysn)
SUBSYSTEM=="usb", ATTR{idVendor}=="4b43", ATTR{idProduct}=="3538", MODE="0666", GROUP="lp"
```

**Reload rules and reconnect printer:**
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
# Unplug and replug the USB cable
```

### 5. Test Print

Use the included test script: [`project_planning_documents/test_print_caysn_v2.py`](project_planning_documents/test_print_caysn_v2.py)

```bash
./venv/bin/python3 project_planning_documents/test_print_caysn_v2.py
```

*(No `sudo` needed if udev rules are configured)*

### 6. Print Images

Use the user-friendly image printing script: [`project_planning_documents/print_image_user.py`](project_planning_documents/print_image_user.py)

```bash
./venv/bin/python3 project_planning_documents/print_image_user.py /path/to/image.png
```

**Note:** For best results, resize images to 384 pixels wide before printing.

**If you get permission errors:** Either run with `sudo` or verify udev rules are configured (see step 4).

## Key Configuration Details

When using `python-escpos` with this printer, always use these parameters:

```python
from escpos.printer import Usb

p = Usb(
    0x4b43,           # Vendor ID
    0x3538,           # Product ID
    in_ep=0x81,       # Input endpoint
    out_ep=0x03       # Output endpoint
)

# Configure printer profile for proper image centering
p.profile.profile_data['media'] = {
    'width': {'pixels': 384},
    'dpi': 203
}
```

## Project Structure

```
.
├── README.md                           # This file
├── MC582H_documentation/               # Manufacturer documentation
│   ├── MC582H Embedded Thermal Receipt Printer Instruction Set_Receipt_En.md
│   ├── MC582H Embedded Thermal Ticket Printer Instruction Set Printing Example.md
│   ├── MC582H Thermal Receipt Printer Use Specification_Receipt_En.md
│   └── printer_email.md
├── project_planning_documents/
│   ├── configuration_setup_log.md      # Setup troubleshooting log
│   ├── raspberry_pi_connection_and_setup.md
│   ├── image_print_integration_plan.md # Non-sudo setup guide
│   ├── find_endpoints.py               # Diagnostic tool
│   ├── test_print_caysn_v2.py         # Basic text test
│   ├── print_image.py                  # Image printing script (requires sudo)
│   └── print_image_user.py            # Image printing script (user mode)
└── python-escpos/                      # Git submodule (ESC/POS library)
```

Quick links:

- Non-sudo setup guide: [project_planning_documents/image_print_integration_plan.md](project_planning_documents/image_print_integration_plan.md)
- Diagnostic tool: [project_planning_documents/find_endpoints.py](project_planning_documents/find_endpoints.py)
- Basic text test: [project_planning_documents/test_print_caysn_v2.py](project_planning_documents/test_print_caysn_v2.py)
- Image print (user): [project_planning_documents/print_image_user.py](project_planning_documents/print_image_user.py)
- Image print (sudo): [project_planning_documents/print_image.py](project_planning_documents/print_image.py)
- Setup log: [project_planning_documents/configuration_setup_log.md](project_planning_documents/configuration_setup_log.md)
- Wiring guide: [project_planning_documents/raspberry_pi_connection_and_setup.md](project_planning_documents/raspberry_pi_connection_and_setup.md)
- Manufacturer docs directory: [MC582H_documentation/](MC582H_documentation/)

## Troubleshooting

### Permission Denied
**Preferred solution:** Configure udev rules (see Quick Start step 4) so you don't need `sudo`.

**Temporary workaround:** Run with `sudo`:
```bash
sudo ./venv/bin/python3 project_planning_documents/print_image_user.py image.png
```

### Module Not Found Error
Make sure you're using the Python interpreter from your virtual environment:
```bash
./venv/bin/python3 script.py
```

### Invalid Endpoint Address
The MC582H uses non-standard USB endpoints. Always specify `in_ep=0x81` and `out_ep=0x03`.

### Image Gets Cut Off
The scripts include paper feed before cutting. If images still get cut off, increase the feed amount in the script (edit the `"\n" * 5` line).

## Additional Resources

 - **Non-sudo setup guide:** [project_planning_documents/image_print_integration_plan.md](project_planning_documents/image_print_integration_plan.md) - Complete guide for running without `sudo`
 - **Full instruction set:** [MC582H_documentation/](MC582H_documentation/)
 - **Setup log with all troubleshooting steps:** [project_planning_documents/configuration_setup_log.md](project_planning_documents/configuration_setup_log.md)
 - **Hardware wiring guide:** [project_planning_documents/raspberry_pi_connection_and_setup.md](project_planning_documents/raspberry_pi_connection_and_setup.md)

## License Notes

This project code is licensed under the MIT License (see `LICENSE`).

Manufacturer-supplied documentation files in `MC582H_documentation/` may not be covered by the MIT license. See `DOCS_LICENSE.md` for details.

## Demo Video

Embedded demo of a successful print run (hosted on YouTube).

[![MC582H print demo](https://img.youtube.com/vi/3RQU2RzL4gs/0.jpg)](https://www.youtube.com/watch?v=3RQU2RzL4gs)

If the embed does not work on GitHub, click the thumbnail above or open the video on YouTube: https://www.youtube.com/watch?v=3RQU2RzL4gs
