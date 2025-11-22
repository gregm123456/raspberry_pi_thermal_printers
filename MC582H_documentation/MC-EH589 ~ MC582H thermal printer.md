# PAGE 1
# MC582H Thermal Receipt Printer Instruction Set

Version Number: V5.23_EN

# PAGE 2
# Catalogue

1 Instruction Interpretation ..... 3
1.1 Initialize Printer ..... 3
1.2 Print Test Page ..... 3
1.3 Set the Character Printing Mode ..... 3
1.4 Set Character Size ..... 4
1.5 Set the Print Alignment ..... 5
1.6 Horizontal Position Print Line Segments (Curve Print Command) ..... 5
1.7 Set the Horizontal TAB Position ..... 10
1.8 Barcode Printing Command ..... 13
1.8.1 Set the Barcode Readable Character (HRI) Print Position ..... 13
1.8.2 Set Barcode Height ..... 13
1.8.3 Set Barcode Width ..... 14
1.8.4 Print Barcode ..... 14
1.9 QR code Printing Command ..... 20
1.9.1 Set the Module Type of the QR Ccode ..... 20
1.9.2 Set the Error Correction Level of QR Code ..... 20
1.9.3 Print QR Code ..... 21
1.9.4 Print QR Code ..... 21
1.10 Print Setup Command ..... 22
1.10.1Set the Line Spacing to $n$ Points ..... 22
1.10.2 Set the Blank Space on the Left ..... 23
1.11 Graphic Print Command ..... 24
1.11.1Figure Vertical Modulus Data ..... 24
1.11.2 Picture Horizontal Module Data Printing ..... 25
2 Printer Status and Settings ..... 27
2.1 Paperless State ..... 27
2.2 Print Status ..... 27
2.3 Set the Baud Rate of the Printer Serial Port ..... 28
2.4 Set the status of the serial port (this command is not saved when powered off) ..... 29
2.5 Set Whether to Feed Paper and the Number of Feed Lines ..... 29
2.6 Full-Cut Paper ..... 30
2.7 Half Cut Paper ..... 30

# PAGE 3
# 1 Instruction Interpretation

## 1.1 Initialize Printer

| Instruction Name | Initialize Printer |
|---|---|
| Instruction code | ASCII: ESC @ DDecimal system: 2164 Hexadecimal: 1B 40 |
| Function Description | Initialize the following for the printer: Clear print cache The default values of each parameter are restored |
| Parameter Range | NO |
| Default Value | NO |
| Supported Model | All models |
| Matters Attention | NO |
| Use Example | NO |

## 1.2 Print Test Page

| Instruction Name | Print Test Page |
|---|---|
| Instruction code | ASCII : DC2 T DDecimal system : 1894 Hexadecimal : 1254 |
| Function Description | The printer prints a self-test page that contains the printer's program version, communication interface type, code page, and other data. |
| Parameter Range | NO |
| Default Value | NO |
| Supported Model | All models |
| Matters Attention | NO |
| Use Example | 1B 401254 |

## 1.3 Set the Character Printing Mode

| Instruction Name | Set the Character Printing Mode |
|---|---|
| Instruction | ASCII : ESC ! n |

# PAGE 4
| code | DDecimal system : 2133 n Hexadecimal : 1B 21 n |
|:---:|:---:|
| Function <br> Description | To set the printing method of the character (font, backwhite, inverted, bold, double height, double width, and underscore), the bits of parameter n are defined as follows: <br> Position Feature Value <br> 0 1 <br> 0 Type Normal Small Character <br> 1 To be Defined <br> 2 To be Defined <br> 3 Bold cancels Settings <br> 4 Double height cancels setting <br> 5 Double width cancels setting <br> 6 To be Defined <br> 1 Underline cancels setting |
| Parameter <br> Range | NO |
| Default Value | $\mathrm{n}=0$ |
| Supported Model | All models |
| Matters <br> Attention | This command is valid for both Chinese and foreign fonts When ESC@, printer reset, power off, this instruction is invalid |
| Use Example | 1B 40 1B 2101303132 OD 0A <br> 1B 40 1B 2102303132 OD 0A <br> 1B 40 1B 2104303132 OD 0A <br> 1B 40 1B 2108303132 OD 0A <br> 1B 40 1B 2110303132 OD 0A <br> 1B 40 1B 2120303132 OD 0A <br> 1B 40 1B 2140303132 OD 0A <br> 1B 40 1B 2180303132 OD 0A |

# 1.4 Set Character Size

| Instruction <br> Name | Set Character Size |
|:---:|:---:|
| Instruction <br> code | ASCII : GS ! n <br> DDecimal system : 2933 n <br> Hexadecimal : 1d 21 n |
| Function <br> Description | 1d 2100 Normal Font (Default) <br> 1d 2111 Double the height and double the width <br> 1d 2110 Font double width <br> 1d 2101 Font double height |
| Parameter <br> Range | NO |
| Default Value | $\mathrm{n}=0$ |
| Supported <br> Model | All models |

# PAGE 5
| Matters <br> Attention | This command is valid for both Chinese and foreign fonts When ESC@, printer reset, power off, this instruction is invalid |
|:---:|:---:|
| Use Example | 1b 401 d 2100 <br> 4865 6C 6C 6F 2057 6F 72 6C 64 Od 0a <br> 1b 401 d 2111 <br> 4865 6C 6C 6F 2057 6F 72 6C 64 Od 0a <br> 1b 401 d 2110 <br> 4865 6C 6C 6F 2057 6F 72 6C 64 Od 0a <br> 1b 401 d 2101 <br> 4865 6C 6C 6F 2057 6F 72 6C 64 Od 0a |

# 1.5 Set the Print Alignment

| Instruction <br> Name | Set the Print Alignment (Left, Center, Right) |
|:---:|:---:|
| Instruction code | ASCII : ESC a n <br> DDecimal system : 2191 n <br> Hexadecimal : 1B 61 n |
| Function <br> Description | If all the data in a row is aligned, the meaning of the $n$ value is as follows: n Mode <br> 0,48 Left <br> 1,49 Center <br> 2,50 Right |
| Parameter <br> Range | $0 \leqslant n \leqslant 2$ 或 $48 \leqslant n \leqslant 50$ |
| Default Value | $n=0$ |
| Supported Model | All models |
| Matters <br> Attention | When ESC@, printer reset, power off, this instruction is invalid |
| Use Example | 1B 401B 6100 <br> 4465666175 6C 7420 4C 6566742041 6C 6967 6E 6D 65 6E 74 0D 0A <br> 1B 401B 6101 <br> 4365 6E 7465722041 6C 6967 6E 6564 0D 0A <br> 1B 401B 6102 <br> 41 6C 6967 6E 205269676874 0D 0A |

### 1.6 Horizontal Position Print Line Segments (Curve Print Command)

| Instruction <br> Name | Horizontal Position Print Line Segments (Curve Print Command) |
|:---|:---|
| Instruction <br> code | ASCII : GS' n x1sL x1eH x1eL x1eH ...xnsL xnsH xneL xneH <br> DDecimal system : 1D 21 n x1sL x1eH x1eL x1eH ...xnsL xnsH xneL <br> xneH |

# PAGE 6
An enlarged print is shown below: Each horizontal curve segment can be viewed as consisting of these points of segment length 1. If $n$ horizontal lines are printed, the desired curve can be printed by using this command continuously.

Function
xksL : The horizontal coordinates of the lower order starting point of the K line; xksH : The horizontal coordinates of the higher order starting point of the K line; xkeL : The horizontal coordinate of the lower order of the end point of the K-line;
xkeH : The horizontal coordinate of the higher order of the end point of the K line;

The starting position of the coordinate is usually to the left of the print area. The minimum coordinate coordinate is $(0,0)$ and the maximum horizontal coordinate value is $383, \mathrm{xkeL}+\mathrm{xkeH}^{*} 256$
Rows of data may not be arranged in a specified order;

Char SendStr[8];
Char SendStr2[16];
Float i;
Short y1,y2,y1s,y2s;
//Print the Y-axis (one line)
SendStr[0]=0x1D;
SendStr[1]=0x21;
SendStr[2]=1: // A Row
SendStr[3]=30
SendStr[4]=0; // Starting Point
SendStr[5]=104;

# PAGE 7
```c
SendStr=1; // End Point
PreSendData(SendStr,1);
//Print curve
SendStr=0x1D;
SendStr=0x21;
SendStr=3; //Three lines:X-axis,sin and cos function curve
Function
SendStr=180; SendStr=0; // X-Axis Position
SendStr=180; SendStr=0;
for(i=1;i<1200;i++)
{
    y1=sin(i/180*3.1416)*(380-30)/2+180; // Calculate the sin function
coordinates
    y2=cos(i/180*3.1416)*(380-30)/2+180; // Calculate the coordinates
of the cos function
    If(i==1){y1s=y1;y2s=y2;}
    PreSendData(SendStr,1);
    If(y1s<y1)
    {
        PreSendData(&y1s,2); // The sin function is the starting point of
this row
        PreSendData(&y1,2); // The sin function is at the end of that row
    }
    Else
    {
        PreSendData(&y1,2); // The sin function is the starting point of this
row
        PreSendData(&y1s,2); // The sin function is at the end of that row
    }
    If(y2s<y2)
    {
        PreSendData(&y2s,2); // Cos function is the starting point of this
row
        PreSendData(&y2,2); // Cos function is the end point of this row
    }
    Else
    {
        PreSendData(&y2,2); // Cos function is the starting point of this
row
        PreSendData(&y2s,2); // Cos function is the end point of this row
    }
    y1s=y1; // When printing goes to the next line, the sin function
curve starts at the horizontal coordinate
    y2s=y2; // When printing goes to the next line, the cos function
curve starts at the horizontal coordinate
    }
```

# PAGE 8
| | |
|---|---|
| Parameter Range | 0≤n≤8 |
| Default Value | NO |
| Supported Model | Portable Printer |
| Matters Attention | When a point is printed, xkeL=xksL, xkeH=xksH |
| Use Example | 1d 21 01 00 00 00 00 1d 21 01 01 00 0f 00 1d 21 01 10 00 1f 00 1d 21 01 20 00 2c 00 1d 21 01 2d 00 3a 00 1d 21 01 3b 00 44 00 1d 21 01 45 00 4c 00 1d 21 01 4d 00 54 00 1d 21 01 55 00 5c 00 1d 21 01 5d 00 63 00 1d 21 01 64 00 6a 00 1d 21 01 6b 00 11 00 1d 21 01 12 00 11 00 1d 21 01 18 00 1d 00 1d 21 01 1e 00 84 00 1d 21 01 85 00 8a 00 1d 21 01 8b 00 91 00 1d 21 01 92 00 91 00 1d 21 01 98 00 9d 00 1d 21 01 9e 00 a3 00 1d 21 01 a4 00 a9 00 1d 21 01 aa 00 af 00 1d 21 01 b0 00 b4 00 1d 21 01 b5 00 b9 00 1d 21 01 ba 00 bf 00 1d 21 01 c0 00 c4 00 1d 21 01 c5 00 c9 00 1d 21 01 ca 00 cf 00 1d 21 01 d0 00 d4 00 1d 21 01 d5 00 d8 00 1d 21 01 d9 00 dc 00 1d 21 01 dd 00 df 00 1d 21 01 e0 00 e3 00 1d 21 01 e4 00 e6 00 1d 21 01 e1 00 e9 00 1d 21 01 ea 00 ec 00 1d 21 01 ed 00 ef 00 1d 21 01 f0 00 f1 00 1d 21 01 f2 00 f3 00 1d 21 01 f4 00 f5 00 1d 21 01 f6 00 f1 00 1d 21 01 f8 00 f8 00 1d 21 01 f9 00 fa 00 1d 21 01 fb 00 fb 00 1d 21 01 fc 00 fd 00 1d 21 01 fe 00 fe 00 1d 21 01 ff 00 ff 00 1d 21 01 00 01 00 01 1d 21 01 01 01 01 01 1d 21 01 02 01 02 01 1d 21 01 03 01 03 01 1d 21 01 04 01 04 01 1d 21 01 05 01 05 01 1d 21 01 06 01 06 01 1d 21 01 06 01 06 01 1d 21 01 01 01 01 01 1d 21 01 01 01 01 01 1d 21 01 01 01 01 01 1d 21 01 01 01 01 01 1d 21 01 01 01 01 01 1d 21 01 06 01 06 01 1d 21 01 06 01 06 01 1d 21 01 05 01 05 01 1d 21 01 04 01 04 01 1d 21 01 04 01 04 01 1d 21 01 03 01 03 01 1d 21 01 02 01 02 01 1d 21 01 00 01 00 01 1d 21 01 ff 00 ff 00 1d 21 01 fe 00 fe 00 1d 21 01 fc 00 fd 00 1d 21 01 f9 00 fa 00 1d 21 01 f8 00 f8 00 1d 21 01 f6 00 f1 00 1d 21 01 f4 00 f5 00 1d 21 01 f2 00 f3 00 1d 21 01 f0 00 f1 00 1d 21 01 ed 00 ef 00 1d 21 01 ea 00 ec 00 |

# PAGE 9
1d 2101 e1 00 e9 00 1d 2101 e4 00 e6 00 1d 2101 e0 00 e3 00 1d 2101 dd 00 df 00 1d 2101 d9 00 dc 00 1d 2101 d5 00 d8 00 1d 2101 d0 00 d4 00 1d 2101 ca 00 cf 00 1d 2101 c5 00 c9 00 1d 2101 c0 00 c4 00 1d 2101 ba 00 bf 00 1d 2101 b5 00 b9 00 1d 2101 b0 00 b4 00 1d 2101 aa 00 af 00 1d 2101 a4 00 a9 00 1d 2101 9e 00 a3 00 1d 21019800 9d 00 1d 21019200 9100 1d 2101 8b 00 91 00 1d 21018500 8a 00 1d 2101 1e 00 84 00 1d 21011800 1d 00 1d 21011200 11 00 1d 2101 6b 00 11 00 1d 21016400 6a 00 1d 2101 5d 006300 1d 21015500 5c 00 1d 2101 4d 005400 1d 21014500 4c 00 1d 2101 3b 004400 1d 2101 2d 00 3a 00 1d 21012000 2c 00 1d 21011000 1f 00 1d 210101000 f 00 1d 210100000000 1d 210100000000 1d 210101000 f 00 1d 21011000 1f 00 1d 21012000 2c 00 1d 2101 2d 00 3a 00 1d 2101 3b 004400 1d 21014500 4c 00 1d 2101 4d 005400 1d 21015500 5c 00 1d 2101 5d 006300 1d 21016400 6a 00 1d 2101 6b 00 11 00 1d 21011200 11 00 1d 21011800 1d 00 1d 2101 1e 008400 1d 21018500 8a 00 1d 2101 8b 009100 1d 21019200 9100 1d 21019800 9d 00 1d 21019 e 00 a3 00 1d 2101 a4 00 a9 00 1d 2101 aa 00 af 00 1d 2101 b0 00 b4 00 1d 2101 b5 00 b9 00 1d 2101 ba 00 bf 00 1d 2101 c0 00 c4 00 1d 2101 c5 00 c9 00 1d 2101 ca 00 cf 00 1d 2101 d0 00 d4 00 1d 2101 d5 00 d8 00 1d 2101 d9 00 dc 00 1d 2101 dd 00 df 00 1d 2101 e0 00 e3 00 1d 2101 e4 00 e6 00 1d 2101 e1 00 e9 00 1d 2101 ea 00 ec 00 1d 2101 ed 00 ef 00 1d 2101 f0 00 f1 00 1d 2101 f2 00 f3 00 1d 2101 f4 00 f5 00 1d 2101 f6 00 f1 00 1d 2101 f8 00 f8 00 1d 21 01 f9 00 fa 00 1d 21 01 fb 00 fb 00 1d 21 01 fc 00 fd 00 1d 21 01 fe 00 fe 00 1d 21 01 ff 00 ff 00 1d 210100010001 1d 210101010101 1d 210102010201 1d 210103010301 1d 210104010401 1d 210105010501 1d 210106010601 1d 210106010601 1d 210101010101 1d 210101010101 1d 210101010101 1d 210101010101 1d 210101010101 1d 210101010101 1d 210106010601

# PAGE 10
| | 1d 2101060106011 d 210105010501 <br> 1d 2101040104011 d 210104010401 <br> 1d 2101030103011 d 210102010201 <br> 1d 2101000100011 d 2101 ff 00 ff 00 <br> 1d 2101 fe 00 fe 001 d 2101 fc 00 fd 00 <br> 1d 2101 f9 00 fa 001 d 2101 f8 00 f8 00 <br> 1d 2101 f6 00 f1 001 d 2101 f4 00 f5 00 <br> 1d 2101 f2 00 f3 001 d 2101 f0 00 f1 00 <br> 1d 2101 ed 00 ef 001 d 2101 ea 00 ec 00 <br> 1d 2101 e1 00 e9 001 d 2101 e4 00 e6 00 <br> 1d 2101 e0 00 e3 001 d 2101 dd 00 df 00 <br> 1d 2101 d9 00 dc 001 d 2101 d5 00 d8 00 <br> 1d 2101 d0 00 d4 001 d 2101 ca 00 cf 00 <br> 1d 2101 c5 00 c9 001 d 2101 c0 00 c4 00 <br> 1d 2101 ba 00 bf 001 d 2101 b5 00 b9 00 <br> 1d 2101 b0 00 b4 001 d 2101 aa 00 af 00 <br> 1d 2101 a4 00 a9 001 d 2101 9e 00 a3 00 <br> 1d 210198009 d 001 d 210192009100 <br> 1d 2101 8b 0091001 d 210185008 a 00 <br> 1d 2101 1e 0084001 d 210118001 d 00 <br> 1d 2101120011001 d 21016b 001100 <br> 1d 210164006 a 001 d 21015 d 006300 <br> 1d 210155005 c 001 d 21014 d 005400 <br> 1d 210145004 c 001 d 21013 b 004400 <br> 1d 21012 d 003 a 001 d 210120002 c 00 <br> 1d 210110001 f 001 d 210101000 f 00 <br> 1d 210100000000 |
|:---|:---|

# 1.7 Set the Horizontal TAB Position

| Instruction <br> Name | Horizontal Tabulation |
|:---|:---|
| Instruction <br> Code | ASCII : HT <br> Decimal system : 9 <br> Hexadecimal : 09 |
| Function <br> Description | Move the Print Position to the Next Tabulation Position |
| Parameter <br> Range | NO |
| Default <br> Value | NO |
| Supported <br> Model | All models |
| Matters <br> Attention | The TAB position is set by ESC D <br> If the TAB position is not set (there is no horizontal TAB position by default), this <br> instruction is treated as an LF instruction |

# PAGE 11
If the tabulation position is outside the print area, the coordinates are moved to the starting position of the next row (if the row is full, print)

| Instruction <br> Name | |
|:---:|:---:|
| Instruction <br> Code | ASCII : ESC D [d]k NUL <br> Decimal system : 2168 [d]k 0 <br> Hexadecimal : 1B 44 [d]k 00 |
| Function <br> Description | Set the horizontal TAB position. The meanings of the parameters are as follows: d1 ... dk: Horizontal table position, in 8 points, NULL as the end character |
| Parameter <br> Range | XX58: $1 \leqslant \mathrm{~d} \leqslant 46$ ( $\mathrm{d}1<\mathrm{d}2<\cdots \cdots \mathrm{dk}, 1 \leqslant \mathrm{k} \leqslant 16$ ) <br> XX80: $1 \leqslant \mathrm{~d} \leqslant 10$ ( $\mathrm{d}1<\mathrm{d}2<\cdots \cdots \mathrm{dk}, 1 \leqslant \mathrm{k} \leqslant 16$ ) |
| Default <br> Value | [d]k = 0 (default no horizontal tabulation position) |
| Supported <br> Model | All models |
| Matters <br> Attention | The tabulation position is shown as follows: |

Supports a maximum of 16 TAB positions
Using this command cancels previous TAB location Settings
$k$ is used for schematic purposes, No transmission
Transmission [d]k is considered terminated when it encounters NULL
If $d k$ is less than or equal to DK-1, it is regarded as the end, and the remaining data is regarded as ordinary data processing
TAB position can be switched by HT
When the left margin is changed, the tabulating position changes at the same time
When ESC@, printer reset, power off, this instruction is invalid
Use Example 1B 44 0B 121900 0D 0A 202020 4E 61 6D 650955 6E 6974 2D 5072696365 09517561 6E 7469747909 4D 6F 6E 657909 0D 0A 426565662046 6C 6F 7373 0D 0A 0931 2E 3009320932 2E 3030 0D 0A 4475726961 6E 204567 672054617274 0D 0A 09313032 2E 30093209323034 2E 3030 0D 0A 42 65656620427572676572 0D 0A 093931 2E 300932300931383230 2E 3030 0D 0A 0D 0A 0D 0A

Instruction Description:

# PAGE 12
1B 44 0B 12 19 00 ==0B is the width of the first column, 12 is the width of the second column, 19 is the width of the third column, and the remaining width is the last column width ending with a split of 00

| Column 1 0B | Column 2 12 | Column 3 19 | Last Column |
|:---|:---|:---|:---|
| | | | |

Like the width of a row
0D OA Line Feed
202020 4E 61 6D 65 ==20 is a space, the first column of text content"Name" 09 ==as a separate symbol,
55 6E 6974 2D 5072696365 The second column contains text content" Unit-Price"
09 Separate symbol
517561 6E 74697479 The third part of the text content" Quantity"
09 Separate symbol
4D 6F 6E 6579 The fourth column contains text content" Money"
09 Separate symbol
0D OA Line Feed
426565662046 6C 6F 7373 First column text content" Beef Floss"
0D OA Line Feed
09 Separate symbol
31 2E 30 Second case 1.0
09 Separate symbol
32 The third column 2
09 Separate symbol
32 2E 3030 Fourth column 2.00
0D OA Line Feed
4475726961 6E 204567672054617274 First column" Durian Egg Tart"
0D OA
09 Separate symbol
313032 2E 30 Second case 102.0
09 Separate symbol
32 Column 32
09 Separate symbol
323034 2E 3030 Fourth column 204.00
0D OAine Feed
4265656620427572676572 First column" Beef Burger"
0D OA Line Feed
09 Separate symbol
3931 2E 30 Second case 91.0
09 Separate symbol
3230 The third column 20
09 Separate symbol
31383230 2E 3030 Fourth column 1820.00
0D OA Line Feed

# PAGE 13
# 1.8 Barcode Printing Command

### 1.8.1 Set the Barcode Readable Character (HRI) Print Position

| Instruction <br> Name | Set the Barcode Readable Character (HRI) Print Position |
|:---:|:---:|
| Instruction <br> Code | ASCII : G5 H n <br> Decimal system : 2912 n <br> Hexadecimal : 1D 48 n |
| Function <br> Description | Set the barcode readable character (HRI) print position. The meaning of the parameter $n$ is as follows: <br> n Print Position <br> 0,48 Not Print <br> 1,49 Above the Barcode <br> 2, 50 Below the Barcode <br> 3, 51 Barcode Above and Below |
| Parameter <br> Range | $0 \leqslant n \leqslant 3$ 或 $48 \leqslant n \leqslant 51$ |
| Default Value | $n=0$ |
| Supported <br> Model | All Models |
| Matters <br> Attention | When ESC@, printer reset, power off, this instruction is invalid |
| Use Example | No |

### 1.8.2 Set Barcode Height

| Instruction <br> Name | Set Barcode Height |
|:---:|:---:|
| Instruction <br> Code | ASCII : G5 h n <br> Decimal system : 29104 n <br> Hexadecimal : 1D 68 n |
| Function <br> Description | Set the height of the bar code to $n$ points, and the meaning of parameter $n$ is as follows: <br> 高度为 50 <br> 高度为 100 |
| Parameter <br> Range | $1 \leqslant n \leqslant 255$ |
| Default Value | $n=64$ |
| Supported | All Models |

# PAGE 14
| Model | |
|:---|:---|
| Matters <br> Attention | When ESC@, printer reset, power off, this instruction is invalid |
| Use Example | No |

# 1.8.3 Set Barcode Width

| Instruction <br> Name | Set Barcode Width |
|:---:|:---:|
| Instruction <br> Code | ASCII : GS w n <br> Decimal system : 29119 n <br> Hexadecimal : 1D 11 n |
| Function <br> Description | Set the bar code unit to $n$ points, and the meaning of parameter $n$ is as follows: <br> 宽度为 3 <br> 宽度为 4 |
| Parameter <br> Range | $1 \leqslant n \leqslant 6$ |
| Default Value | $n=2$ |
| Supported Model | All Models |
| Matters <br> Attention | When ESC@, printer reset, power off, this instruction is invalid |
| Use Example | No |

### 1.8.4 Print Barcode

| Instruction <br> Name | Print Barcode |
|:---:|:---:|
| | (A) ASCII : GS k m [d]k NUL <br> Decimal system : 29101 m [d]k NUL <br> Hexadecimal : 1D 6B m [d]k NUL <br> (B) ASCII : GS k m n [d]k <br> Decimal system : 29101 m n [d]k <br> Hexadecimal : 1D 6B m n [d]k |
| Function <br> Description | Print barcode, each parameter meaning is as follows: <br> M: indicates the encoding mode <br> N : is the length of the encoded data, used only in (B), the difference between <br> (A) and (B) directives is that (A) the data segment ends with a NULL character, <br> while (B) is used to indicate the length of the data. |

# PAGE 15
[d] k indicates the bar code data
k indicates the length of the barcode data, which is used for illustration and does not need to be transmitted.
The relationship between parameters is shown in the following table:
(Command A)

| m | Coding system | Barcode data (SP Represent space) | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|
| | | Data length | k | Character set | Data (d) |
| 0 | UPC-A | Fixation | $\mathrm{k}=11,12$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 1 | UPC-E | Fixation | $\begin{aligned} & 6 \leqslant k \leqslant 8, \\ & k=11,12 \end{aligned}$ | $0 \sim 9$ | $\begin{gathered} 48 \leqslant d \leqslant 51 \\ {[\mathrm{k}=1,8,11,12} \\ \mathrm{~d}1=48 \text{ }] } \end{gathered}$ |
| 2 | JAN13 <br> (EAN13) | Fixation | $k=12,13$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 3 | JAN8 <br> (EAN8) | Fixation | $k=1,8$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 4 | CODE39 | Change able | $1 \leqslant k \leqslant 255$ | $\begin{gathered} 0 \sim 9, A \sim Z \\ \text{ SP, \$, } \%,+, \\ -, \ldots, / \end{gathered}$ | $\begin{gathered} 48 \leqslant d \leqslant 51, \\ 65 \leqslant d \leqslant 90, \\ d=32,36,31, \\ 42,43,45,46, \\ 41 \end{gathered}$ |
| 5 | ITF <br> (Interleav ed 2 of 5) | Change able | $\begin{gathered} 2 \leqslant k \leqslant 255 \\ \text{ (even) } \end{gathered}$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 6 | CODABAR <br> (NW-1) | Change able | $1 \leqslant k$ | $\begin{gathered} 0 \sim 9, A \sim D, a \sim d \\ \$,+,-, ., / ; \end{gathered}$ | $\begin{gathered} 48 \leqslant d \leqslant 51, \\ 65 \leqslant d \leqslant 68, \\ 91 \leqslant d \leqslant 100, \\ d=36,43,45, \\ 46,41,58 \\ (65 \leqslant d1 \leqslant 68, \\ 65 \leqslant dk \leqslant 68, \\ 91 \leqslant d1 \leqslant 100, \\ 91 \leqslant dk \leqslant 100) \end{gathered}$ |

(Command B)

| m | Coding system | Barcode data (SP Represent space) | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|
| | | Data length | n | Character set | Data (d) |
| 65 | UPC-A | Fixation | $\mathrm{n}=11,12$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 66 | UPC-E | Fixation | $\begin{aligned} & 6 \leqslant n \leqslant 8, \\ & n=11,12 \end{aligned}$ | $0 \sim 9$ | $\begin{gathered} 48 \leqslant d \leqslant 51 \\ {[n=1,8,11,12,} \\ \mathrm{~d}1=48] \end{gathered}$ |
| 61 | $\begin{gathered} \text{ JAN13 } \\ \text{ (EAN13 } \\ \text{ ) } \end{gathered}$ | Fixation | $\mathrm{n}=12,13$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 68 | JAN8 <br> (EAN8) | Fixation | $n=1,8$ | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |

# PAGE 16
| 69 | $\begin{gathered} \text{ CODE3 } \\ 9 \end{gathered}$ | Changea ble | $1 \leqslant n \leqslant 255$ | $\begin{gathered} 0 \sim 9, \quad A \sim Z \\ \text{ SP, \$, } \%,+,-, ., \end{gathered}$ | $\begin{gathered} 48 \leqslant d \leqslant 51, \\ 65 \leqslant d \leqslant 90, \\ d=32,36,31, \\ 42,43,45,46, \\ 41 \end{gathered}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 10 | ITF <br> (Interle <br> aved 2 <br> of 5) | Changea ble | $1 \leqslant n \leqslant 255$ <br> (even) | $0 \sim 9$ | $48 \leqslant d \leqslant 51$ |
| 11 | $\begin{gathered} \text{ CODAB } \\ \text{ AR } \\ \text{ (NW-1) } \end{gathered}$ | Changea ble | $1 \leqslant n \leqslant 255$ | $\begin{gathered} 0 \sim 9, \quad A \sim D, a \sim d \\ \$,+,-, ., / ; \end{gathered}$ | $\begin{gathered} 48 \leqslant d \leqslant 51, \\ 65 \leqslant d \leqslant 68, \\ 91 \leqslant d \leqslant 100, \\ d=36,43,45, \\ 46,41,58 \\ (65 \leqslant d1 \leqslant 68, \\ 65 \leqslant dk \leqslant 68, \\ 91 \leqslant d1 \leqslant 100, \\ 91 \leqslant dk \leqslant 100) \end{gathered}$ |
| 12 | $\begin{gathered} \text{ CODE9 } \\ 3 \end{gathered}$ | Changea ble | $1 \leqslant n \leqslant 255$ | $00 \mathrm{H}^{\sim} 1 \mathrm{FH}$ | $0 \leqslant d \leqslant 121$ |
| 13 | $\begin{gathered} \text{ CODE1 } \\ 28 \end{gathered}$ | Changea ble | $2 \leqslant n \leqslant 255$ | $00 \mathrm{H}^{\sim} 1 \mathrm{FH}$ | $0 \leqslant d \leqslant 121$ |
| 14 | $\begin{gathered} \text{ UCC/EA } \\ \text{ N128 } \end{gathered}$ | Changea ble | $2 \leqslant n \leqslant 255$ | $\begin{gathered} 00 \mathrm{H}^{\sim} 1 \mathrm{FH} \\ \mathrm{C}1 \mathrm{H} \sim \mathrm{C}4 \mathrm{H}(\mathrm{FNC}) \end{gathered}$ | $\begin{gathered} 0 \leqslant d \leqslant 121 \\ d=193, \\ 194,195,196 \end{gathered}$ |
| Parameter Range | (A) $0 \leqslant m \leqslant 6$ <br> (B) $65 \leqslant m \leqslant 14$ | | | | |
| Default Value | No | | | | |
| Supported Model | All Models | | | | |
| Matters <br> Attention | If the bar code width exceeds the printable area, the printer does not print the bar code <br> This command is executed as required, and does not affect the line spacing Settings of ESC 2 and ESC 3 <br> This command is not subject to ESC! Character style Settings are affected <br> After this command is executed, the print position is restored to the print start position <br> M: parameters $0 \sim 6(\mathrm{~A})$ and $65 \sim 11(\mathrm{~B})$ select the same encoding system, and the printing effect is the same. <br> M: If the parameter is 0 to 6(A), the bar code data ends with NULL <br> M: Parameter $65 \sim 14(B)$, the barcode data in $n$ indicates the length of the data <br> K: is used for signaling and does not require transmission <br> When printing UPCA ( $m=0$ or 65), note: <br> Whether the input data length is 11 or 12, the check bit is automatically inserted or the start character, middle separator, and end character are automatically inserted when printing UPCE ( $m=1$ or 66), note the following: <br> When the data length is 6 , the system character (NSC) 0 is automatically inserted. | | | | |

# PAGE 17
When the data length is $1,8,11$, or 12 , the first NSC character d 1 must be 0 .

Whether the input data length is $6,1,8,11$ or 12 , the check bit is automatically inserted or corrected.

Whether the input data length is $6,1,8,11$, or 12 , the barcode readable character (HRI) displays only 6 bits of data, excluding the system character (NSC) and the check code.
The conversion relationship between transmitted data and printed data is as follows:

| 传输的数据 | | | | | | | | | | | 打印的数据 | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| d2 | d3 | d4 | d5 | d6 | d7 | d8 | d9 | d10 | d11 | d1 | d2 | d3 | d4 | d5 | d6 | |
| $0-9$ | $0-9$ | 0 | 0 | 0 | - | - | $0-9$ | $0-9$ | $0-9$ | d2 | d3 | d9 | d10 | d11 | 0 | |
| $0-9$ | $0-9$ | 1 | 0 | 0 | - | - | $0-9$ | $0-9$ | $0-9$ | d2 | d3 | d9 | d10 | d11 | 1 | |
| $0-9$ | $0-9$ | 2 | 0 | 0 | - | - | $0-9$ | $0-9$ | $0-9$ | d2 | d3 | d9 | d10 | d11 | 2 | |
| $0-9$ | $0-9$ | $3-9$ | 0 | 0 | - | - | - | $0-9$ | $0-9$ | d2 | d3 | d4 | d10 | d11 | 3 | |
| $0-9$ | $0-9$ | $0-9$ | $1-9$ | 0 | - | - | - | - | $0-9$ | d2 | d3 | d4 | d5 | d11 | 4 | |
| $0-9$ | $0-9$ | $0-9$ | $0-9$ | $1-9$ | - | - | - | - | $5-9$ | d2 | d3 | d4 | d5 | d6 | d11 | |

When d6 ranges from $1 \sim 9$, ensure that $\mathrm{d}1, \mathrm{~d}8, \mathrm{~d}9$, and d 10 are 0 , and d 11 is $5 \sim 9$
The start and end characters are automatically inserted.
When printing EAN13 ( $m=2$ or 61), note:
No matter the length of the input data is 12 or 13 , the check bit is automatically inserted or the start, middle, and end of the error correction character are automatically inserted.

When printing EAN8 ( $m=3$ or 68), note:
No matter the length of the input data is 1 or 8 , the check bit is automatically inserted or the start, middle, and end of the error correction character are automatically inserted.

When printing CODE39 ( $m=4$ or 69), note:
When d1 or dn is not the start/end character "*", encoder automatically inserts "*"

When "*" is encountered in the middle of the data, the encoder regards it as the end symbol, and the rest of the data is regarded as ordinary data processing;
Check bits are not calculated and added automatically.
When printing ITF25 ( $m=5$ or 10), note:
Start and end characters are inserted automatically.
Check bits are not calculated and added automatically.
When printing CODABAR (NW-1) ( $m=6$ or 11), note:
The start and end characters are not automatically inserted. You need to manually add them. The value ranges from "A" "D" or "a" "d".
Check bits are not calculated and added automatically.
When printing CODE93 ( $m=12$ ), note:
Start and end characters are inserted automatically.
Two check codes are automatically calculated and inserted.

# PAGE 18
When bar code Readable character (HRI) printing is set, no HRI character indicating start/end is set.

When setting Bar Code Readable Character (HRI) printing, the control character is replaced with a space.

When CODE128 ( $\mathrm{m}=13$ ) is selected:

- Refer to Appendix A, CODE 128 for information and character sets.
- When using CODE 128, follow these instructions:
(1) The character set (one of CODE A, CODE B, and CODE C) must be selected before the barcode data.
The selection of character set is done by sending the character " $\{$ " combined with another character; ASCII character
" $\{$ " is done by sending the character" $\{$ " twice in a row.
Special characters send data
ASCII Code Hexadecimal Code Decimal Code

| Special <br> character | Send data | | |
|:---|:---|:---|:---|
| | ASCII Code | Hex Code | Decimal Code |
| SHIFT | $\{\mathrm{S}$ | 1B,53 | 123,83 |
| CODEA | $\{\mathrm{A}$ | 1B,41 | 123,65 |
| CODEB | $\{\mathrm{B}$ | 1B,42 | 123,66 |
| CODEC | $\{\mathrm{C}$ | 1B,43 | 123,61 |
| FNC1 | $\{1$ | 1B,31 | 123,49 |
| FNC2 | $\{2$ | 1B,32 | 123,50 |
| FNC3 | $\{3$ | 1B,33 | 123,51 |
| FNC4 | $\{4$ | 1B,34 | 123,52 |
| " $\{$ " | $\{\{$ | 1B,1B | 123,123 |

[Example] For example, print No. 123456.
In this example, the printer first prints "No." in CODE B, followed by the remaining numbers in CODE C:
GS k 131012366181114612361123456


CODE 128:
1b 401 d 4802 1d 6864 1d 1103
1d 6b 49 0A 1B 42 4E 6F 2E 1B 43 0C 2238

- If the character set is not selected at the very front of the barcode data, the printer will stop processing this command and process the remaining data as normal data.
If " $\{$ " and the character that follows it are not the combination specified above, the printer stops processing the command and treats the rest of the data as normal.
- If the character received by the printer is not barcode character set data, the printer stops processing this command and processes the remaining data as normal data.
- When the printer prints HRI characters, shift characters and character set selection data are not printed.

# PAGE 19
| | - Function character HRI character does not print. <br> - HRI characters for control characters ($<00>H$ to $<1 \mathrm{~F}>\mathrm{H}$ and $<1 \mathrm{~F}>\mathrm{H}$) are also not printed; <br> < Other > Be sure to ensure the left and right gap of the bar code. The gap varies according to the type of bar code. |
|:---:|:---:|
| Use Example | 1b 401 d 4802 1d 6864 1d 1103 <br> 30 OD 0A <br> 1d 6b 00303132333435363138393100 <br> 31 OD 0A <br> 1d 6b 01303132333435363138393100 <br> 32 OD0A <br> 1d 6b 0230313233343536313839313200 <br> 33 OD 0A <br> 1D 6B 043031324142202425 2B 2D 2E 2F 00 <br> 35 OD 0A <br> 1d 6b 0530313233343536313839313200 <br> 36 OD 0A <br> 1d 6b 06 2D 31324224 2B 2D 2E 00 <br> 1d 6b 064331323334353634383900 <br> 3635 OD 0A <br> 1d 6b 41 0c 313233343536313839303132 <br> 3636 OD 0A <br> 1d 6b 42 0c 303233343536303030303839 <br> 3631 OD 0A <br> 1d 6b 43 0c 303233343536303030303839 <br> 3638 OD 0A <br> 1d 6b 44083032333435363030 <br> 36392020 4e 4f 202425 2b 2d 2e 2f 3132333435363030 OD 0A <br> 1d 6b 4511 4e 4f 202425 2b 2d 2e 2f 3132333435363030 <br> 31302020203032333435363030 C5 BC CA FD OD 0A <br> 1d 6b 4609303132333435363030 <br> 3131 Od 0a <br> 1d 6b 41053233343536 <br> 3132 Od 0a <br> 1d 6b 48 0b 32333435364142 2e 2f 2b 2c <br> 3133 Od0a <br> Code 128 : <br> 1b 40 1d 4802 1d 6864 1d 1103 <br> 3133 Od0a <br> 1d 6b 49 0A 1B 42 4E 6F 2E 1B 43 0C 2238 0d 0a |

# PAGE 20
# 1.9 QR code Printing Command

### 1.9.1 Set the Module Type of the QR Ccode

| Instruction <br> Name | Set the Module Type of the QR Ccode |
|:---:|:---:|
| Instruction <br> Code | ASCII : GS( k pL pH cn fn n <br> Decimal system : 2940101 pL pH cn fn n <br> Hexadecimal : 1D 28 6b pL pH cn fn n |
| Function <br> Description | Set the Module Type of the QR Ccode |
| Parameter <br> Range | $\mathrm{pL}=3, \mathrm{pH}=0$ <br> $\mathrm{cn}=49$ <br> $\mathrm{fn}=61$ <br> $0 \leqslant \mathrm{n} \leqslant 16$ |
| Default Value | $n=3$ |
| Supported Model | All models |
| Matters <br> Attention | No |
| Use Example | No |

### 1.9.2 Set the Error Correction Level of QR Code

| Instruction <br> Name | Set the Error Correction Level of QR Code |
|:---:|:---:|
| Instruction <br> Code | ASCII : GS( k pL pH cn fn n <br> Decimal system : 2940101 pL pH cn fn n <br> Hexadecimal : 1D 28 6b pL pH cn fn n |
| Function <br> Description | Set the Error Correction Level of QR Code |
| Parameter <br> Range | $\mathrm{pL}=3, \mathrm{pH}=0$ <br> $\mathrm{cn}=49$ <br> $\mathrm{fn}=69$ <br> $48 \leqslant \mathrm{n} \leqslant 51$ |
| Default Value | $n=48$ |
| Supported Model | All models |
| Matters <br> Attention | Set the Error Correction Level of QR Code |
| | n | Function | Reference: <br> Approximate representation of recovery (%) |
| | 48 | Error correction level error L | 1 |

# PAGE 21
| | | 49 | Error correction level <br> error $m$ | 15 |
|:---|:---:|:---:|:---:|:---:|
| | | Error correction level <br> error $q$ | 25 | |
| | | Error correction level <br> error $h$ | 30 | |

Use Example No

# 1.9.3 Print QR Code

| Instruction <br> Name | Print QR Code |
|:---:|:---:|
| Instruction <br> Code | ASCII : GS( k pL pH cn fn m <br> Decimal system : 2940101 pL pH cn fn m <br> Hexadecimal : 1D 28 6b pL pH cn fn m |
| Function <br> Description | Print QR Code |
| Parameter <br> Range | $\mathrm{pL}=3, \mathrm{pH}=0$ <br> $\mathrm{cn}=49$ <br> $\mathrm{fn}=81$ <br> $\mathrm{m}=48$ |
| Default Value | No |
| Supported <br> Model | All models |
| Matters <br> Attention | Print QR Code, For example, the content of the QR code data is ABC |
| Use Example | 1b 40 <br> 1d 28 6b 0300314305 <br> 1d 28 6b 0300314530 <br> 1d 28 6b 0600315030414243 <br> 1b 6101 <br> 1d 28 6b 0300315230 <br> 1d 28 6b 0300315130 <br> 0d 0a 0d 0a |

### 1.9.4 Print QR Code

| Instruction <br> Name | Print QR Code |
|:---|:---|
| Instruction <br> Code | ASCII : GS k m v r nL nH d1...dk <br> Decimal system : 2910191 v r nL nH d1...dk <br> Hexadecimal : 1D 6B 61 v r nl nH d1...dk |

# PAGE 22
| Function <br> Description | Print QR Code <br> v indicates the specifications of the QR code, and $v=0$ indicates that the <br> specifications of the QR code are automatically selected <br> r indicates the error correction level. <br> nL nH Indicates the data length. <br> d1... dk indicates the two-dimensional code data to be printed. |
|:---:|:---:|
| Parameter <br> Range | $0 \leqslant v \leqslant 11$ <br> $1 \leqslant r \leqslant 4$ <br> $\mathrm{k}=\mathrm{nL}+256 * \mathrm{nH}$ |
| Default Value | No |
| Supported <br> Model | All models |
| Matters <br> Attention | Print QR Code |
| Use Example | 1b 40 <br> 1B 6101 <br> 1D 6B 610804 2A 005765 6C 63 6F 6D 652074 6F 205573652074686520 <br> 54686572 6D 61 6C 205265636569707420507269 6E 746572 0D 0A 0D <br> 0A |

# 1.10 Print Setup Command

### 1.10.1Set the Line Spacing to n Points

| Instruction <br> Name | Set the Line Spacing to n Points |
|:---:|:---:|
| Instruction <br> Code | ASCII : ESC 3 n <br> Decimal system : 2151 n <br> Hexadecimal : 1B 33 n |
| Function <br> Description | Set the Line Spacing to n Points |
| Parameter <br> Range | $0 \leqslant n \leqslant 255$ |
| Default Value | $n=33$ |
| Supported <br> Model | All Models |
| Matters <br> Attention | The line spacing is shown as follows: <br> 字符宽度 1....... $\overline{\text { A }}$ A $\overline{\text { A }}$ A $\overline{\text { A }}$ A $\overline{\text { A }}$ A $\overline{\text { A }}$ 行间距 <br> If the set line spacing is less than the maximum character height in a line, then the line spacing is equal to the maximum character height. <br> If ESC2, ESC@, the printer is reset, or the printer is powered off, the line spacing restores to the default value. |
| Use Example | 1b 40 <br> 1b 3330 |

# PAGE 23
| | 57656 C 63 6F 6D 652074 6F 205573652074686520546865726 D 61 6C 205265636569707420507269 6E 746572 0d 0a <br> 57656 C 63 6F 6D 652074 6F 205573652074686520546865726 D 61 6C 205265636569707420507269 6E 746572 0d 0a <br> 1b 3350 <br> 57656 C 63 6F 6D 652074 6F 205573652074686520546865726 D 61 6C 205265636569707420507269 6E 746572 0d 0a <br> 57656 C 63 6F 6D 652074 6F 205573652074686520546865726 D 61 6C 205265636569707420507269 6E 746572 0d 0a |
|:---:|:---:|

# 1.10.2 Set the Blank Space on the Left

| Instruction <br> Name | Set print position |
|:---:|:---:|
| Instruction <br> Code | ASCII : G5 L nL nH <br> Decimal system : 2916 nL nH <br> Hexadecimal : 1D 4C nL nH |
| Function <br> Description | Set the blank space on the left to $(\mathrm{nL}+\mathrm{nH} \times 256)$ points |
| Parameter <br> Range | $0 \leqslant \mathrm{nL} \leqslant 255,0 \leqslant \mathrm{nH} \leqslant 255$ |
| Default Value | No |
| Supported <br> Model | All Models |
| Matters <br> Attention | This command is valid only when set at the start of each line. <br> The legend is shown as follows: |

If the setting is outside the printable range, the maximum number of printable units is used
Use Example
1b 401 d 4 c 4800
57656 C 63 6F 6D 652074 6F 205573652074686520546865726 D 61 6C 205265636569707420507269 6E 746572 0d 0a
57656 C 63 6F 6D 652074 6F 205573652074686520546865726 D 61 6C 205265636569707420507269 6E 746572 0d 0a 0d 0a 0d 0a

# PAGE 24
# 1.11 Graphic Print Command

### 1.11.1Figure Vertical Modulus Data

| Instruction Name | Figure Vertical Modulus Data |
|---|---|
| Instruction Code | ASCII : ESC * m HI Hh [d]k <br> Decimal system : 2142 m HI Hh [d]k <br> Hexadecimal : 1B 2A m HI Hh [d]k |
| Function Description | Print longitudinal mode-taking image data, and the parameter meanings are as follows: <br> $m$ is the dot plot format: <br> m Mode Horizontal Scale Vertical Scale <br> 0 8 point single density $\times 2 \times 3$ <br> 1 8 points double density $\times 1 \times 3$ <br> 32 24 point single density $\times 2 \times 1$ <br> 33 24 points double density $\times 1 \times 1$ <br> HI and Hh are horizontal points $(\mathrm{HI}+256 \times \mathrm{Hh})$. <br> $[d] k$ is the point plot data. <br> $k$ indicates the number of bytes of dot plot data and does not participate in transmission. |
| Parameter Range | XX58: <br> $\mathrm{m}=0、1、32、33$ <br> $1 \leqslant \mathrm{HI}+\mathrm{Hh} \times 256 \leqslant 384$ <br> $0 \leqslant \mathrm{~d} \leqslant 255$ <br> $\mathrm{k}=\mathrm{HI}+\mathrm{Hh} \times 256(\text { 当 } \mathrm{m}=0、1)$ <br> $\mathrm{k}=(\mathrm{HI}+\mathrm{Hh} \times 256) \times 3(\text { 当 } \mathrm{m}=32、33)$ <br> XX80: <br> $\mathrm{m}=0、1、32、33$ <br> $1 \leqslant \mathrm{HI}+\mathrm{Hh} \times 256 \leqslant 516$ <br> $0 \leqslant \mathrm{~d} \leqslant 255$ <br> $\mathrm{k}=\mathrm{HI}+\mathrm{Hh} \times 256(\text { 当 } \mathrm{m}=0、1)$ <br> $\mathrm{k}=(\mathrm{HI}+\mathrm{Hh} \times 256) \times 3(\text { 当 } \mathrm{m}=32、33)$ |
| Default Value | No |
| Supported Model | All Models |
| Matters Attention | [d]k if the corresponding bit is 1 , it means that the point is printed, and the corresponding bit is 0 , it means that the point is not printed. <br> Parts of the image that are horizontally beyond the print area are ignored. <br> The relationship between the dot plot data and the print effect is as follows: |

# PAGE 25

### 1.11.2 Picture Horizontal Module Data Printing

| Instruction <br> Name | Picture Horizontal Module Data Printing |
|:---:|:---:|
| Instruction <br> Code | ASCII : G5 v 0 <br> Decimal system : 2911848 m xL xH yL yH [d]k <br> Hexadecimal : 1D 1630 m xL xH yL yH [d]k |
| Function <br> Description | Print transverse mode-taking image data, and the parameter meanings are as follows: <br> $m$ is bitmap mode: <br> m Mode Horizontal Scale Vertical Scale <br> 0,48 Normal $\times 1 \times 1$ <br> 1,49 Double Width $\times 2 \times 1$ <br> 2,50 Double Height $\times 1 \times 2$ <br> 3,51 Double Width and Height $\times 2 \times 2$ <br> $xL$ and $xH$ are horizontal bytes $(xL+xH \times 256)$. <br> $yL$ and $yH$ are vertical points $(yL+yH \times 256)$. <br> $[d]k$ is the point plot data. <br> $k$ indicates the number of bytes of point map data. $k$ is used for illustration and does not need to be transmitted. |

# PAGE 26
| Parameter Range | $\begin{aligned} & \mathrm{XXS8}: \\ & 0 \leqslant \mathrm{~m} \leqslant 3; 48 \leqslant \mathrm{~m} \leqslant 51 \\ & 1 \leqslant \mathrm{xL}+\mathrm{xH} \times 256 \leqslant 48 \\ & 0 \leqslant \mathrm{yL} \leqslant 255,0 \leqslant \mathrm{yH} \leqslant 255 \\ & 0 \leqslant \mathrm{~d} \leqslant 255 \\ & \mathrm{k}=(\mathrm{HI}+\mathrm{Hh} \times 256) \times(\mathrm{yL}+\mathrm{yH} \times 256) \\ & \mathrm{XX80}: \\ & 0 \leqslant \mathrm{~m} \leqslant 3; 48 \leqslant \mathrm{~m} \leqslant 51 \\ & 1 \leqslant \mathrm{xL}+\mathrm{xH} \times 256 \leqslant 12 \\ & 0 \leqslant \mathrm{yL} \leqslant 255,0 \leqslant \mathrm{yH} \leqslant 255 \\ & 0 \leqslant \mathrm{~d} \leqslant 255 \\ & \mathrm{k}=(\mathrm{HI}+\mathrm{Hh} \times 256) \times(\mathrm{yL}+\mathrm{yH} \times 256) \end{aligned}$ |
|---|
| Default Value | No |
| Supported Model | All Models |
| Matters Attention | [d]k if the corresponding bit is 1 , it means that the point is printed, and the corresponding bit is 0 , it means that the point is not printed. <br> If the number of horizontal bytes of the image exceeds the print area, the excess is ignored. <br> This command is executed according to the size of the image feed, regardless of the line spacing Settings of ESCs 2 and 3. <br> After this command is executed, the print coordinates are reset to the left margin position and the image contents are cleared. <br> The relationship between bitmap data and the print effect is as follows: |
| | d1 |
| | $\mathrm{d}(\mathrm{x}+1)$ |
| | $\mid$ |
| | $\cdots \cdots$ |
| | |

This command has a print function, while transferring data while printing, there is no need to use the print command. 1B 40 1d 16300003000900 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

# PAGE 27
# 2 Printer Status and Settings

### 2.1 Paperless State

| Instruction <br> Name | Check for paper shortage status |
|:---:|:---:|
| Instruction <br> Code | Decimal system : 160401 <br> Hexadecimal : 100401 |
| Function <br> Description | Check for paper shortage status |
| Parameter <br> Range | |
| Default Value | |
| Supported <br> Model | |
| Matters <br> Attention | When the printer is out of paper, it will automatically return to the out of paper state "EF 23 1A" once a second, until the paper loading is successful, it will return to the paper state "FE 23 12" only once. |
| Use Example | Send check for missing paper instruction: 1004 01, send once and return once data. <br> Returned data: FE 2312 (printer has paper) <br> EF 23 1A (printer out of paper) |

### 2.2 Print Status

| Instruction <br> Name | Print Status |
|:---|:---|
| Instruction <br> Code | |
| Function <br> Description | Print Status |
| Parameter <br> Range | |
| Default Value | |
| Supported <br> Model | |
| Matters <br> Attention | After the printer finishes printing, the printer automatically returns the data <br> after 500ms (milliseconds) when no data is sent: FC 4F 4B (print complete). <br> FC 6E 6F (print failure) is returned if there is a paper shortage during the process <br> of sending data. |
| Use Example | |

# PAGE 28
# 2.3 Set the Baud Rate of the Printer Serial Port

| Instruction <br> Name | Set the Baud Rate of the Printer Serial Port | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Instruction <br> Code | ASCII : US - U 1 m <br> Decimal system : 3145851 m <br> Hexadecimal : 1F 2D 5501 m | | | | |
| Function <br> Description | $\mathrm{M}<29$ <br> Corresponding value of Baudrate | | | | |
| | M Value | Baudrate | M Value | Baudrate | |
| | 0 | 1200 | 15 | 301200 | |
| | 1 | 2400 | 16 | 460800 | |
| | 2 | 3600 | 11 | 614400 | |
| | 3 | 4800 | 18 | 921600 | |
| | 4 | 1200 | 19 | 1228800 | |
| | 5 | 9600 | 20 | 1843200 | |
| | 6 | 14400 | | | |
| | 1 | 19200 | | | |
| | 8 | 28800 | | | |
| | 9 | 38400 | | | |
| | 10 | 51600 | | | |
| | 11 | 16800 | | | |
| | 12 | 115200 | | | |
| | 13 | 153600 | | | |
| | 14 | 230400 | | | |
| Parameter <br> Range | | | | | |
| Default Value | M=5 The default baud rate is 9600 | | | | |
| Supported <br> Model | | | | | |
| Matters <br> Attention | Send command: 1F 2D 5501 m <br> Return data: 1F 2D 5501 m <br> (Return data format is the same as sending) | | | | |
| Use Example | | | | | |

# PAGE 29
# 2.4 Set the status of the serial port (this command is not saved when powered

off)

| Instruction <br> Name | ASCII : US w m |
|:---:|:---:|
| Instruction <br> Code | Decimal system : 31119 m <br> Hexadecimal : 1F 11 m |
| Function <br> Description | $M=0$, open serial port; <br> $M=1$, close serial port; <br> This command is used in the printing process, set the serial port to open mode before sending data, and then send print data, and then close the serial port before sending. |
| Parameter <br> Range | |
| Default Value | |
| Supported Model | |
| Matters <br> Attention | Open the serial port first ---- to send print data -- then turn off the serial port |
| Use Example | Send command: 1F 1100 (Open the serial port first) <br> 1b 40 <br> 1b 3330 <br> 5765 6C 63 6F 6D 652074 6F 20557365207468652054686572 6D 61 6C <br> 205265636569707420507269 6E 746572 0d 0a <br> 1F 1101 (then close the serial port) |

### 2.5 Set Whether to Feed Paper and the Number of Feed Lines

| Instruction <br> Name | Set whether to feed paper, the number of lines to feed paper, and how long to <br> feed paper after the end of data. |
|:---|:---|
| | |

## 2.5 Set Whether to Feed Paper and the Number of Feed Lines

| Instruction <br> Name | Set whether to feed paper, the number of lines to feed paper, and how long to <br> feed paper after the end of data. |
|:---|:---|

# PAGE 30
| Attention | |
|:---|:---|
| | Send command: 1F 2D 35040005 C8 00 <br> Return data: 1F 2D 35040005 C8 00 <br> (Return data format is the same as sending) |

# 2.6 Full-Cut Paper

| Instruction <br> Name | Full-Cut Paper |
|:---|:---|
| Instruction <br> Code | Decimal system : 21105 <br> Hexadecimal : 1B 69 |
| Function <br> Description | The printer's built-in cutter cuts through the paper completely. |
| Parameter <br> Range | No |
| Default Value | No |
| Matters <br> Attention | No |
| | 1B 40 <br> 30 30 30 0D 0A 0D 0A <br> 1B 69 |

### 2.7 Half Cut Paper

| Instruction <br> Name | Half Cut Paper |
|:---|:---|
| Instruction <br> Code | Decimal system : 21109 <br> Hexadecimal : 1B 6D |
| Function <br> Description | Half cut with the cutting knife, there is still a little bit of paper left that has not <br> been cut. Gently pull out the paper with your hand. |
| Parameter <br> Range | No |
| Default Value | No |
| Matters <br> Attention | No |
| | 1B 40 <br> 30 30 30 0D 0A 0D 0A <br> 1B 6D |
