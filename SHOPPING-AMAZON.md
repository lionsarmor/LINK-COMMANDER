# LINK COMMANDER Rev D — exact Amazon order

**Recommended purchase: order the main table below plus the main table in [SHOPPING-MOUSER.md](SHOPPING-MOUSER.md).** I selected the circuit components, regulated power supply, fuse holder and DIN cable plugs from Mouser. Amazon supplies the wire and cables here. There are no keyword-search links.

Each **ASIN** is Amazon's exact product identifier. Order one of each required listing, unless you already have that item. Quantities below cover both keyboard and mouse; they also cover a keyboard-first build.

## Buy these supplies

| Buy quantity | Exact product — direct Amazon link | ASIN | What it supplies |
|---:|---|---|---|
| 1 kit | [TUOFENG 22 AWG solid-core wire, six colors](https://www.amazon.com/dp/B07TX6BX47) | B07TX6BX47 | Breadboard connections, short power leads and the removable JP1 jumper. Cut USB data leads short. |
| 1 cable | [JUXINICE 6 ft PS/2 male-to-male cable](https://www.amazon.com/dp/B0933GL5CX) | B0933GL5CX | Cut in half to obtain **two approximately 3 ft male-ended PS/2 cable sections**, one keyboard and one mouse. Solder an SDR-70 DIN plug from the Mouser list to each cut end using the Rev D pin table. |
| 1 kit | [Ginsco 580-piece heat-shrink tubing assortment](https://www.amazon.com/dp/B01MFA3OFA) | B01MFA3OFA | Insulate soldered cable and power-wire joints; choose a size that shrinks firmly around each joint. |
| 1 cable, if missing | [Anker PowerLine USB-A to USB-C data cable, 10 ft](https://www.amazon.com/dp/B01MZIPYPY) | B01MZIPYPY | Programming connection from a computer with USB-A to the RP2040-Zero. Reuse an existing data-capable cable if you have one; remove JP1 before plugging into the computer. |

## Only if you do not already have these

| Buy quantity | Exact product — direct Amazon link | ASIN | Purpose |
|---:|---|---|---|
| 1 meter | [AstroAI AM33D digital multimeter](https://www.amazon.com/dp/B01ISAMUA6) | B01ISAMUA6 | DC voltage, resistance and cable continuity checks for the breadboard. |
| 1 board | [Qunqi 400-contact solderless breadboard](https://www.amazon.com/dp/B0135IQ0ZC) | B0135IQ0ZC | Extra space beside the breadboard in your photo, if needed. This is an expansion board, not a replacement for your existing large board. |

Reuse your RP2040-Zero and USB/DIN connector breakouts. Your module listing is [hiBCTR RP2040-Zero — B0DXL12W59](https://www.amazon.com/dp/B0DXL12W59); your DIN board listing is [Treedix 4-pack — B0B11JZ1F3](https://www.amazon.com/dp/B0B11JZ1F3). Neither is a required repeat purchase. The final PCB still uses directly soldered sockets.

Cable assembly also uses your soldering iron, electronics solder, wire stripper/cutter and a suitable heat source for the heat-shrink. These are bench tools, not circuit parts. The solderless breadboard itself does not need soldering, but the custom cable joints do.

## Optional Amazon substitutes — skip when buying the recommended Mouser order

These are specific listings, provided for Amazon alternatives to some Mouser parts. They duplicate items in the main order; **do not buy both**. I could not verify suitable Amazon listings for the two exact DIP chips, so buy those from Mouser.

| Buy quantity | Exact product — direct Amazon link | ASIN | Replaces these Mouser order items |
|---:|---|---|---|
| 1 kit | [BOJACK 1,350-piece, 50-value resistor kit](https://www.amazon.com/dp/B07P3MFG5D) | B07P3MFG5D | All six resistor rows. Full build uses 4 × 22 Ω, 4 × 15 kΩ, 6 × 2.2 kΩ, 4 × 47 kΩ, 4 × 4.7 kΩ, 4 × 100 kΩ. Listing specifies 1%, ¼ W axial metal-film parts. |
| 1 kit | [BOJACK 630-piece radial electrolytic capacitor kit](https://www.amazon.com/dp/B07PBQXQNQ) | B07PBQXQNQ | Electrolytic rows only: 1 × 10 µF, 2 × 220 µF, 1 × 470 µF, rated at least 10 V. Still buy the separate 100 nF ceramics. These assortment parts are for the breadboard; dimensions may differ from the PCB footprints. |
| 1 kit | [BOJACK 5×20 inline fuse holders and fast-blow fuse assortment](https://www.amazon.com/dp/B0813Q4S6P) | B0813Q4S6P | Both the fuse-holder and fuse rows. Use one holder and **one 1.5 A fast-blow fuse** from the kit. |
| 1 pack | [DAYKIT 5.5×2.1 mm male/female screw-terminal adapters](https://www.amazon.com/dp/B01J1WZENK) | B01J1WZENK | Adafruit 368 adapter only. Use **one female** adapter with the selected 5 V power supply. The listing's “12V” label does not change the circuit's 5 V supply requirement. |

The recommended Mouser order CSV does not automatically remove these optional substitutes. The simplest purchase is the two main tables without this optional section.

Listings were inspected on 2026-09-17; no stock or delivery date is guaranteed. Assembly instructions: [BREADBOARD.md](BREADBOARD.md). Buying and wiring the parts does not replace the pending firmware and bench tests.
