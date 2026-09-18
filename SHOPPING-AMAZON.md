# LINK COMMANDER Rev D — Amazon breadboard shopping list

**Choose this list OR the Mouser list. Do not buy both lists.** This document covers the entire breadboard checklist, including parts you already own. Each Amazon link is a specific listing, with its ASIN beside it.

**Amazon-only sourcing is not complete:** I could not verify purchasable Amazon listings for the two exact DIP chips, **TPS2042P and CD4050BE**. Both are required. Their exact Mouser links are provided below as the only two required outside-store purchases in this checklist. Do not substitute similarly numbered chips. The Amazon purchases alone cannot complete the circuit.

## Buy once per listing

Quantities below cover both keyboard and mouse. The packs also cover keyboard-only; use the installed-quantity table below to pick parts from them. Skip supplies already on your bench.

| Buy quantity | Product — direct Amazon link | ASIN | What to use |
|---|---|---|---|
| 1 kit | [BOJACK 50-value, 1,350-piece resistor assortment](https://www.amazon.com/dp/B07P3MFG5D) | B07P3MFG5D | All six required 1%, ¼ W axial resistor values; installed quantities below. |
| 1 kit | [BOJACK 630-piece radial electrolytic assortment](https://www.amazon.com/dp/B07PBQXQNQ) | B07PBQXQNQ | C1: 1 × 470 µF; C2: 1 × 10 µF; C5/C7: 2 × 220 µF. Choose ratings ≥10 V. |
| 1 kit | [BOJACK 15-value leaded ceramic assortment](https://www.amazon.com/dp/B07P8N8BW9) | B07P8N8BW9 | C3/C4/C6/C8: 4 × 100 nF (104), 50 V. Keyboard-only uses 3. |
| 1 kit | [BOJACK 10-type TO-92 transistor assortment](https://www.amazon.com/dp/B07T61SY9Y) | B07T61SY9Y | Use only the 2N3904 parts: 2 for keyboard, 4 full. Other transistor types are not substitutes. |
| 1 kit | [300-piece 3 mm / 5 mm LED assortment](https://www.amazon.com/dp/B0F38LJDJB) | B0F38LJDJB | Choose the plain 3 mm red LEDs: 1 keyboard, 2 full; retain circuit resistors. |
| 1 kit | [BOJACK 5×20 inline holders and fast-fuse assortment](https://www.amazon.com/dp/B0813Q4S6P) | B0813Q4S6P | Use 1 holder and 1 × 1.5 A fast fuse for either build. Other fuse values stay unused. |
| 1 supply | [ALITOVE fixed 5 V / 3 A supply with female screw-terminal adapter](https://www.amazon.com/dp/B078RXZM4C) | B078RXZM4C | External supply AND J1 breadboard power connection. Included adapter avoids a separate barrel-adapter purchase. |
| 1 pack | [JING three sets of full-size 7-pin DIN cable plugs / panel sockets](https://www.amazon.com/dp/B0978QLHVD) | B0978QLHVD | Use 1 male plug keyboard, 2 full. Female panel sockets are spare; reuse your DIN breakouts. These are not the PCB-mounted SDS-70J sockets. |
| 1 cable | [JUXINICE 6 ft PS/2 male-to-male cable](https://www.amazon.com/dp/B0933GL5CX) | B0933GL5CX | Cut in half: two approximately 3 ft male-ended sections for the custom keyboard/mouse cables. |
| 1 kit | [TUOFENG 22 AWG solid-core wire, six colors](https://www.amazon.com/dp/B07TX6BX47) | B07TX6BX47 | Breadboard wiring, short power leads and removable JP1 wire. |
| 1 pack | [ELEGOO male/female jumper-wire assortment](https://www.amazon.com/dp/B01EV70C78) | B01EV70C78 | Reach the module end-header pins; use short solid-core wiring for USB data. |
| 1 kit | [Ginsco heat-shrink assortment](https://www.amazon.com/dp/B01MFA3OFA) | B01MFA3OFA | Insulate the cable and power joints. |
| 1 if missing | [Anker USB-A to USB-C data cable](https://www.amazon.com/dp/B01MZIPYPY) | B01MZIPYPY | Programming cable; reuse a data-capable cable if owned. |

**Download:** [Amazon order CSV](SHOPPING-AMAZON-ORDER.csv), including the two clearly labeled Mouser exceptions and the already-owned replacement items.

## Required chips — outside-store exceptions

Both chips are needed even for keyboard-only. These are individually ordered parts, not assortments.

| Buy | Part / package | Exact Mouser SKU — direct product link | Reference |
|---:|---|---|---|
| 1 | TPS2042P, DIP-8 | [595-TPS2042P](https://www.mouser.com/en/ProductDetail/Texas-Instruments/TPS2042P?qs=sGAEpiMZZMv0DJfhVcWlK5dti4XbSOwogfbpZrAIrQU%3D) | U1 |
| 1 | CD4050BE, DIP-16 | [595-CD4050BE](https://www.mouser.com/en/ProductDetail/Texas-Instruments/CD4050BE?qs=j%2FZo4ajzVJLKLpJvKsajlg%3D%3D) | U2 |

Order these two exact parts in addition to the Amazon purchases. No verified Amazon purchase link is available for them.

## Already-owned items and replacements

These are part of the complete build even if you do not need to buy them again.

| Buy quantity | Product — direct Amazon link | ASIN | What to use |
|---|---|---|---|
| 1 module; already owned | [hiBCTR RP2040-Zero](https://www.amazon.com/dp/B0DXL12W59) | B0DXL12W59 | M1. Reuse your existing module. |
| 1 kit if missing | [yddmyo 14-piece USB connector breakout kit](https://www.amazon.com/dp/B0D7676X4L) | B0D7676X4L | Includes two USB 2.0 Type-A female boards: one bare-header style and one terminal style. Use those two only; reuse your existing USB boards instead if available. |
| 1 pack if missing | [Treedix four 7-pin DIN socket breakout boards](https://www.amazon.com/dp/B0B11JZ1F3) | B0B11JZ1F3 | J4/J5: use 1 keyboard, 2 full. You already own these; breadboard use only. |
| 4 boards if starting empty | [Qunqi 400-contact solderless breadboard](https://www.amazon.com/dp/B0135IQ0ZC) | B0135IQ0ZC | Four half-size boards provide room for the full build. With your existing large board, buy only any expansion space needed. |
| 1 pack if headers missing | [OCR 40-pin straight 2.54 mm male/female header assortment](https://www.amazon.com/dp/B0774VBJ3J) | B0774VBJ3J | Use male strips: cut 9 + 9 + 5 for M1. One extra 4-pin piece can serve the bare USB breakout. Reuse fitted headers. |
| 1 if missing | [AstroAI AM33D multimeter](https://www.amazon.com/dp/B01ISAMUA6) | B01ISAMUA6 | DC voltage, resistance and continuity checks. |

## Installed circuit quantities — pick these from the packs above

Buying one resistor kit covers all six resistor rows; do not order six kits. The same applies to the three electrolytic rows. Each reference below is accounted for once.

| Circuit part | Keyboard only | Full build | References | Source / SKU |
|---|---:|---:|---|---|
| Two-contact 5 V power connection | 1 | 1 | J1 | Included screw adapter: [B078RXZM4C](https://www.amazon.com/dp/B078RXZM4C) |
| 1.5 A fast fuse, 5×20 mm | 1 | 1 | F1 | 1.5 A fuse from kit: [B0813Q4S6P](https://www.amazon.com/dp/B0813Q4S6P) |
| Removable module-power jumper | 1 | 1 | JP1 | Removable wire: [B07TX6BX47](https://www.amazon.com/dp/B07TX6BX47) |
| RP2040-Zero module on headers | 1 | 1 | M1 | Existing module: [B0DXL12W59](https://www.amazon.com/dp/B0DXL12W59) |
| 470 µF / 10 V electrolytic capacitor | 1 | 1 | C1 | Electrolytic kit: [B07PBQXQNQ](https://www.amazon.com/dp/B07PBQXQNQ) |
| 10 µF / 10 V electrolytic capacitor | 1 | 1 | C2 | Electrolytic kit: [B07PBQXQNQ](https://www.amazon.com/dp/B07PBQXQNQ) |
| 100 nF leaded ceramic capacitor | 3 | 4 | C3 C4 C6 C8 | Ceramic kit: [B07P8N8BW9](https://www.amazon.com/dp/B07P8N8BW9) |
| USB-A receptacle, keyboard | 1 | 1 | J2 | Existing USB board or kit: [B0D7676X4L](https://www.amazon.com/dp/B0D7676X4L) |
| TPS2042P dual power switch, DIP-8 | 1 | 1 | U1 | **Mouser** [595-TPS2042P](https://www.mouser.com/en/ProductDetail/Texas-Instruments/TPS2042P?qs=sGAEpiMZZMv0DJfhVcWlK5dti4XbSOwogfbpZrAIrQU%3D) |
| 22 Ω resistor | 2 | 4 | R1 R2 R6 R7 | Resistor kit: [B07P3MFG5D](https://www.amazon.com/dp/B07P3MFG5D) |
| 15 kΩ resistor | 2 | 4 | R3 R4 R8 R9 | Resistor kit: [B07P3MFG5D](https://www.amazon.com/dp/B07P3MFG5D) |
| 2.2 kΩ resistor | 3 | 6 | R5 R10 R11 R15 R19 R23 | Resistor kit: [B07P3MFG5D](https://www.amazon.com/dp/B07P3MFG5D) |
| 220 µF / 10 V electrolytic capacitor | 1 | 2 | C5 C7 | Electrolytic kit: [B07PBQXQNQ](https://www.amazon.com/dp/B07PBQXQNQ) |
| Red LED, 3 mm | 1 | 2 | D1 D2 | 3 mm red LEDs: [B0F38LJDJB](https://www.amazon.com/dp/B0F38LJDJB) |
| USB-A receptacle, mouse | 0 | 1 | J3 | Existing USB board or kit: [B0D7676X4L](https://www.amazon.com/dp/B0D7676X4L) |
| 7-pin DIN socket, keyboard (SDS-70J for PCB) | 1 | 1 | J4 | Existing DIN board: [B0B11JZ1F3](https://www.amazon.com/dp/B0B11JZ1F3) |
| 7-pin DIN socket, mouse (SDS-70J for PCB) | 0 | 1 | J5 | Existing DIN board: [B0B11JZ1F3](https://www.amazon.com/dp/B0B11JZ1F3) |
| 2N3904 transistor, TO-92 | 2 | 4 | Q1 Q2 Q3 Q4 | 2N3904 from kit: [B07T61SY9Y](https://www.amazon.com/dp/B07T61SY9Y) |
| 47 kΩ resistor | 2 | 4 | R12 R16 R20 R24 | Resistor kit: [B07P3MFG5D](https://www.amazon.com/dp/B07P3MFG5D) |
| 4.7 kΩ resistor | 2 | 4 | R13 R17 R21 R25 | Resistor kit: [B07P3MFG5D](https://www.amazon.com/dp/B07P3MFG5D) |
| 100 kΩ resistor | 2 | 4 | R14 R18 R22 R26 | Resistor kit: [B07P3MFG5D](https://www.amazon.com/dp/B07P3MFG5D) |
| CD4050BE buffer, DIP-16 | 1 | 1 | U2 | **Mouser** [595-CD4050BE](https://www.mouser.com/en/ProductDetail/Texas-Instruments/CD4050BE?qs=j%2FZo4ajzVJLKLpJvKsajlg%3D%3D) |

## Your proposed replacements

| Product | Decision | Reason |
|---|---|---|
| [SQXBK fuse clips — B09XMSVQTJ](https://www.amazon.com/dp/B09XMSVQTJ) | **Skip for this build.** | They hold **6×30 mm** fuses. Rev D uses **5×20 mm**. They also are not a verified match for the PCB's clip footprint. The inline holder above is easier to wire on a breadboard. |
| [Tugermoola panel-mount jack kit — B0DP6MNQQB](https://www.amazon.com/dp/B0DP6MNQQB) | **Suitable optional enclosure jack; not required.** | 5.5×2.1 mm, prewired 20 AWG leads, listing rating 5 A / 50 V. Use one female jack instead of the screw adapter if mounting in a panel. It is not a PCB drop-in connector. |

For the optional panel jack, identify center-pin and outer-barrel leads by continuity before wiring. Center-positive goes through the **1.5 A fuse** to J1.1, outer barrel to J1.2/common ground. Splice its stranded wires to short solid-core breadboard leads and insulate them. Keep the supply at **5 V**; “50 V” is a connector rating.

The listed ALITOVE supply already includes a female screw-terminal adapter. For the simplest breadboard purchase, use that adapter and skip the separate panel-jack kit and DAYKIT adapter pack.

## Assembly details that affect the purchase

- Cut the PS/2 male-to-male cable in half. Solder one 7-pin male plug onto each section following the custom-cable pin table. Check DIN plug fit before soldering; the JING listing photo shows the standard full-size seven-contact pattern, but no sample-fit test has been done. The kit's panel sockets do not replace the PCB-mounted SDS-70J parts.
- Use the plugs' cable clamps/boots for strain relief. Continuity-test conductors to numbered PS/2 contacts; colors are not standardized.
- The BOJACK transistor pack contains several types with different pinouts. Select **2N3904**, and verify emitter/base/collector against the supplied part information before installation.
- Amazon assortment capacitors are selected for the breadboard. Their body dimensions and lead spacing are not verified for the later PCB; use the Mouser individual selections for known nominal PCB dimensions.
- There is no separate radio board to buy: the keyboard/mouse receivers provide the wireless link.

## What this order covers

This is the **Rev D keyboard-and-mouse breadboard**, including its external power supply and two custom cables to the X16. It covers every electrical position in [BREADBOARD-PARTS.csv](BREADBOARD-PARTS.csv). Keyboard-only quantities are an alternative to full-build quantities; do not add them together. All circuit components are through-hole except the assembled RP2040-Zero module. Passive connector breakouts are for breadboarding only.

Have a soldering iron, electronics solder, wire stripper/cutter, small screwdriver and suitable heat source for heat-shrink available. These workshop tools are not included in the component order. The multimeter is listed. The later firmware validation also requires access to a suitable logic analyzer, preferably an oscilloscope, and a computer. Reuse your keyboard, mouse, paired USB receivers and Commander X16; peripheral compatibility is still subject to testing.

This is **not a complete PCB assembly order**. The later carrier adds DIP sockets, female module sockets, PCB fuse clips, JP1 header/shunt, mounting hardware and the fabricated PCB; see [PCB parts](hardware/rev-d/parts.md). The 26 PCB test holes do not require purchased components for this breadboard.

Follow [BREADBOARD.md](BREADBOARD.md), including polarity/continuity checks and removing JP1 before connecting the module to the programming computer. Firmware and physical validation remain pending. Listings were reviewed September 18, 2026; stock, seller and delivery can change.
