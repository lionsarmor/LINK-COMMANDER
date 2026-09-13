# Understanding LINK COMMANDER Rev D

A modern USB keyboard and an older PS/2 keyboard speak different protocols.
LINK COMMANDER listens to USB and sends the PS/2 messages the X16 expects.
It performs the same translation for a mouse.

For wireless devices, the little USB receiver handles the radio link.
LINK COMMANDER reads USB reports from that receiver; it does not contain
a 2.4 GHz radio. A receiver still needs to use a USB interface supported
by the firmware.

## The two chips

| Reference | Part | Job |
|---|---|---|
| U1 | TPS2042P, DIP-8 | Two protected power channels: one for each USB port. |
| U2 | CD4050BE, DIP-16 | Converts four incoming PS/2 signal levels for the RP2040's 3.3 V inputs. |
| M1 | RP2040-Zero module | Runs the USB host and PS/2 translation program. It plugs into headers. |

U2A, U2B, U2C and U2D on the schematic are four circuits **inside the same
U2 chip**. U2E and U2F are its two unused circuits. U2G shows its supply
pins. You buy one CD4050BE, not seven chips.

U1 contains two separate power switches. A short on either USB port can
assert that port's red fault LED; these are not activity lights. Both
active-low enable pins go to ground, so both ports have power whenever
the external supply is present. Combining the switches in one DIP package
saves a chip and its separate input bypass capacitor. See the
[TI TPS2042 datasheet](https://www.ti.com/lit/gpn/TPS2042).

The CD4050 is specifically a level-converting, non-inverting buffer; do not
substitute an ordinary 74HC buffer. Its input-high voltage can exceed its
supply voltage. This lets the design power U2 from 3.3 V while sensing the
PS/2 lines. See the [TI CD4050 datasheet](https://www.ti.com/lit/ds/symlink/cd4050b.pdf).

## Why there are four transistors

A PS/2 cable has two signal wires: DATA and CLOCK. Either end may need to
pull a line LOW. The adapter must also let go so the other end can speak.
This is why simply sending characters on an ordinary serial output is
not enough.

Each 2N3904 transistor works as a switch to ground:

1. The RP2040 raises a drive GPIO. Current passes through a 2.2 kΩ resistor
   into the transistor's base. The transistor pulls its cable line LOW.
2. The RP2040 lowers the drive GPIO. The transistor turns off. A 4.7 kΩ
   pullup resistor lets the cable line rise, unless the X16 is holding it LOW.
3. U2 reads the cable level and presents it to a separate RP2040 input.

Q1/Q2 serve keyboard DATA/CLOCK. Q3/Q4 serve mouse DATA/CLOCK.
The 47 kΩ base resistors hold the switches off while the module starts.
The 100 kΩ line resistors provide a weak path to ground when the target
reference supply is absent. They are much weaker than the 4.7 kΩ pullups.

| Drive GPIO | Transistor | Cable line, if X16 releases it | Sense GPIO |
|---|---|---|---|
| LOW | Off | HIGH through pullup | HIGH |
| HIGH | On | LOW | LOW |

The sense signal is **not inverted in Rev D**. Firmware should enable input
hysteresis on these GPIOs; the RP2040 provides this in its GPIO hardware.
See the [official GPIO API](https://www.raspberrypi.com/documentation/pico-sdk/hardware.html).
This does not eliminate the need to measure actual PS/2 signal edges.

## Reading the schematic

Read the sheet in order: power, module, logic power, USB keyboard, USB mouse,
PS/2 keyboard, PS/2 mouse. Green wires show connections. A dot means wires
join. A crossing without a dot does not join. Equal net names connect even
when a long wire is omitted between sections.

`R11.1` means pin 1 of resistor R11. `J4.3` means contact 3 of output socket
J4. `GP8` is the GPIO label on the module; it is not physical header pin 8.
The complete [pin table](breadboard-wiring.csv) shows both names.

- R = resistor; its value controls current or establishes a weak HIGH/LOW.
- C = capacitor; the nearby capacitors help keep supplies steady.
- Q = transistor; here it is a switch to ground.
- U = integrated circuit; its physical pin numbers are shown.
- J = connector; JP1 is a removable jumper; F1 is the input fuse.
- An X on a pin means leave it unconnected, not connect it to ground.

The master PDF is one large vector sheet. Zoom in on one section at a time;
printing the entire schematic on one letter-sized page will make the text
small. The assembly PDF is a separate A4 landscape page.

## Three power names to keep separate

**5V_BOARD** comes from the external supply through F1. It powers the two
USB ports. **3V3** comes from the RP2040-Zero and powers U2. **KBD_5V** and
**MOUSE_5V** come from the X16 through the custom cables and supply only the
PS/2 pullups. Do not join those reference nets to 5V_BOARD.

All signal grounds are connected together. A 5 V signal must never be
connected directly to an RP2040 GPIO.

JP1 connects 5V_BOARD to the module's 5 V header. **Remove JP1 before
connecting the module's USB-C to a computer.** This is a manual jumper,
not automatic power-source switching. See the reference
[RP2040-Zero schematic](https://files.waveshare.com/upload/4/4c/RP2040_Zero.pdf)
and verify the actual module before powering it.

## First learning exercise

Build only the keyboard half using [the breadboard guide](breadboard.md).
Identify its drive transistor, pullup and sense buffer on the schematic.
With the X16 disconnected, use test firmware and a meter/logic analyzer to
confirm the truth table above. Then verify host-command handling on a
PS/2 test fixture before attempting an X16 test. Test firmware and bridge
firmware have not yet been supplied or validated in this revision.
