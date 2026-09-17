# LINK COMMANDER Rev D — Mouser shopping links

For **Rev D: keyboard and mouse only**, using your RP2040-Zero module and an external regulated 5 V supply. All circuit parts other than the assembled RP2040-Zero are through-hole.

**Keyboard** means the first build. **Full** means the total for keyboard plus mouse, not an additional purchase. Quantities are minimum installed quantities; small spare packs are fine. Skip parts you already own. These are alternative sources: do not order the same parts from both lists.

Use [BREADBOARD.md](BREADBOARD.md) for assembly and [BREADBOARD-PARTS.csv](BREADBOARD-PARTS.csv) for component references. Firmware and bench testing are still pending.

## Circuit components

These links search **exact manufacturer part numbers** on Mouser. Select the matching part, not a suggested substitute. This keeps the links usable across Mouser country stores. Stock and prices must be checked at checkout.

All six resistor selections are axial, 1%, ¼ W. The capacitor voltage ratings below exceed the circuit's minimum 10 V rating; they do not change the supply voltage, which remains 5 V.

| Part | Keyboard | Full | Exact part — Mouser search |
|---|---:|---:|---|
| TPS2042P power-switch chip, DIP-8 | 1 | 1 | [TPS2042P](https://www.mouser.com/c/?q=TPS2042P) |
| CD4050BE buffer chip, DIP-16 | 1 | 1 | [CD4050BE](https://www.mouser.com/c/?q=CD4050BE) |
| 2N3904 transistor, TO-92 | 2 | 4 | [2N3904BU](https://www.mouser.com/c/?q=2N3904BU) |
| 22 Ω resistor | 2 | 4 | [MFR-25FBF52-22R](https://www.mouser.com/c/?q=MFR-25FBF52-22R) |
| 15 kΩ resistor | 2 | 4 | [MFR-25FBF52-15K](https://www.mouser.com/c/?q=MFR-25FBF52-15K) |
| 2.2 kΩ resistor | 3 | 6 | [MFR-25FBF52-2K2](https://www.mouser.com/c/?q=MFR-25FBF52-2K2) |
| 47 kΩ resistor | 2 | 4 | [MFR-25FBF52-47K](https://www.mouser.com/c/?q=MFR-25FBF52-47K) |
| 4.7 kΩ resistor | 2 | 4 | [MFR-25FBF52-4K7](https://www.mouser.com/c/?q=MFR-25FBF52-4K7) |
| 100 kΩ resistor | 2 | 4 | [MFR-25FBF52-100K](https://www.mouser.com/c/?q=MFR-25FBF52-100K) |
| 100 nF / 0.1 µF ceramic capacitor, leaded | 3 | 4 | [K104K15X7RF5TH5](https://www.mouser.com/c/?q=K104K15X7RF5TH5) |
| 470 µF electrolytic capacitor, radial | 1 | 1 | [UVR1E471MPD](https://www.mouser.com/c/?q=UVR1E471MPD) |
| 10 µF electrolytic capacitor, radial | 1 | 1 | [EEU-FR1H100](https://www.mouser.com/c/?q=EEU-FR1H100) |
| 220 µF electrolytic capacitor, radial | 1 | 2 | [EEU-FR1C221](https://www.mouser.com/c/?q=EEU-FR1C221) |
| Red 3 mm LED | 1 | 2 | [WP710A10ID](https://www.mouser.com/c/?q=WP710A10ID) |
| 1.5 A fast-blow fuse, 5 × 20 mm | 1 | 1 | [BK1/GMA-1.5-R](https://www.mouser.com/c/?q=BK1%2FGMA-1.5-R) |

Capacitor selections: K104K15X7RF5TH5 = 100 nF / 50 V ceramic, 5 mm lead spacing; UVR1E471MPD = 470 µF / 25 V, 10 mm diameter / 5 mm spacing; EEU-FR1H100 = 10 µF / 50 V, 5 mm diameter / 2 mm spacing; EEU-FR1C221 = 220 µF / 16 V, 6.3 mm diameter / 2.5 mm spacing. These nominal diameters and lead spacings match the current PCB constraints; confirm samples before PCB assembly. The 16 V / 25 V / 50 V markings are capacitor ratings, **not instructions to increase the power-supply voltage**.

For Q1–Q4 use the onsemi 2N3904BU TO-92 pinout, 1=emitter, 2=base, 3=collector. Do not rely on a generic photograph to orient another vendor's transistor.

## Connectors and module

Your module and breadboard connector breakouts can be reused. The bare PCB sockets below are for the later PCB or for soldering short insulated leads; their terminals do not necessarily plug into a solderless breadboard directly.

| Item | Keyboard | Full | Exact part — Mouser search |
|---|---:|---:|---|
| USB-A female, through-hole | 1 | 2 | [Molex 67643-3910](https://www.mouser.com/c/?q=67643-3910) |
| 7-pin DIN female, PCB-mounted | 1 | 2 | [Same Sky SDS-70J](https://www.mouser.com/c/?q=SDS-70J) |
| Two-contact PCB power terminal | 1 | 1 | [TE 282834-2](https://www.mouser.com/c/?q=282834-2); breadboard can use an insulated wired connection instead. |
| RP2040-Zero module | 1 | 1 | Reuse your module. No verified Mouser source for that exact hiBCTR module is provided. |

## Power, wiring and tools — Mouser search links

Select the specifications in the table; these are category/keyword searches, not individually approved products.

| Item | Quantity | Search | What to select |
|---|---|---|---|
| External regulated 5 V DC supply, at least 2 A | 1 | [Search](https://www.mouser.com/c/?q=5V+2A+regulated+AC+adapter) | Select fixed 5 V output, center-positive 5.5 × 2.1 mm plug for the adapter below. Keep the 1.5 A circuit fuse. |
| Matching power adapter to insulated wires | 1 | [Search](https://www.mouser.com/c/?q=2.1mm+female+DC+power+pigtail) | Connect through the fuse holder to J1; meter-check polarity. A pigtail is cable hardware, not an extra electronic module. |
| Inline fuse holder, 5 × 20 mm | 1 | [Search](https://www.mouser.com/c/?q=5x20+inline+fuse+holder) | Must accept the selected fuse; rated at least 2 A and 5 V DC. |
| Solderless breadboard | 1 large board; another if crowded | [Search](https://www.mouser.com/c/?q=solderless+breadboard) | Already shown in your photo; buy only if more space is needed. |
| 22 AWG solid-core hookup wire / short jumper leads | 1 assortment | [Search](https://www.mouser.com/c/?q=22+AWG+solid+hookup+wire) | Keep USB data wires short; use suitable heavier leads for the external supply. |
| 2.54 mm single-row male headers | 2 × 9 pins + 1 × 5 pins | [Search](https://www.mouser.com/c/?q=2.54mm+single+row+breakaway+male+header) | Only if the RP2040-Zero does not already have headers. A 40-pin strip can be cut to length. |
| Removable module-power jumper, JP1 | 1 | [Search](https://www.mouser.com/c/?q=breadboard+jumper+wires) | A short removable jumper wire works on the breadboard. |
| 7-pin DIN male cable plug | 1 keyboard / 2 full | [Search](https://www.mouser.com/c/?q=7+pin+DIN+male+cable+connector) | Match the physical pin pattern of your existing socket; generic 7-pin connectors are not automatically interchangeable. |
| PS/2 cable with 6-pin mini-DIN male end | 1 keyboard / 2 full | [Search](https://www.mouser.com/c/?q=6+pin+mini+DIN+male+cable) | For the custom output cable; identify conductors by continuity, not color. An extension cable can supply a male-ended cable section. |
| Cable finishing materials | Enough for 1 / 2 cables | [Search](https://www.mouser.com/c/?q=heat+shrink+tubing) | Four insulated conductors per custom PS/2 cable; add cable if the PS/2 cable section is too short. |
| USB-C data cable | 1 | [Search](https://www.mouser.com/c/?q=USB+C+data+cable) | Use for programming the module; remove JP1 before connecting the PC. |
| Multimeter with DC voltage and continuity | 1 | [Search](https://www.mouser.com/c/?q=digital+multimeter+continuity) | Skip if you have one. |

For the later PCB only: one DIP-8 socket and one DIP-16 socket (both 7.62 mm row spacing), two 1×9 plus one 1×5 female module sockets at 2.54 mm pitch, a two-pin header/shunt for JP1, the matching pair of Littelfuse 111-series fuse clips, and four sets of M3 insulating mounting hardware. Follow [PCB purchasing notes](hardware/rev-d/parts.md) before ordering those. The 26 PCB test holes do not need purchased test points.

A paired USB keyboard/receiver and later a mouse/receiver are needed for testing; keep your existing peripherals. Receiver compatibility depends on firmware.

## Specification sources

- [TI TPS2042P package details](https://www.ti.com/product/TPS2042/part-details/TPS2042P) — exact PDIP power-switch part.
- [CD4050BE at Mouser](https://www.mouser.ca/ProductDetail/Texas-Instruments/CD4050BE?qs=j%2FZo4ajzVJLKLpJvKsajlg%3D%3D) — DIP buffer.
- [YAGEO 22 Ω selection](https://www.mouser.com/ProductDetail/YAGEO/MFR-25FBF52-22R?qs=oAGoVhmvjhx96aHnODh%2FLA%3D%3D) and [15 kΩ selection](https://www.mouser.com/ProductDetail/YAGEO/MFR-25FBF52-15K?qs=oAGoVhmvjhzZTLCD9uq%2F7w%3D%3D) — axial ¼ W, 1%.
- [100 nF ceramic](https://www.mouser.com/ProductDetail/Vishay-BC-Components/K104K15X7RF5TH5?qs=CuWZN%2F5Vbiofhf%252BuZNGw%2Fg%3D%3D).
- [470 µF capacitor](https://www.mouser.com/ProductDetail/Nichicon/UVR1E471MPD?qs=eBzRnwgjaQf16mhkgyDt6A%3D%3D), [10 µF capacitor](https://www.mouser.ca/en/ProductDetail/Panasonic-Industry/EEU-FR1H100?qs=tfZGHB2PWd1NAbdNSgjToQ%3D%3D), [220 µF capacitor](https://www.mouser.co.uk/en/ProductDetail/Panasonic-Industry/EEU-FR1C221?qs=sGAEpiMZZMsh%252B1woXyUXj1qMLSoXX8Md3jdDfI7Gxc0%3D).
- [1.5 A fast fuse](https://www.mouser.com/ProductDetail/Eaton-Electronics/BK1-GMA-1.5-R?qs=9GX7soZQXxHHwQMtPHv6gQ%3D%3D).

Researched 2026-09-17. These are component selections for an untested prototype, not a statement that the finished adapter has passed hardware testing.
