# Rev D parts and assembly

Use [bom-grouped.csv](bom-grouped.csv) for quantities and [bom.csv](bom.csv)
for individual references. All carrier components are through-hole; the
already assembled RP2040-Zero plugs into removable headers.

## Chips, sockets and connectors

| Quantity | Part |
|---:|---|
| 1 | User's hiBCTR RP2040-Zero module, ASIN B0DXL12W59; verify actual header geometry |
| 2 + 1 | 1×9 + 1×5 male headers, 2.54 mm, on the module |
| 2 + 5 | SSW-109-01-T-S 9-contact female sockets + SSW-101-01-T-S individual sockets on the carrier; see orientation below |
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

## Five-board purchasing documents

[Full Mouser PO](../../MOUSER-PO-01-FIVE-PCBS.md) ([PDF](../../MOUSER-PO-01-FIVE-PCBS.pdf), [CSV](../../MOUSER-PO-01-FIVE-PCBS.csv)) includes the circuit components, sockets, fuse clips, mounting feet, external supplies and custom-cable materials for five PCBs. The [chips-only PO](../../MOUSER-PO-02-CHIPS-ONLY.md) contains five of each DIP IC. Both are plain parts tables for presenting to Mouser; no order has been submitted. Arrange pricing and will-call pickup with the supplier. Supply five RP2040-Zero modules and five fabricated boards separately.

### Selected module sockets

For each board, use two Samtec **SSW-109-01-T-S** sockets for the side rows
and five **SSW-101-01-T-S** individual sockets at M1 contacts 10–14. Turn
the single sockets so their **3.05 mm dimension runs parallel to the long
side rows**, with their **2.41 mm dimension along the end row**. All sockets
have the same nominal 8.51 mm body height. Align them on the actual module
before soldering; keep the module removable.

This is a purchasing/assembly refinement; no holes or circuit connections
change. The [Samtec drawing](https://suddendocs.samtec.com/catalog_english/ssw_th.pdf)
specifies a row housing length of contact count × 2.54 mm + 0.51 mm. A complete
SSW-105 housing would nominally overlap the side-row housings at this
footprint's corners. Rotated individual end sockets avoid that overlap,
with nominal 0.13 mm lateral clearance. Manufacturing tolerances and clone
module dimensions still require a physical sample fit. Do not substitute
a complete 5-contact socket strip without checking its housing dimensions.

One Adafruit 392 pack supplies all five modules' male headers and five
2-pin JP1 headers: use five strips, cutting each into 9 + 9 + 5 + 2 contacts.
Ten Littelfuse **01110501Z** clips supply the five fuse positions; these
are individual clips, two per fuse, not complete holders.

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
