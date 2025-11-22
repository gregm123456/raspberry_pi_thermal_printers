# MC582H Embedded Thermal Ticket Printer Instruction Set Printing Example

## Interface use Method

Use serial port: Connect the TX, RX and GND on the serial line to the device (TX-RX cross-connect); Separately powered, using 12~24V3A depending on the version of the power supply you ordered; When the current is less than 3A, the printer may not work or the printing may not be clear, so please pay attention.

Use the USB interface: Connect the USB cable to the printer and computer or device, then power on, install the USB driver we provided, and use it after installation. Separately powered, using 12~24V3A depending on the version of the power supply you ordered; When the current is less than 3A, the printer may not work or the printing may not be clear, so please pay attention.

Fixed data can be edited according to our instruction set example. It is ok to write a function for the data of the variable.

## Text Printing

| Print example: | Instruction description: |
| --- | --- |
| | `1B 40` // Initialize the printer; |
| | `1B 33 10` // Set Row height height 10; |
| | Line spacing range: 10,20,30,40,50,60 |
| | `1B 33 20` |
| | `1B 33 30` |
| | `1B 33 40` |
| | `1B 33 50` |
| | `1B 33 60` |
| `1B 40 1B 33 10 1D 21 11 1B 61 01 57 65 6C 63 6F 6D 65 0D 0A` | |
| | `1D 21 00` // Normal font size |
| | `1D 21 11` // Double the font size |
| | `1D 21 10` // Double the font width |
| `1B 69` | `1D 21 01` // Double the font height |
| | `1B 61 00` // Text left aligned |
| | `1B 61 01` // Text centered alignment |
| | `1B 61 02` // Text Right aligned |
| | `57 65 6C 63 6F 6D 65` // Text print content "Welcome" |
| | `OD 0A` End character, can also be used as a newline |

# Bar code Printing

## Print example:

```
1B 401B 6100 1D 4801 1D 6850 1D 7703 1d 6b 48 0c 303233343536303030303839
0D 0A
0D 0A
0D 0A
1B 69
```

```
1B 401B 6100 1D 4801 1D 6850 1D 7703 1d 6b 4908 3032333435363839
0D 0A
0D 0A
0D 0A
1B 69
```

```
1B 401B 6100 1D 4801 1D 6850 1D 7702 1d 6b 4810 30323334353638393032333435303233
0D 0A
0D 0A
0D 0A
1B 69
```

## Instruction description:

`1B 40`
// Initialize the printer;

`1B 6100` // Bar code left;
`1B 6101` // Bar code centered;
`1B 6102` // Bar code Right;

`1D 4801` // Data is displayed above the barcode;
`1D 4802` // Data is displayed below the barcode;
`1D 4803` // Data is displayed above and below the barcode;
`1D 4800` // Number that does not display a barcode;

`1D 6850` // `1D 68` Set the bar code height 50 for 80 Height: Height range 10-200;

`1D 7703` // `1D 77` Set the barcode width 03 for 3 Width; Width range 1-6;

`1D 6B 49` // Barcode type: CODE128;
`0c 3132333435363738393130` // `0c` For 13-bit data length;
Bar code data `31323334353637383931 30` = 12345678910;

## QR code Printing

## Print example:

```
1b 40
1d 28 6b 0300314308
1d 28 6b 0300314530
1d 28 6b 0600315030414243
1b 6101
1d 28 6b 0300315230
1d 28 6b 0300315130
0d 0a
0d 0a
0D 0A
1B 69
```

## Print example:

```
1b 401d 2100
```

## Instruction description:

`1b 40` // Initialize the printer;
`1d 28 6b 03003143 03` // QR code size; `43 02`、`43 03`、`43 04`、`43 05`、 `43 06`、`43 07`、`43 08`
`1d 28 6b 0300314530` // Fixed;
`1d 28 6b 0600315030414243` // `06 00` Data length; If the data content has 81 data, plus 3 QR code fixed instructions is 84 digits. Converting decimal 84 to hex is 54 (`3150304142 43`) 6 data lengths, `315030` Fixed, `414243` QR code content
`1b 61 01` // `00` QR code Left; `01` QR code Centered; `10` QR code Right;
`1d 28 6b 03003152 30` // Fixed;
`1d 28 6b 03003151 30` // Fixed;

## Instruction description:

`1b 40` // Initialize the printer;

# Text and Alignment Examples

```
1b 61 01
57 65 6C 63 6F 6D 65 0d 0a 0d 0a
0d 0a
0D 0A
1B 6D
```

`1b 61 01` // `00` left aligned; `01` Centered alignment; `10` Right aligned;
`1d 21 00` // `00` Normal; `01` Double the font width; `10` Double the font height; `11` Double the font size;
`57 65 6C 63 6F 6D 65` // Text print content "Welcome"
`0d 0a` // End;

# Picture Printing

## Print example:

```
1D 76300007002 F 00
00000000000000000000000000000000000
000000000000007 F0 000000001 FF FF 580000
00 1F DF FF FC 000000 E0 0040 FC 000007800001
FC 0006 1E 00 7E 07 FE 0001 7E 03 FE 1F FE 80 1C 44
07 FE 3F FE CO 1F 8007 EO 3F F8 CO 1E CO 0000 FF E1
80 1E 400033 FF 0700 1E 60000007 F 00007 F 3400
00 FE 00007 F 720007 FC 00007 F CC 00 F1 FC 0000
7E 870001 F8 0000 3C 03 C1 C3 F0 0000001 FF E7
E0 000000007 F F7 C0 00000001 F F7 80000000
0007 FF 000000000001 FE 00000000000007 E 00
00000000007 E 00000000000007 E 000000000
00 6E 000000000000 F6 000000000000 C6 0000
0000001 C2 000000000001 C1 000000000001
8100000000003810000000000701000000
00000700000000000070000000000000700
000000000064000000000009400000000
0009000000000000000000000000000000
0000000000000000000000000000000000
0000000000
0D 0A 0D 0A 0D 0A
0D 0A
1B 69
```

## Instruction description:

`1D 76 30` // Print horizontal modulo image data;
`00` // 4th bit data normal picture size;
`0700` Picture Width;
`2F 00` Picture Height;
The rest of the data is the picture data, and the picture data pixels are the width times the height = `0700` * `2F 00` = 329 Point;
`0D 0A` // End;

## Out of Paper, Paper Cutting Instruction

## Instruction description:

Send a command to check if there is no paper: `100401`
Out of paper: `EF 23 1A`;
With paper: `FE 23 12`;

`0D 0A` // End Newline;
`1B 69` // Full Cut
`1B 6D` // Half-Cut

# Print Status Reply:

There is no need to issue an instruction, the printer will automatically return to the printing state; if the data is sent continuously, and the printer does not receive data for more than 200 ms, it is considered that the printing is complete.
Return data: `FC 4F 4B`: printing completed;
Return data: `FC 6E 6F`: print failed;

When printing is completed, it will automatically return to `FC 4F 4B` this code, indicating that printing is complete. Returns `FC 6E 6F` if printing fails. When there is no paper during printing, it will automatically return to the `EF 23 1A` code, indicating that there is no paper, and return to `FC 6E 6F`;

## Example of Content Printing:

```
1B 40
1B 3310 1D 2111 1B 61015765 6C 63 6F 6D 65 0D 0A
1B 3310 1D 2100 1B 61014152 4C 2049 4E 475443 4E 2054582023393938 0D 0A
1B 3320 1D 2100 1B 6100 2A 53656173 6F 6E 7320477265657469 6E 67732648617070792048 6F 6C 6C 646179 0D 0A
1B 6100333536393732202020 5A 4F 41552053 6C 75736368202020203239 2E 3941 0D 0A
3331303030303035373632382020204350 4E 2F 333536393732 0D 0A
53554254 4F 5441 4C 2020202020202020202020202020203239 2E 39 0D 0A
20202054 4F 5441 4C 0D 0A
5646202020202041 6D 6572696361204578707265737320203239 2E 39 0D 0A
1B 6101 2D 20 2D 20 2D 20 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
```