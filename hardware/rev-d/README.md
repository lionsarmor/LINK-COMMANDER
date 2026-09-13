# LINK COMMANDER — Rev D

Rev D translates supported **USB keyboards and mice** into the PS/2
keyboard and mouse interfaces used by the Commander X16. Wired peripherals
and manufacturers' 2.4 GHz USB receivers use the same two USB input ports.
Gamepad support has been removed from this revision.

The RP2040-Zero plugs into removable headers. Every other carrier component
is through-hole. There are **two socketed DIP chips and four transistors**.
The board is **140 × 80 mm**, has **two copper layers** and 4 mm corner radii,
and retains the KiCad/open-hardware logos.

The board and USB receivers use a separate regulated **5 V / 2 A supply**.
The X16 PS/2 +5 V pins supply only their signal pull-ups; they do not power
the RP2040 or USB ports. All grounds are shared.

## Start here

- [Student design guide: how the circuit works](student-guide.md)
- [One-page schematic PDF](review/schematic.pdf)
- [Assembly PDF](review/assembly.pdf) and [PCB preview](review/pcb-top.png)
- [Editable KiCad project](kicad/link-commander.kicad_pro)
- [Breadboard guide and custom cable table](breadboard.md)
- [Every physical pin](breadboard-wiring.csv) and [connections grouped by net](net-connections.csv)
- [Grouped BOM](bom-grouped.csv), [individual BOM](bom.csv), [purchasing notes](parts.md)
- [Firmware interface and test requirements](firmware-contract.md)
- [Validation reports](review/design-checks.txt), [PCB DRC](review/pcb-drc.txt)
- [Rebuild instructions](tools/README.md)

## What changed from Rev C

| | Rev C | Rev D |
|---|---:|---:|
| USB inputs | 4 | 2: keyboard and mouse |
| DIN outputs | 4 | 2: PS/2 keyboard and mouse |
| Socketed DIP ICs | 17 | 2 |
| Transistors | 7 | 4 |
| Component positions, including mounting holes | 143 | 54 |
| Board | 230 × 130 mm, four layers | 140 × 80 mm, two layers |

The gamepad shift registers, resistor networks and control gates are gone.
One TPS2042P replaces the two individual USB power chips. One CD4050 handles all four PS/2 sense lines. The separate HC14 inverter
stage and four input/output series-resistor pairs have been removed. Both
channels of the USB power chip are enabled directly by ground, so no shared enable
transistor or RUN_ENABLE GPIO is required. Port fault LEDs remain useful
for students during bring-up.

**Rev D sense signals are non-inverting:** HIGH means the cable line is
HIGH. The old Rev C firmware assumptions and component reference numbers
must not be reused without updating them. PS/2 drive HIGH still pulls LOW.

The DIN-to-PS/2 cable signal assignment is unchanged, but the output
connectors are now J4 and J5. Use the Rev D wiring tables exclusively.

## Prototype status

The saved PCB passes KiCad clearance/connectivity checks, and the exported
schematic netlist matches the canonical circuit. All populated component
pads are through-hole. These are CAD checks, not evidence of a working
physical adapter: module/socket fit, USB signal integrity, power sequencing,
PS/2 timing, firmware and receiver compatibility still need bench testing.
The two-layer ground pour is interrupted by routes; it is not a dedicated
unbroken reference plane or a controlled-impedance qualification.

No working bridge firmware or fabrication release is supplied here. Start
with the standalone breadboard tests. Do not connect the X16 until the
firmware and cable checks in the guide have passed.
