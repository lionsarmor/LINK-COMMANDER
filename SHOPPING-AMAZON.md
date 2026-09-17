# LINK COMMANDER Rev D — Amazon shopping links

For **Rev D: keyboard and mouse only**, using your RP2040-Zero module and an external regulated 5 V supply. All circuit parts other than the assembled RP2040-Zero are through-hole.

**Keyboard** means the first build. **Full** means the total for keyboard plus mouse, not an additional purchase. Quantities are minimum installed quantities; small spare packs are fine. Skip parts you already own. These are alternative sources: do not order the same parts from both lists.

Use [BREADBOARD.md](BREADBOARD.md) for assembly and [BREADBOARD-PARTS.csv](BREADBOARD-PARTS.csv) for component references. Firmware and bench testing are still pending.

## Kits with identified Amazon listings

| Buy | Link | What it supplies |
|---:|---|---|
| 1 kit | [BOJACK 1,350-piece, 50-value resistor kit](https://www.amazon.com/dp/B07P3MFG5D) | All six required values: 22 Ω, 15 kΩ, 2.2 kΩ, 47 kΩ, 4.7 kΩ and 100 kΩ. Listing specifies 1%, ¼ W metal-film resistors. |
| 1 kit | [BOJACK 630-piece radial electrolytic capacitor kit](https://www.amazon.com/dp/B07PBQXQNQ) | 10 µF, 220 µF and 470 µF capacitors rated at least 10 V. Breadboard selection; assortment dimensions are not guaranteed to fit the PCB. |

The capacitor kit does **not** replace the separate 100 nF ceramic capacitors. Kits are optional; individual-value links below are alternatives.

## Individual parts

The following links are explicitly **Amazon searches**, not verified seller listings. Match the complete value and package. I could not verify an Amazon listing for either DIP chip; the [Mouser list](SHOPPING-MOUSER.md) identifies both exact parts. Do not substitute an SMD package or a similarly named chip.

| Part | Keyboard | Full | Amazon search |
|---|---:|---:|---|
| TPS2042P power-switch chip, DIP-8 | 1 | 1 | [Search](https://www.amazon.com/s?k=TPS2042P+DIP+8) |
| CD4050BE buffer chip, DIP-16 | 1 | 1 | [Search](https://www.amazon.com/s?k=CD4050BE+DIP+16) |
| 2N3904 transistor, TO-92 | 2 | 4 | [Search](https://www.amazon.com/s?k=2N3904+TO-92+transistor) |
| 22 Ω resistor | 2 | 4 | [Search](https://www.amazon.com/s?k=22+ohm+1+percent+1%2F4+watt+axial+resistor) |
| 15 kΩ resistor | 2 | 4 | [Search](https://www.amazon.com/s?k=15k+ohm+1+percent+1%2F4+watt+axial+resistor) |
| 2.2 kΩ resistor | 3 | 6 | [Search](https://www.amazon.com/s?k=2.2k+ohm+1+percent+1%2F4+watt+axial+resistor) |
| 47 kΩ resistor | 2 | 4 | [Search](https://www.amazon.com/s?k=47k+ohm+1+percent+1%2F4+watt+axial+resistor) |
| 4.7 kΩ resistor | 2 | 4 | [Search](https://www.amazon.com/s?k=4.7k+ohm+1+percent+1%2F4+watt+axial+resistor) |
| 100 kΩ resistor | 2 | 4 | [Search](https://www.amazon.com/s?k=100k+ohm+1+percent+1%2F4+watt+axial+resistor) |
| 100 nF / 0.1 µF ceramic capacitor, leaded | 3 | 4 | [Search](https://www.amazon.com/s?k=100nF+50V+ceramic+capacitor+radial+5mm) |
| 470 µF electrolytic capacitor, radial | 1 | 1 | [Search](https://www.amazon.com/s?k=470uF+16V+radial+electrolytic+capacitor) |
| 10 µF electrolytic capacitor, radial | 1 | 1 | [Search](https://www.amazon.com/s?k=10uF+16V+radial+electrolytic+capacitor) |
| 220 µF electrolytic capacitor, radial | 1 | 2 | [Search](https://www.amazon.com/s?k=220uF+16V+radial+electrolytic+capacitor) |
| Red 3 mm LED | 1 | 2 | [Search](https://www.amazon.com/s?k=3mm+red+LED+through+hole) |
| 1.5 A fast-blow fuse, 5 × 20 mm | 1 | 1 | [Search](https://www.amazon.com/s?k=1.5A+fast+blow+fuse+5x20) |

## Already owned / connector hardware

| Item | Keyboard | Full | Link / action |
|---|---:|---:|---|
| Your RP2040-Zero module | 1 | 1 | [Your supplied hiBCTR listing](https://www.amazon.com/dp/B0DXL12W59); keep the module you already have. |
| USB-A female connector | 1 | 2 | Reuse the USB connector breakouts shown in your photo during breadboarding. |
| 7-pin DIN female connector | 1 | 2 | Reuse your DIN connector breakouts during breadboarding; confirm pin numbering by continuity. |

The final PCB has directly soldered sockets. If buying those now, use the exact connector selections in [SHOPPING-MOUSER.md](SHOPPING-MOUSER.md), not a visually similar Amazon connector.

## Power, wiring and tools — Amazon search links

| Item | Quantity | Search | What to select |
|---|---|---|---|
| External regulated 5 V DC supply, at least 2 A | 1 | [Search](https://www.amazon.com/s?k=regulated+5V+2A+power+adapter+5.5mm+2.1mm+center+positive) | Select fixed 5 V output, center-positive 5.5 × 2.1 mm plug for the adapter below. Keep the 1.5 A circuit fuse. |
| Matching power adapter to insulated wires | 1 | [Search](https://www.amazon.com/s?k=5.5mm+2.1mm+female+DC+power+pigtail) | Connect through the fuse holder to J1; meter-check polarity. A pigtail is cable hardware, not an extra electronic module. |
| Inline fuse holder, 5 × 20 mm | 1 | [Search](https://www.amazon.com/s?k=5x20+inline+fuse+holder+wire) | Must accept the selected fuse; rated at least 2 A and 5 V DC. |
| Solderless breadboard | 1 large board; another if crowded | [Search](https://www.amazon.com/s?k=830+breadboard+solderless) | Already shown in your photo; buy only if more space is needed. |
| 22 AWG solid-core hookup wire / short jumper leads | 1 assortment | [Search](https://www.amazon.com/s?k=22+awg+solid+core+breadboard+jumper+wire) | Keep USB data wires short; use suitable heavier leads for the external supply. |
| 2.54 mm single-row male headers | 2 × 9 pins + 1 × 5 pins | [Search](https://www.amazon.com/s?k=2.54mm+male+header+single+row+breakaway) | Only if the RP2040-Zero does not already have headers. A 40-pin strip can be cut to length. |
| Removable module-power jumper, JP1 | 1 | [Search](https://www.amazon.com/s?k=breadboard+male+male+jumper+wires) | A short removable jumper wire works on the breadboard. |
| 7-pin DIN male cable plug | 1 keyboard / 2 full | [Search](https://www.amazon.com/s?k=7+pin+DIN+male+solder+connector) | Match the physical pin pattern of your existing socket; generic 7-pin connectors are not automatically interchangeable. |
| PS/2 cable with 6-pin mini-DIN male end | 1 keyboard / 2 full | [Search](https://www.amazon.com/s?k=PS2+6+pin+mini+DIN+male+extension+cable) | For the custom output cable; identify conductors by continuity, not color. An extension cable can supply a male-ended cable section. |
| Cable finishing materials | Enough for 1 / 2 cables | [Search](https://www.amazon.com/s?k=heat+shrink+tubing+cable+strain+relief) | Four insulated conductors per custom PS/2 cable; add cable if the PS/2 cable section is too short. |
| USB-C data cable | 1 | [Search](https://www.amazon.com/s?k=USB+C+data+cable) | Use for programming the module; remove JP1 before connecting the PC. |
| Multimeter with DC voltage and continuity | 1 | [Search](https://www.amazon.com/s?k=digital+multimeter+continuity+DC+voltage) | Skip if you have one. |

A paired USB keyboard/receiver and later a mouse/receiver are also required for testing. Use your existing devices. A wired USB keyboard is another initial test option; receiver support depends on the firmware.

Listing specifications researched on 2026-09-17. Prices, sellers and availability can change; no price or stock guarantee is implied.
