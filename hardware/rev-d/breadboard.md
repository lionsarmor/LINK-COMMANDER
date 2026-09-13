# Rev D breadboard and custom PS/2 cables

Use this guide with the **Rev D** schematic and wiring CSV. Component
numbers and the sense polarity differ from Rev C. Begin with a keyboard
receiver on USB input 1; add the mouse after the keyboard tests pass.

## Parts for the first keyboard build

Populate M1, J1, F1, JP1, C1-C6, U1, U2, J2, D1, R1-R5, Q1/Q2,
R11-R18, and the keyboard output J4. Leave the mouse port and mouse output
parts out initially. Tie the unused U2 inputs 7, 9, 11 and 14 to ground in
this keyboard-only breadboard. Leave outputs 6, 10, 12 and 15 open. When
adding the mouse, remove the temporary grounds from U2 pins 7 and 9 and
connect them to MOUSE_DATA and MOUSE_CLOCK instead.

The RP2040-Zero needs two 1×9 side headers and one 1×5 end header. Its end
row does not share the same grid alignment as the side rows on a normal
breadboard; use short leads for the end contacts. Use the printed GP labels.
Do not solder wires to underside GPIO pads.

USB and DIN sockets may need short soldered leads or your existing connector
breakouts during breadboarding. The finished PCB takes the sockets directly.
Keep USB data leads short and paired, with the 22 Ω resistors beside the
module. Do not carry the combined receiver load through long breadboard rails.

## Test access

The finished PCB provides TP1–TP26. On the breadboard, clip to the same
named nets; the test holes themselves do not need separate components.
Use the [test-point guide](test-points.md) for the power checks, PS/2
drive/sense comparisons, voltage domains and USB resistor probe pads.
The external supply and JP1 procedure are unchanged.

## Module wiring

| Module GPIO | M1 carrier pin | Connection |
|---|---:|---|
| GP0 | 1 | R1.1 → 22 Ω → keyboard USB D+ |
| GP1 | 2 | R2.1 → 22 Ω → keyboard USB D− |
| GP2 | 3 | R6.1 → 22 Ω → mouse USB D+ |
| GP3 | 4 | R7.1 → 22 Ω → mouse USB D− |
| GP8 | 9 | R11.1 → keyboard DATA transistor base |
| GP9 | 10 | U2.2 → keyboard DATA sense |
| GP10 | 11 | R15.1 → keyboard CLOCK transistor base |
| GP11 | 12 | U2.4 → keyboard CLOCK sense |
| GP12 | 13 | R19.1 → mouse DATA transistor base |
| GP13 | 14 | U2.6 → mouse DATA sense |
| GP14 | 15 | R23.1 → mouse CLOCK transistor base |
| GP15 | 16 | U2.10 → mouse CLOCK sense |
| 3V3 | 21 | U2.1, C2.1, C3.1 |
| GND | 22 | Common ground |
| 5V | 23 | JP1.2, net 5V_MODULE |

GP4-GP7 and GP26-GP29 are unused. GP16 remains the module's onboard LED.
Drive HIGH asserts LOW. Sense HIGH means the cable is HIGH.

## Power and chip connections

J1.1 goes to F1.1. F1.2 supplies 5V_BOARD; J1.2 is GND. C1's positive
lead goes to 5V_BOARD. JP1.1 is 5V_BOARD; JP1.2 is 5V_MODULE.
Use a regulated 5 V / 2 A supply and a 1.5 A fast 5×20 fuse. Verify
4.75-5.25 V at each USB socket under the intended load; supply and wiring
losses matter. Do not exceed 5.25 V at J1.

U1 is a **TPS2042P dual power switch**. Pin 2 is 5V_BOARD; pins 1, 3 and
4 are GND. Pin 7 supplies keyboard USB VBUS, and pin 6 supplies mouse USB
VBUS. Pin 8 is the keyboard fault output; pin 5 is the mouse fault output.
Each red LED's cathode goes to its fault output; its anode is fed from
5V_BOARD through 2.2 kΩ. A TPS2041P has a different pinout and must not be
substituted. TPS2052 has the opposite enable polarity.

U2: pin 1 is 3V3; pin 8 is GND. Do not use the usual “pin 16 is power”
assumption: **U2 pins 13 and 16 are no-connects**. In the complete design,
pins 11/14 are grounded and outputs 12/15 stay open.

Place each 100 nF capacitor near the corresponding IC or USB supply pins.
Electrolytic pin 1 is positive. DIP numbering is viewed from above, notch
at the top: pin 1 is upper left, then count down the left and up the right.
For the selected 2N3904, verify manufacturer pins **1=E, 2=B, 3=C**.

## PS/2 signal circuits

| Line | Base resistor | Base pulldown | Target pullup | Line pulldown | Transistor | U2 input → output |
|---|---|---|---|---|---|---|
| Keyboard DATA | R11 2.2 kΩ | R12 47 kΩ | R13 4.7 kΩ | R14 100 kΩ | Q1 | 3 → 2 |
| Keyboard CLOCK | R15 2.2 kΩ | R16 47 kΩ | R17 4.7 kΩ | R18 100 kΩ | Q2 | 5 → 4 |
| Mouse DATA | R19 2.2 kΩ | R20 47 kΩ | R21 4.7 kΩ | R22 100 kΩ | Q3 | 7 → 6 |
| Mouse CLOCK | R23 2.2 kΩ | R24 47 kΩ | R25 4.7 kΩ | R26 100 kΩ | Q4 | 9 → 10 |

Each emitter goes to GND. Its collector goes directly to the named cable
line. The 2.2 kΩ resistor connects the drive GPIO to its base; 47 kΩ connects
base to ground. The 4.7 kΩ resistor connects that line to the corresponding
X16-side 5 V reference. The 100 kΩ resistor connects the line to ground.

For every physical connection, use [breadboard-wiring.csv](breadboard-wiring.csv)
or [net-connections.csv](net-connections.csv). Do not infer connections from
where components happen to sit on a breadboard or on the PCB.

## Custom cables: same assignment for J4 and J5

J4 connects only to the X16 keyboard port; J5 connects only to its mouse port.
Use a 7-pin DIN male plug on the adapter end and a 6-pin mini-DIN PS/2 male
plug on the X16 end. Numbers below refer to the actual numbered contacts,
not left-to-right positions or wire colors.

| Adapter 7-pin DIN contact | PS/2 plug contact | Signal |
|---:|---:|---|
| 1 | 4 | X16 +5 V reference |
| 2 | 3 | Ground |
| 3 | 1 | DATA |
| 4 | 5 | CLOCK |
| 5, 6, 7 | None | Leave unconnected |
| Shell / local PCB pad 8 | None | Leave unconnected |

PS/2 contacts 2 and 6 remain unconnected. The two physical shell terminals
on the DIN footprint share local pad number 8; neither is a signal contact.
Front and solder-side views are mirrored. Confirm numbering against the
connector drawing and then continuity-test every wire before use. The
[X16 hardware reference](https://github.com/X16Community/x16-docs/blob/master/X16%20Reference%20-%2014%20-%20Hardware.md)
provides the target PS/2 pin assignment.

## Bring-up sequence

1. Leave the X16 and USB receivers disconnected. Check supply continuity,
   capacitor polarity, DIP orientation and transistor pinouts without power.
2. Apply external 5 V with a current-limited bench supply. Confirm 3V3 at
   U2.1 and receiver VBUS on J2.1/J3.1. Both USB ports are always enabled.
3. For PC programming, remove JP1 first. With JP1 removed, the PC powers
   the module and U2 while external 5 V powers the receiver sockets.
   For standalone use, disconnect PC USB and refit JP1 with power off.
4. With the X16 absent, a temporary regulated 5 V reference can supply
   KBD_5V/MOUSE_5V on the test fixture. Use GPIO test firmware to verify all
   four drive/sense paths. Remove those temporary reference jumpers before
   connecting any X16 cable. Measure rise time and check that sense inputs
   stay in the 3.3 V domain.
5. Test USB enumeration and reports, then PS/2 reset, acknowledgments,
   keyboard scan-code behavior and mouse packets on a suitable host fixture.
   The firmware requirements are in [firmware-contract.md](firmware-contract.md).
6. Only after these checks pass, power off, attach the checked custom cables,
   and begin an X16 keyboard test. Add mouse operation and simultaneous use
   afterward. Record receiver models and results.

These are required tests, not completed test results. This repository does
not yet include a tested bridge or GPIO test application.
