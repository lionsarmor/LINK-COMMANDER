# LINK COMMANDER Rev D — Mouser breadboard shopping list

**Choose this list OR the Amazon list. Do not buy both lists.** This document now includes the circuit parts, connectors, power supply, wire, insulation, breadboards and custom-cable materials. Nothing in its purchase tables depends on the Amazon shopping document.

**One sourcing exception:** the specified **hiBCTR RP2040-Zero module, M1**, is already yours. I could not verify that exact module at Mouser. Reuse it, or buy the [same module on Amazon — B0DXL12W59](https://www.amazon.com/dp/B0DXL12W59). A Raspberry Pi Pico is not a drop-in replacement. This is therefore a complete breadboard checklist with one explicit outside-store module, not a claim that Mouser sells everything.

## Exact order

The table includes replacements for your existing connectors, headers, breadboard and meter so it also works as a from-scratch checklist. **Delete those rows from your cart if reusing them.** Bare USB/DIN sockets need short soldered, insulated leads to reach breadboard holes; do not force their pins or shell tabs into the breadboard.

| Part | Keyboard only | Full build | Mouser SKU — direct link | Manufacturer part number | Use / reference |
|---|---:|---:|---|---|---|
| USB power-switch chip — PDIP-8 | 1 | 1 | [595-TPS2042P](https://www.mouser.com/en/ProductDetail/Texas-Instruments/TPS2042P?qs=sGAEpiMZZMv0DJfhVcWlK5dti4XbSOwogfbpZrAIrQU%3D) | TPS2042P | U1 |
| PS/2 input buffer — PDIP-16 | 1 | 1 | [595-CD4050BE](https://www.mouser.com/en/ProductDetail/Texas-Instruments/CD4050BE?qs=j%2FZo4ajzVJLKLpJvKsajlg%3D%3D) | CD4050BE | U2 |
| NPN transistor — TO-92 | 2 | 4 | [512-2N3904BU](https://www.mouser.com/en/ProductDetail/onsemi/2N3904BU?qs=or4AE2qAS%252Bd0Jdpn%2F8ktKg%3D%3D) | 2N3904BU | Q1 Q2 Q3 Q4 |
| 22 Ω resistor — 1%, ¼ W, axial; select Cut Tape | 2 | 4 | [603-MFR-25FRF52-22R](https://www.mouser.com/en/ProductDetail/YAGEO/MFR-25FRF52-22R?qs=oAGoVhmvjhwUlsp%2F3bYXqg%3D%3D) | MFR-25FRF52-22R | R1 R2 R6 R7 |
| 15 kΩ resistor — 1%, ¼ W, axial | 2 | 4 | [603-MFR-25FBF52-15K](https://www.mouser.com/en/ProductDetail/YAGEO/MFR-25FBF52-15K?qs=oAGoVhmvjhzZTLCD9uq%2F7w%3D%3D) | MFR-25FBF52-15K | R3 R4 R8 R9 |
| 2.2 kΩ resistor — 1%, ¼ W, axial | 3 | 6 | [603-MFR-25FBF52-2K2](https://www.mouser.com/en/ProductDetail/YAGEO/MFR-25FBF52-2K2?qs=oAGoVhmvjhwVT9mopfAMPA%3D%3D) | MFR-25FBF52-2K2 | R5 R10 R11 R15 R19 R23 |
| 47 kΩ resistor — 1%, ¼ W, axial | 2 | 4 | [603-MFR-25FBF52-47K](https://www.mouser.com/en/ProductDetail/YAGEO/MFR-25FBF52-47K?qs=oAGoVhmvjhwOchl34Oamzw%3D%3D) | MFR-25FBF52-47K | R12 R16 R20 R24 |
| 4.7 kΩ resistor — 1%, ¼ W, axial | 2 | 4 | [603-MFR-25FBF52-4K7](https://www.mouser.com/en/ProductDetail/YAGEO/MFR-25FBF52-4K7?qs=oAGoVhmvjhyEuU2iU0uA4w%3D%3D) | MFR-25FBF52-4K7 | R13 R17 R21 R25 |
| 100 kΩ resistor — 1%, ¼ W, axial | 2 | 4 | [603-MFR-25FBF52-100K](https://www.mouser.com/en/ProductDetail/YAGEO/MFR-25FBF52-100K?qs=oAGoVhmvjhxAqZbyE%2Fs9bg%3D%3D) | MFR-25FBF52-100K | R14 R18 R22 R26 |
| 100 nF ceramic capacitor — 50 V, leaded | 3 | 4 | [594-K104K15X7RF5TH5](https://www.mouser.com/en/ProductDetail/Vishay-BC-Components/K104K15X7RF5TH5?qs=CuWZN%2F5Vbiofhf%252BuZNGw%2Fg%3D%3D) | K104K15X7RF5TH5 | C3 C4 C6 C8 |
| 470 µF electrolytic — 25 V, radial | 1 | 1 | [647-UVR1E471MPD](https://www.mouser.com/en/ProductDetail/Nichicon/UVR1E471MPD?qs=eBzRnwgjaQf16mhkgyDt6A%3D%3D) | UVR1E471MPD | C1 |
| 10 µF electrolytic — 50 V, radial | 1 | 1 | [667-EEU-FR1H100](https://www.mouser.com/en/ProductDetail/Panasonic-Industry/EEU-FR1H100?qs=tfZGHB2PWd1NAbdNSgjToQ%3D%3D) | EEU-FR1H100 | C2 |
| 220 µF electrolytic — 16 V, radial | 1 | 2 | [667-EEU-FR1C221](https://www.mouser.com/en/ProductDetail/Panasonic-Industry/EEU-FR1C221?qs=sGAEpiMZZMsh%252B1woXyUXj1qMLSoXX8Md3jdDfI7Gxc0%3D) | EEU-FR1C221 | C5 C7 |
| Red LED — 3 mm, through-hole | 1 | 2 | [604-WP710A10ID](https://www.mouser.com/en/ProductDetail/Kingbright/WP710A10ID?qs=wRBQ8ZgBZ98VyHeNIlWGkQ%3D%3D) | WP710A10ID | D1 D2 |
| 1.5 A fast-blow fuse — 5 × 20 mm | 1 | 1 | [504-BK1/GMA-1.5-R](https://www.mouser.com/en/ProductDetail/Eaton-Electronics/BK1-GMA-1.5-R?qs=9GX7soZQXxHHwQMtPHv6gQ%3D%3D) | BK1/GMA-1.5-R | F1 |
| Inline fuse holder — 5 × 20 mm, wire leads | 1 | 1 | [576-01500274Z](https://www.mouser.com/en/ProductDetail/Littelfuse/01500274Z?qs=2VFNtWizgidXPNQ%2FDEp6Dw%3D%3D) | 01500274Z | F1 holder |
| Regulated 5 V / 3 A wall supply — US plug | 1 | 1 | [709-GSM18U05-P1J](https://www.mouser.com/en/ProductDetail/MEAN-WELL/GSM18U05-P1J?qs=y5B8D4YB%2F3Q73ALXdTERfw%3D%3D) | GSM18U05-P1J | External supply |
| 5.5 × 2.1 mm female barrel-to-screw-terminal adapter | 1 | 1 | [485-368](https://www.mouser.com/en/ProductDetail/Adafruit/368?qs=GURawfaeGuDj%2FuiL%252B50YjQ%3D%3D) | 368 | J1 breadboard connection |
| 7-pin DIN male cable plug — solder terminals | 1 | 2 | [490-SDR-70](https://www.mouser.com/en/ProductDetail/Same-Sky/SDR-70?qs=WyjlAZoYn525nOK6Wu9GaQ%3D%3D) | SDR-70 | Custom PS/2 cable plugs |
| 22 AWG solid-core hookup wire — six-color spool set | 1 | 1 | [485-1311](https://www.mouser.com/en/ProductDetail/Adafruit/1311?qs=GURawfaeGuBbUKgxUfZ%252BxQ%3D%3D) | 1311 | Wiring and removable JP1 jumper |
| Heat-shrink assortment | 1 | 1 | [474-PRT-09353](https://www.mouser.com/en/ProductDetail/SparkFun/PRT-09353?qs=WyAARYrbSnbX2QgoKpWtUQ%3D%3D) | PRT-09353 | Insulation for cable and power joints |
| PS/2 male-to-female extension cable — 6 ft | 1 | 2 | [545-P222006](https://www.mouser.com/en/ProductDetail/Tripp-Lite/P222-006?qs=sukvznpo3Fq6Bwrm0MV4eQ%3D%3D) | P222-006 | One male-ended cable section per output |
| USB-A to USB-C data cable — approximately 1 m | 1 | 1 | [485-4474](https://www.mouser.com/en/ProductDetail/Adafruit/4474?qs=CUBnOrq4ZJz9F%2FNF%252BRRALQ%3D%3D) | 4474 | Module programming |
| Male-to-female jumper wires — 20-pack | 1 | 1 | [485-1954](https://www.mouser.com/en/ProductDetail/Adafruit/1954?qs=GURawfaeGuCB%252BLTF1NsFig%3D%3D) | 1954 | Reach module end-header contacts |
| Full-size solderless breadboard — two give working space | 2 | 2 | [485-239](https://www.mouser.com/en/ProductDetail/Adafruit/239?qs=GURawfaeGuBO%2FIaAv%252BnS1w%3D%3D) | 239 | Reuse existing boards if adequate |
| USB-A female through-hole socket | 1 | 2 | [538-67643-3910](https://www.mouser.com/en/ProductDetail/Molex/67643-3910?qs=x6EjVpvqMVPR04zsu4B0aw%3D%3D) | 67643-3910 | J2 J3; reuse existing breakouts or solder short leads |
| 7-pin DIN female through-hole socket | 1 | 2 | [490-SDS-70J](https://www.mouser.com/en/ProductDetail/Same-Sky/SDS-70J?qs=sGAEpiMZZMtAYTMy7wxAr38XxmkflkdN2GGAM5wDr1DA1h1NpC6HFw%3D%3D) | SDS-70J | J4 J5; reuse existing breakouts or solder short leads |
| Male header strips — ten 36-pin strips, 2.54 mm | 1 | 1 | [485-392](https://www.mouser.com/en/ProductDetail/Adafruit/392?qs=GURawfaeGuBPkJS%252B96amuQ%3D%3D) | 392 | M1 headers; omit if already fitted |
| Multimeter for DC voltage, resistance and continuity | 1 | 1 | [485-850](https://www.mouser.com/en/ProductDetail/Adafruit/850?qs=GURawfaeGuBADKQ4LzdFCg%3D%3D) | 850 | Bench tool; omit if owned |

**Order CSVs:** [Keyboard + mouse](SHOPPING-MOUSER-ORDER.csv) · [Keyboard only](SHOPPING-MOUSER-KEYBOARD.csv). Each has 29 unique SKU rows, matching this table. They exclude the outside-store module and workshop tools. Remove already-owned rows before ordering. Select **Cut Tape** for the 22 Ω resistors.

## Cable and power details

- Buy **two P222-006 cables** for the full build. Each has only **one male PS/2 end**. Cut each about 3 ft from its male end and solder an SDR-70 plug to the cut wires using the project's custom-cable pin table. The remaining female-ended sections are unused. Do not buy just one expecting two male ends.
- SDR-70 is a full-size 7-pin DIN cable plug; it is not a PS/2 connector. It matches the SDS-70J family. Check the fit against existing Treedix sockets before soldering. Identify every conductor by continuity, never wire color.
- GSM18U05-P1J supplies regulated **5 V, up to 3 A**, with a US mains plug and a center-positive 5.5×2.1 mm output. Keep the specified **1.5 A fast 5×20 mm fuse**. Connect the barrel adapter positive through that fuse to J1.1; negative goes to J1.2/common ground.
- Splice the inline holder's 16 AWG leads to short 22 AWG solid-core leads; insulate every joint. Do not force thick or stranded wire into breadboard contacts.
- Cut module male headers into **9 + 9 + 5 contacts** if needed. Use male-to-female jumpers for the module's offset end header. Use short solid-core connections for USB D+/D−; long jumper ribbons are not the USB data wiring.
- JP1 is one labeled removable wire from the hookup-wire kit; it needs no extra component on the breadboard.
- The capacitor voltage ratings are maximum ratings, not supply settings. The selected individual capacitors meet the existing PCB's nominal lead spacing/body limits; the circuit remains a 5 V design.

## What this order covers

This is the **Rev D keyboard-and-mouse breadboard**, including its external power supply and two custom cables to the X16. It covers every electrical position in [BREADBOARD-PARTS.csv](BREADBOARD-PARTS.csv). Keyboard-only quantities are an alternative to full-build quantities; do not add them together. All circuit components are through-hole except the assembled RP2040-Zero module. Passive connector breakouts are for breadboarding only.

Have a soldering iron, electronics solder, wire stripper/cutter, small screwdriver and suitable heat source for heat-shrink available. These workshop tools are not included in the component order. The multimeter is listed. The later firmware validation also requires access to a suitable logic analyzer, preferably an oscilloscope, and a computer. Reuse your keyboard, mouse, paired USB receivers and Commander X16; peripheral compatibility is still subject to testing.

This is **not a complete PCB assembly order**. The later carrier adds DIP sockets, female module sockets, PCB fuse clips, JP1 header/shunt, mounting hardware and the fabricated PCB; see [PCB parts](hardware/rev-d/parts.md). The 26 PCB test holes do not require purchased components for this breadboard.

Follow [BREADBOARD.md](BREADBOARD.md), including polarity/continuity checks and removing JP1 before connecting the module to the programming computer. Firmware and physical validation remain pending. Listings were reviewed September 18, 2026; stock, seller and delivery can change.
