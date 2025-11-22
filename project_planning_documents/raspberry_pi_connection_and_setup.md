# MC582H Thermal Printer - Raspberry Pi Connection and Setup Guide

This document outlines the hardware wiring, electrical connections, and software configuration required to connect the MC582H Embedded Thermal Printer to a Raspberry Pi 4 or 5 running Ubuntu Bookworm (Headless).

## 1. Hardware Requirements

*   **Printer:** MC582H Embedded Thermal Receipt Printer
*   **Computer:** Raspberry Pi 4 or 5
*   **OS:** Ubuntu Bookworm (Headless / Server)
*   **Power Supply:** External DC Power Supply (12V - 24V, Minimum 3A).
    *   *Note: The printer cannot be powered directly by the Raspberry Pi.*
*   **Cables:**
    *   2-pin Power Cable (usually included with printer pigtails)
    *   USB Cable (4-pin header to USB-A) OR Serial Cable (depending on chosen method)

## 2. Electrical & Power Wiring

**WARNING:** Incorrect power connections can permanently damage the printer or the Raspberry Pi. Double-check all polarities before powering on.

### Power Supply Connection
The MC582H requires a dedicated power source.
*   **Voltage:** 12V to 24V DC.
*   **Current:** 3A recommended (Peak current can reach ~3A).

**Wiring the 2-Pin Power Connector (Red Header):**
Looking at the printer interface (or referring to the documentation):
*   **Pin 1 (Left):** GND (-) -> Connect to Power Supply Negative
*   **Pin 2 (Right):** VH (+) -> Connect to Power Supply Positive (12-24V)

**Common Ground:**
If you are connecting the printer to the Raspberry Pi via **GPIO/Serial**, you **MUST** connect the Power Supply GND to a Raspberry Pi GND pin to establish a common ground reference. If using USB, the ground is shared via the USB cable.

## 3. Data Connection Methods

There are two primary ways to connect the printer for data: USB or Serial (TTL/RS232).

*   **Serial (UART):** This is the **officially documented method** for Linux integration according to the manufacturer's spec sheet ("Linux serial port development").
*   **USB:** While the manufacturer emphasizes Windows for USB (via a driver), this printer can typically be controlled on Linux using **Raw USB** commands via the `python-escpos` library. This is often easier than wiring serial pins but relies on the library's ability to claim the USB interface.

### Method A: USB Connection (Easiest / Recommended to try first)

The printer has a 4-pin header for USB. You may need to wire this to a standard USB-A plug to insert into the Raspberry Pi.

**Printer USB Header Pinout (Left to Right):**
1.  **GND**
2.  **D+**
3.  **D-**
4.  **VBUS** (5V)

**Wiring to Standard USB Cable:**
Strip a standard USB cable and connect as follows:

| Printer Pin | Signal | Standard USB Wire Color | USB-A Pin |
| :--- | :--- | :--- | :--- |
| 1 | GND | Black | 4 |
| 2 | D+ | Green | 3 |
| 3 | D- | White | 2 |
| 4 | VBUS | Red | 1 |

*Note: The VBUS connection allows the host (Pi) to detect the device, but it does not power the printer's printing mechanism.*

### Method B: Serial Connection (Advanced)

**Caution:** The MC582H documentation mentions "RS232+TTL".
*   **RS232 Levels:** +/- 12V. **Connecting this directly to Pi GPIO will destroy the Pi.**
*   **TTL Levels:** Usually 5V or 3.3V. The Pi uses 3.3V logic. If the printer uses 5V logic, a Logic Level Converter is required to protect the Pi's RX pin.

**Pinout (4-Pin Serial Header):**
1.  **GND**
2.  **RX** (Printer Receive)
3.  **TX** (Printer Transmit)
4.  **DTR**

**Wiring to Raspberry Pi GPIO (UART):**
*   **Printer GND** -> Pi GND (Pin 6, 9, etc.)
*   **Printer RX** -> Pi TX (GPIO 14 / Pin 8)
*   **Printer TX** -> Pi RX (GPIO 15 / Pin 10) *(Use Level Shifter if Printer is 5V/RS232)*

**Configuration:**
*   Default Baud Rate: **115200**

## 4. Software Setup (Ubuntu Bookworm)

### Step 1: System Preparation
Ensure your system is up to date.
```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Permissions
Add your user (e.g., `ubuntu` or `pi`) to the `dialout` (for serial) and `lp` (for USB/printer) groups to access hardware without `sudo`.

```bash
sudo usermod -a -G dialout,lp $USER
# You must logout and login again for this to take effect.
```

### Step 3: Verify Connection

**For USB:**
Run `lsusb`. You should see a device corresponding to the printer (often generic or with a specific Vendor/Product ID).
```bash
lsusb
```
Check if a kernel device was created (usually `/dev/usb/lp0` or similar):
```bash
ls -l /dev/usb/lp*
```

**For Serial:**
You must enable the hardware serial port and disable the serial console.
1.  Edit `/boot/firmware/cmdline.txt` (or `/boot/cmdline.txt`): Remove `console=serial0,115200`.
2.  Reboot.
The device will likely be `/dev/ttyS0` or `/dev/serial0`.

### Step 4: Python Environment Setup
We will use the `python-escpos` library available in this workspace.

1.  **Install Dependencies:**
    ```bash
    sudo apt install python3-pip python3-venv libusb-1.0-0-dev
    ```

2.  **Create Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install python-escpos:**
    (Assuming you are in the root of the workspace)
    ```bash
    pip install ./python-escpos
    ```

### Step 5: Testing the Printer

Create a test script `test_print.py`:

**USB Test:**
```python
from escpos.printer import Usb

# You need to find the Vendor ID (idVendor) and Product ID (idProduct) from 'lsusb'
# Example: Bus 001 Device 004: ID 0416:5011 Winbond Electronics Corp.
# p = Usb(0x0416, 0x5011)

try:
    # Replace with your actual IDs
    # If you don't know them yet, run lsusb
    p = Usb(0xYYYY, 0xZZZZ) 
    p.text("Hello World\n")
    p.barcode('123456', 'EAN13', 64, 2, '', '')
    p.cut()
except Exception as e:
    print(f"Error: {e}")
```

**Serial Test:**
```python
from escpos.printer import Serial

try:
    # Adjust port to /dev/ttyS0, /dev/ttyAMA0, or /dev/USB0 (if using USB-Serial adapter)
    p = Serial(devfile='/dev/serial0', baudrate=115200)
    p.text("Hello Serial World\n")
    p.cut()
except Exception as e:
    print(f"Error: {e}")
```
