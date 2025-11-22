# Configuration and Setup Log

## Initial Connection (USB)

**Date:** November 22, 2025
**Action:** Plugged printer into Raspberry Pi via USB.
**Command:** `lsusb`

**Output:**
```text
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 002: ID 1915:1025 Nordic Semiconductor ASA USB Composite Device
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 002: ID 152d:581d JMicron Technology Corp. / JMicron USA Technology Corp. SSK  Storage
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 002: ID 4b43:3538 Caysn Thermal Printer
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

**Identified Device:**
*   **Device Name:** Caysn Thermal Printer
*   **Vendor ID:** `0x4b43`
*   **Product ID:** `0x3538`

**Next Steps:**
1.  Configure `python-escpos` with these USB IDs.
2.  Attempt a test print.

## Test 1: Basic Text Print (Python)

**Script:** `test_print_caysn.py`
```python
from escpos.printer import Usb

# Vendor ID: 0x4b43, Product ID: 0x3538
try:
    p = Usb(0x4b43, 0x3538)
    p.text("Hello World\n")
    p.text("Connection Successful!\n")
    p.cut()
    print("Success")
except Exception as e:
    print(f"Error: {e}")
```

**Command to run:**
```bash
sudo python3 test_print_caysn.py
```
*(Note: `sudo` might be required if udev rules aren't set up yet)*

**Result:**
`ModuleNotFoundError: No module named 'escpos'`

**Diagnosis:**
You installed the library in a virtual environment (`venv`), but `sudo python3` defaults to the system-wide Python, which doesn't have the library.

**Correct Command:**
Point `sudo` explicitly to the Python executable inside your virtual environment:
```bash
sudo ./venv/bin/python3 test_print_caysn.py
```

**Result:**
`RuntimeError: Printing with USB connection requires a usb library tobe installed.`

**Diagnosis:**
`python-escpos` does not install USB support by default. It requires the `pyusb` library.

**Fix:**
Install the missing dependency:
```bash
pip install pyusb
```

**Retest:**
```bash
sudo ./venv/bin/python3 test_print_caysn.py
```

**Result:**
`Error: Invalid endpoint address 0x1`

**Diagnosis:**
The library tried to guess the USB "Endpoint" (the channel used to send data) and guessed `0x01`, which is incorrect for this specific printer model. We need to find the correct "OUT" endpoint address.

**Action:**
Run a diagnostic script to list the printer's USB endpoints.

**Script:** `find_endpoints.py`
```python
import usb.core

# Vendor: 0x4b43, Product: 0x3538
dev = usb.core.find(idVendor=0x4b43, idProduct=0x3538)

if dev is None:
    print("Device not found")
else:
    print("Device found!")
    for cfg in dev:
        print(f"Configuration: {cfg.bConfigurationValue}")
        for intf in cfg:
            print(f"  Interface: {intf.bInterfaceNumber}, Alt: {intf.bAlternateSetting}")
            for ep in intf:
                print(f"    Endpoint: {hex(ep.bEndpointAddress)}")
                # 0 = Control, 1 = Isochronous, 2 = Bulk, 3 = Interrupt
                type_attr = ep.bmAttributes & 0x03
                direction = "IN" if (ep.bEndpointAddress & 0x80) else "OUT"
                print(f"      Type: {type_attr} (2=Bulk), Direction: {direction}")
```

**Command:**
```bash
sudo ./venv/bin/python3 find_endpoints.py
```

**Output:**
```text
Device found!
Configuration: 1
  Interface: 0, Alt: 0
    Endpoint: 0x81
      Type: 2 (2=Bulk), Direction: IN
    Endpoint: 0x3
      Type: 2 (2=Bulk), Direction: OUT
```

**Analysis:**
The printer uses Endpoint `0x03` for receiving data (OUT), not the default `0x01`.

## Test 2: Text Print with Explicit Endpoints

**Updated Script:** `test_print_caysn_v2.py`
```python
from escpos.printer import Usb

# Vendor: 0x4b43, Product: 0x3538
# Out Endpoint: 0x03 (found via scan)
# In Endpoint: 0x81 (found via scan)
try:
    p = Usb(0x4b43, 0x3538, in_ep=0x81, out_ep=0x03)
    
    p.text("Hello World\n")
    p.text("Endpoint Configuration Correct!\n")
    p.cut()
    print("Success")
except Exception as e:
    print(f"Error: {e}")
```

**Command:**
```bash
sudo ./venv/bin/python3 test_print_caysn_v2.py
```

**Result:**
Success! The printer printed "Hello World" and "Endpoint Configuration Correct!".

**Conclusion:**
The printer is fully operational via USB using `python-escpos` with explicit endpoint configuration (`in_ep=0x81`, `out_ep=0x03`).

## Test 3: Image Printing

**Script:** `print_image.py`
This script takes an image path as an argument, configures the printer profile (width: 384px, dpi: 203), prints the image, feeds paper, and cuts.

**Command:**
```bash
sudo ./venv/bin/python3 print_image.py celadon.png
```

**Result:**
Success! The image printed correctly, centered, and the paper was cut after feeding.

**Key Configuration Details:**
*   **Vendor ID:** `0x4b43`
*   **Product ID:** `0x3538`
*   **Endpoints:** `in_ep=0x81`, `out_ep=0x03`
*   **Profile:** `media.width.pixels=384`, `media.dpi=203`
