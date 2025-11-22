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

### 4. Test Print

**Create a test script** (`test_print.py`):
```python
from escpos.printer import Usb

try:
    p = Usb(0x4b43, 0x3538, in_ep=0x81, out_ep=0x03)
    p.text("Hello World\n")
    p.text("MC582H Test Print\n")
    p.cut()
    print("Success")
except Exception as e:
    print(f"Error: {e}")
```

**Run the test:**
```bash
sudo ./venv/bin/python3 test_print.py
```

### 5. Print Images

Use the included `project_planning_documents/print_image.py` script:

```bash
sudo ./venv/bin/python3 project_planning_documents/print_image.py /path/to/image.png
```

**Note:** For best results, resize images to 384 pixels wide before printing.

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
│   ├── find_endpoints.py               # Diagnostic tool
│   ├── test_print_caysn_v2.py         # Basic text test
│   └── print_image.py                  # Image printing script
└── python-escpos/                      # Git submodule (ESC/POS library)
```

## Troubleshooting

### Module Not Found Error
If you get `ModuleNotFoundError: No module named 'escpos'`, make sure you're using the Python interpreter from your virtual environment:
```bash
sudo ./venv/bin/python3 script.py
```

### Invalid Endpoint Address
The MC582H uses non-standard USB endpoints. Always specify `in_ep=0x81` and `out_ep=0x03`.

### Image Gets Cut Off
The script `print_image.py` includes paper feed before cutting. If images still get cut off, increase the feed amount in the script.

### Permission Denied
Run with `sudo` or configure udev rules to allow non-root access to the USB device.

## Additional Resources

- Full instruction set: See `MC582H_documentation/`
- Setup log with all troubleshooting steps: `project_planning_documents/configuration_setup_log.md`
- Hardware wiring guide: `project_planning_documents/raspberry_pi_connection_and_setup.md`

## License Notes

This project code is licensed under the MIT License (see `LICENSE`).

Manufacturer-supplied documentation files in `MC582H_documentation/` may not be covered by the MIT license. See `DOCS_LICENSE.md` for details.

## Demo Video

Embedded demo of a successful print run (hosted on YouTube).

[![MC582H print demo](https://img.youtube.com/vi/3RQU2RzL4gs/0.jpg)](https://www.youtube.com/watch?v=3RQU2RzL4gs)

If the embed does not work on GitHub, click the thumbnail above or open the video on YouTube: https://www.youtube.com/watch?v=3RQU2RzL4gs
