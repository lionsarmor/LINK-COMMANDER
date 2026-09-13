# Rev D parts and assembly

Use [bom-grouped.csv](bom-grouped.csv) for quantities and [bom.csv](bom.csv)
for individual references. All carrier components are through-hole; the
already assembled RP2040-Zero plugs into removable headers.

## Chips, sockets and connectors

| Quantity | Part |
|---:|---|
| 1 | User's hiBCTR RP2040-Zero module, ASIN B0DXL12W59; verify actual header geometry |
| 2 + 1 | 1×9 + 1×5 male headers, 2.54 mm, on the module |
| 2 + 1 | Matching 1×9 + 1×5 female sockets on the carrier |
| 1 | TPS2042P, PDIP-8, dual channel, active-low enables |
| 1 | CD4050BE, PDIP-16, non-inverting level converter |
| 1 + 1 | DIP-8 + DIP-16 sockets, 7.62 mm row spacing |
| 4 | 2N3904 TO-92; verify 1=emitter, 2=base, 3=collector |
| 2 | USB-A receptacles matching Molex 67643-3910 and the supplied THT footprint |
| 2 | Same Sky SDS-70J, 7-contact right-angle PCB DIN sockets |
| 1 | TE 282834-2, two-position, 2.54 mm pitch input terminal |
| 1 pair | Littelfuse 111-series PCB clips matching the supplied 5×20 fuse footprint |
| 1 | 1.5 A fast 5×20 fuse, chosen for the specified clips and supply |
| 1 | Two-pin 2.54 mm header and removable shunt for JP1 |
| 2 | Red 3 mm LEDs |
| 4 sets | M3 insulating standoffs/screws |

The header and DIP sockets, fuse clips, cable plugs, power supply and
mounting hardware are additional purchasing items, not extra electrical
IC positions. Use complete manufacturer part numbers: “74HC”, “CD4050”
or “TPS2042” alone does not specify a through-hole package.

## Optional test contacts

TP1–TP26 are bare plated holes already part of the PCB, not 26 required
purchased parts. Each has 2 mm copper and a 1 mm drill. Optional short
single through-hole pins can be fitted for clip probes; check lead fit.
The BOM lists the test positions for traceability. There are still only
50 electrical parts, plus four mounting holes and these 26 test contacts.
See [test-points.md](test-points.md) for the map and voltage domains.

## Resistors and capacitors

| Quantity | Value | References |
|---:|---|---|
| 4 | 22 Ω | R1, R2, R6, R7 |
| 4 | 15 kΩ | R3, R4, R8, R9 |
| 6 | 2.2 kΩ | R5, R10, R11, R15, R19, R23 |
| 4 | 47 kΩ | R12, R16, R20, R24 |
| 4 | 4.7 kΩ | R13, R17, R21, R25 |
| 4 | 100 kΩ | R14, R18, R22, R26 |
| 4 | 100 nF ceramic | C3, C4, C6, C8 |
| 2 | 220 µF / 10 V electrolytic | C5, C7 |
| 1 | 470 µF / 10 V electrolytic | C1 |
| 1 | 10 µF / 10 V electrolytic | C2 |

Use 1% axial 0.25 W resistors, approximately 6.3 × 2.5 mm bodies with
10.16 mm formed lead spacing. The ceramics use 5 mm lead spacing.
C5/C7: 2.5 mm pitch, maximum 6.3 mm diameter. C1: 5 mm pitch, maximum
10 mm diameter. C2: 2 mm pitch, maximum 5 mm diameter. Verify actual
parts against the footprints; electrolytic pin 1 is positive.

## Before assembly

Confirm the actual module and DIN socket against a 1:1 PCB print and samples.
The module footprint is nominal Waveshare-style perimeter-header geometry;
a clone's appearance alone does not prove its mechanical fit. The custom
DIN footprint follows the terminal positions on page 4 of the
[manufacturer drawing](https://www.sameskydevices.com/product/resource/sds-j.pdf).
That drawing's hole-count annotation is inconsistent with its visible
terminal positions, so sample fit is still required.

The supplied local footprint library includes the two logo footprints;
see [FOOTPRINT-LICENSE.txt](kicad/FOOTPRINT-LICENSE.txt) for library licensing.
The logos are silkscreen graphics, not a certification claim.

Solder low parts first: resistors, IC sockets, small capacitors, transistors,
headers/connectors, then tall capacitors. Leave the chips and module out
while inspecting joints and checking power continuity. Align DIP notches,
LED polarity, electrolytic polarity and transistor leads with the assembly
PDF. Install the module sockets using the module as an alignment guide.
The mounting-hole locations are intentionally asymmetric to clear parts.

Provide regulated 5 V / 2 A power, a multimeter, a logic analyzer and ideally
an oscilloscope. There is no dedicated external USB ESD suppressor in this
bench revision. A product release still needs connector ESD and USB signal
integrity review in addition to firmware and electrical testing.
