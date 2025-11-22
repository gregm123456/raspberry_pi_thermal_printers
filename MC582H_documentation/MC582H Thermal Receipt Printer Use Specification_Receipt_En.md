# MC582H Embedded Thermal Receipt Printer

## Specification

## - Product Parameters and Applications

### Product Parameters:

| Product Category | | Embedded Thermal Printer | | |
| :---: | :---: | :---: | :---: | :---: |
| Product Series | | MC582H | | |
| Communication Interface | | RS232+TTL+USB | | |
| Power supply | Power supply | Switching power supply or motherboard power | | |
| | Working Voltage | $12 \sim 24 \mathrm{~V}$ | | |
| | Working Current | $1 \sim 2.5 \mathrm{~A}$, Instantaneous current $\approx 3 \mathrm{~A}$ | | |
| Serial port settings | | Default Baud Rate is 115200. (Can be set according to actual needs) | | |
| | | Parity check: No | Data bits: 8 | Stop position: 1 |
| printing method | | Thermal dot matrix printing | | |
| Print color | | Black and white output | | |
| Resolution | | 203DPL8 points / mm, 384 points per line | | |
| Paper type | | Thermal Receipt paper | | |
| Paper roll specification | Paper Roll width | 57MM $\pm 0.5 \mathrm{MM}$, Paper thickness $55-90 \mu \mathrm{~m}$ | | |
| | Paper roll diameter | Max: 50 mm | | |
| Print content | Text | Support | | |
| | Picture | Support | | |
| | Bar code | Support | | |
| | QR code | Support | | |
| Fixed Method | | There are sliders on both sides of the printer | | |
| Print life | | 50 km | | |
| Printing speed | | 90MM/S | | |
| Character Set | | GB2312 Chinese character library 24X24 international first- and second-level font library, 12X24 standard ASCII code, and can read Chinese characters and characters Enlarge 1-4 times to print | | |
| Paper tearing method | | Automatic paper cutting, supporting full or half cutting | | |
| Print status reply | | Automatic reply status after printing completion, supporting automatic reply and feedback for paper shortage status: | | |
| Paper loading method | | Easy to install paper structure, front panel with paper compartment cover for paper exchange | | |
| Out of paper detection | | Send command query | | |
| Print command | | ESC/POS compatible instruction set (see "Printer Instruction Set" for details) | | |
| Platform support | Support microcontroller development, Android development, Arduino, Linux serial port development and Windows system driver printing and other platforms | |
| :---: | :---: | :---: |
| Product Size | Appearance size | $117.8 * 102.6 * 58 \mathrm{MM}\left(\mathrm{L}^{*} \mathrm{~W}^{*} \mathrm{H}\right)$ |
| | Installation size | $110 * 95 * 56 \mathrm{MM}$ |
| Operating temperature | $-20^{\circ} \mathrm{C} \sim 50^{\circ} \mathrm{C}$ | |
| Relative humidity | $10-80 \%$ | |

### Application Field:

The product is mainly used in "weighing instrument", "medical equipment", "self-service ordering machine", "supermarket ticket printing", "self-service bag storage cabinet", "all kinds of instruments" and other intelligent terminal equipment that need to print thermal receipts, mainly used to print transaction vouchers and other information.

The printer comes with a paper bin, and the paper bin can be put 50MM diameter of the small ticket paper roll, easy to use, panel open cover for paper change, easy to replace the paper roll operation;

It can send data to the printer by means of instructions through the serial port for secondary development, and can also use Android devices to connect to the printer for secondary development (secondary development kit is provided), supporting Windows system and Linux printing.

## 二. Parameters of paper roll

1. Thermal receipt paper roll

| Code Name | Definition | Maximum value (mm) | Minimum value (mm) |
| :---: | :---: | :---: | :---: |
| a | Paper width | $57 \pm 0.5$ | 30 |
| b | Paper thickness | 0.1 | 0.05 |

## 三. Appearance Size Drawing

[Image of Appearance Size Drawing would be here if provided as an image - Placeholder]

## 四. Printer Function Description

### Print Test:

### 1. How to Print the Test Page:

This printer is a wide voltage version, support $12 \mathrm{~V} \sim 24 \mathrm{~V}$ power input, the current is recommended to use 3 A, connect the printer to $12 \mathrm{~V} \sim 24 \mathrm{~V} 3 \mathrm{~A}$ power supply, and then place the thermal paper in the paper bin, pull out a small piece of paper, cover the paper bin cover, and then long hold down the paper key for about 3 seconds, you will print a test page.
2. The maximum voltage cannot exceed 24 V, otherwise it will burn out the motherboard and make it unusable.

### 3. Pilot lamp Status:

| Pilot lamp | Power State | Under normal power-on state, the green light is long on; |
| :--- | :--- | :--- |
| | Fault State | When there is a lack of paper, the red light flashes three times and goes out. |
| Buzzer | Power State | When the power is on normally, the buzzer stops after two drops; |
| | Fault State | When there is a lack of paper, drop three times, stop once, and stop after detecting a drop of paper; |

### 4. Printer Interface Introduction:

[Image of Printer Interface Introduction would be here if provided as an image - Placeholder]

## 五. USB and Serial Port Definition

### Warm Reminder:

The pin is defined from right to left in the direction laid out in the figure above, with the left being the first pin, arranged in sequence. The corresponding pins are defined in the table below. (The corresponding pin definitions are also indicated at the interface)

| Red 2PIN Power Socket - Pin Definition (From left to Right) | | USB Pin Definition (From left to Right) | | Serial Port Pin Definition (From left to Right) | |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Pin number | Signal name | Pin number | Signal name | Pin number | Signal name |
| 1 | GND ( - ) | 1 | GND | 1 | GND |
| 2 | VH ( + ) | 2 | D+ | 2 | RX |
| | | 3 | D- | 3 | TX |
| | | 4 | VBUS | 4 | DTR |
| VH is the positive electrode of the power supply; GND is a negative electrode; Power Supply of the Printer is 12 V $\sim 24 \mathrm{~V}$, and the Current is Recommended to use 3A. | | The USB interface can be connected to Android devices for secondary development. The USB port is only used for communication and cannot be used as a power supply port. Please note! | | TX on the printer driver board to RX on the device; RX on the printer driver board to TX on the device; Default Baud Rate is 115200. | |

### Contact us:

Work Email: 3122285228@qq.com;

If you have any questions in the test or use, please feel free to contact us, so that we can solve your questions in time!