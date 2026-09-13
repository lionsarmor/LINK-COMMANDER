# Rev D test points

The external regulated **5 V supply stays in use**. PS/2 power is still
separate and supplies only the cable-side signal pull-ups.

The PCB has **26 dedicated plated test holes**, labeled TP1–TP26. Each has
2 mm exposed copper on both sides and a 1 mm plated hole. Probe the pad
as supplied, or solder in an optional short single through-hole pin that
fits the hole. No extra component is required for the circuit to work.
Keep optional pins upright and short; do not let them contact nearby parts.

Locate TP numbers on the assembly PDF and in schematic section 8. Equal
net labels connect the test symbols to the circuits in sections 1–7.
The [test-point CSV](test-points.csv) also includes the four existing USB
data probe pads. Board coordinates in [placement.csv](placement.csv) use
the KiCad origin, not a breadboard row number.

## Power: use a multimeter first

Measure relative to any GND test point. The voltages below are nominal
expectations for a correctly powered board, not measured test results.

| Test point | Net | What to check |
|---|---|---|
| TP8 | 5V_INPUT | External 5 V before F1 |
| TP1 | 5V_BOARD | External 5 V after F1 |
| TP2 | 5V_MODULE | Module supply after JP1; may instead come from PC USB when JP1 is removed |
| TP3 | 3V3 | Module-regulated 3.3 V powering U2 |
| TP4 | USB1_5V | Keyboard receiver supply after U1 |
| TP5 | USB2_5V | Mouse receiver supply after U1 |
| TP6 | KBD_5V | Keyboard cable's X16 +5 V reference |
| TP7 | MOUSE_5V | Mouse cable's X16 +5 V reference |
| TP23, TP24, TP25, TP26 | GND | Four locations for meter/probe ground |

TP6/TP7 are not powered by the external supply. Expect them to be unpowered
with the X16 disconnected unless the isolated bench fixture supplies the
references. Do not bridge them to TP1, TP2, TP4 or TP5.

Remove JP1 before attaching PC USB-C, as in the breadboard guide. Test
points are for measurement; they are not power-selection jumpers.

## PS/2: compare drive, cable and sense

| Signal | Drive: 3.3 V GPIO | Cable: 5 V domain | Sense: 3.3 V GPIO |
|---|---|---|---|
| Keyboard DATA | TP13 / GP8 | TP9 / KBD_DATA | TP17 / GP9 |
| Keyboard CLOCK | TP14 / GP10 | TP10 / KBD_CLOCK | TP18 / GP11 |
| Mouse DATA | TP15 / GP12 | TP11 / MOUSE_DATA | TP19 / GP13 |
| Mouse CLOCK | TP16 / GP14 | TP12 / MOUSE_CLOCK | TP20 / GP15 |

With the reference powered and the host releasing the line:

- Drive LOW releases the transistor; cable and sense should become HIGH.
- Drive HIGH turns the transistor on; cable and sense should become LOW.

The X16 can also pull a cable line LOW while the drive GPIO is LOW. That
is normal PS/2 behavior. A meter can check static levels; use an oscilloscope
or suitable logic analyzer for edges, timing and protocol traffic. For a
3.3 V-only analyzer, use the sense points, not the 5 V cable points.

## USB power faults

| Test point | Net | Connection |
|---|---|---|
| TP21 | USB1_FAULT | U1 pin 8 and keyboard fault LED cathode |
| TP22 | USB2_FAULT | U1 pin 5 and mouse fault LED cathode |

These open-drain fault outputs pull LOW when asserted. The LED/resistor
path returns to 5V_BOARD; these are not 3.3 V logic test points. The inactive
voltage is not specified as a digital HIGH by this LED circuit. Start by
observing the fault LED and measuring with a high-impedance meter or probe.

## USB data: existing pads, no additional branches

Use the exposed pin-1 annulus or lead of the corresponding 15 kΩ resistor.
The nearby silkscreen identifies USB1/USB2 and D+/D−. Pin 1 is the left
pad of these horizontal resistors in the top assembly view; pin 2 is GND.

| USB signal | Existing probe pad | Nearby ground pad |
|---|---|---|
| Keyboard D+ | R3.1 | R3.2 |
| Keyboard D− | R4.1 | R4.2 |
| Mouse D+ | R8.1 | R8.2 |
| Mouse D− | R9.1 | R9.2 |

No dedicated header or long test-point branch was added to the USB data
nets. Use a suitable low-capacitance probe with a short ground connection;
probe loading can change the signal being measured. See
[Tektronix's probe primer](https://www.tek.com/en/documents/whitepaper/abcs-probes-primer).
A basic GPIO logic analyzer capture is not a USB signal-integrity test.

## Other accessible nodes

The module-side USB signals are available at R1.1, R2.1, R6.1 and R7.1.
Transistor bases are accessible at Q1.2–Q4.2 or their base-resistor ends.
LED anodes are accessible at D1.2/D2.2. Unused module GPIOs remain available
at their original perimeter header contacts. Use the full wiring CSV to
identify these nodes; do not assume they have the same voltage or function
as the nearby dedicated test point.

Begin with the X16 disconnected and follow the staged tests in
[breadboard.md](breadboard.md). Firmware and physical test results are
still outstanding; adding test access does not validate the adapter.
