# LINK COMMANDER Rev D — breadboard wiring and parts

**Buy the parts:** [Amazon products + ASINs](SHOPPING-AMAZON.md) · [Mouser products + SKUs](SHOPPING-MOUSER.md) · [Full Mouser order CSV](SHOPPING-MOUSER-ORDER.csv) · [Keyboard-only Mouser CSV](SHOPPING-MOUSER-KEYBOARD.csv). The two main shopping tables form one combined order; reuse the parts marked already owned.

**Build the keyboard half first, then add the mouse.** This guide is for
Rev D: RP2040-Zero module, two USB inputs, two 7-pin DIN outputs, and an
external regulated 5 V supply. It does not include gamepad circuitry.

The parts list is included below and attached as
[BREADBOARD-PARTS.csv](BREADBOARD-PARTS.csv). The complete Rev D connection
list is [BREADBOARD-WIRING.csv](BREADBOARD-WIRING.csv). Open the
[one-page schematic](hardware/rev-d/review/schematic.pdf) alongside this guide.

**Firmware is still required.** Wiring the board alone will not translate
USB into PS/2. Leave the X16 disconnected until the standalone electrical
and firmware tests below have passed.

## 1. Gather the parts

“Keyboard first” is the starting quantity. “Add mouse” is the extra quantity,
not a replacement. All parts except the assembled RP2040-Zero module are
through-hole. The following table covers the 50 electrical positions in
the full circuit; tools, leads and cable parts are listed afterward.

<!-- BEGIN GENERATED BREADBOARD PARTS -->
| Keyboard first | Add mouse | Full total | Part / value | References |
|---:|---:|---:|---|---|
| 1 | 0 | 1 | Two-contact 5 V power connection | J1 |
| 1 | 0 | 1 | 1.5 A fast fuse, 5×20 mm | F1 |
| 1 | 0 | 1 | Removable module-power jumper | JP1 |
| 1 | 0 | 1 | RP2040-Zero module on headers | M1 |
| 1 | 0 | 1 | 470 µF / 10 V electrolytic capacitor | C1 |
| 1 | 0 | 1 | 10 µF / 10 V electrolytic capacitor | C2 |
| 3 | 1 | 4 | 100 nF leaded ceramic capacitor | C3 C4 C6 C8 |
| 1 | 0 | 1 | USB-A receptacle, keyboard | J2 |
| 1 | 0 | 1 | TPS2042P dual power switch, DIP-8 | U1 |
| 2 | 2 | 4 | 22 Ω resistor | R1 R2 R6 R7 |
| 2 | 2 | 4 | 15 kΩ resistor | R3 R4 R8 R9 |
| 3 | 3 | 6 | 2.2 kΩ resistor | R5 R10 R11 R15 R19 R23 |
| 1 | 1 | 2 | 220 µF / 10 V electrolytic capacitor | C5 C7 |
| 1 | 1 | 2 | Red LED, 3 mm | D1 D2 |
| 0 | 1 | 1 | USB-A receptacle, mouse | J3 |
| 1 | 0 | 1 | 7-pin DIN socket, keyboard (SDS-70J for PCB) | J4 |
| 0 | 1 | 1 | 7-pin DIN socket, mouse (SDS-70J for PCB) | J5 |
| 2 | 2 | 4 | 2N3904 transistor, TO-92 | Q1 Q2 Q3 Q4 |
| 2 | 2 | 4 | 47 kΩ resistor | R12 R16 R20 R24 |
| 2 | 2 | 4 | 4.7 kΩ resistor | R13 R17 R21 R25 |
| 2 | 2 | 4 | 100 kΩ resistor | R14 R18 R22 R26 |
| 1 | 0 | 1 | CD4050BE buffer, DIP-16 | U2 |
<!-- END GENERATED BREADBOARD PARTS -->

For a breadboard, J1 can be an insulated supply connection and F1 can use
an inline 5×20 fuse holder. JP1 can be a clearly labeled removable jumper
wire. These serve the same connections as their PCB counterparts.

Also gather:

| Item | Keyboard first | Add mouse | Notes |
|---|---:|---:|---|
| Regulated 5 V / 2 A supply | 1 | 0 | A current-limited bench supply is useful for first power-up |
| 5×20 fuse holder | 1 | 0 | For F1; not an unfused wire link |
| Solderless breadboard | 1 large board to start | As needed | Use another board if the USB/PS/2 wiring becomes crowded |
| Solid-core jumper wire and short hookup leads | Assortment | As needed | Check continuity across split breadboard rails |
| Module male headers, 2.54 mm | Two 1×9 and one 1×5 | 0 | Only if your module does not already have them fitted |
| 7-pin DIN male cable plug | 1 | 1 | Matches your output socket |
| 6-pin mini-DIN PS/2 male cable or plug | 1 | 1 | Four conductors used; continuity-test the numbered contacts |
| Insulated cable, heat-shrink and strain relief | 1 cable's worth | 1 cable's worth | Or adapt a checked PS/2 cable |
| USB receiver and its paired peripheral | Keyboard set | Mouse set | Or a wired USB keyboard/mouse for initial firmware testing |
| USB-C data cable to the computer | 1 | 0 | For programming the module; remove JP1 first |
| Multimeter | 1 | 0 | Power and cable continuity checks |
| Suitable logic analyzer; preferably an oscilloscope too | 1 setup | 0 | Logic timing and signal-edge tests |

Your existing USB and DIN connector breakouts can hold the sockets during
breadboarding; they contain no extra controller chips. Alternatively,
solder short insulated leads to the sockets. The final PCB uses sockets
mounted directly on the board. No USB hub is used.

DIP sockets, module female sockets, PCB fuse clips and mounting hardware
are for the later PCB assembly; see
[PCB purchasing notes](hardware/rev-d/parts.md). The 26 PCB test holes do
not require 26 extra breadboard parts: probe the corresponding named nets.

Use 1% axial 0.25 W resistors and leaded capacitors. Electrolytics are rated
at least 10 V. Confirm lead spacing against the PCB purchasing notes if
buying the same parts for both builds.

## 2. Identify the pins and lay out the breadboard

Place U1 and U2 across the breadboard's center gap. DIP pin numbering is
viewed from above: with the notch at the top, pin 1 is upper left; count
down the left side and then up the right side.

- **U1 is TPS2042P, DIP-8.** TPS2041P has a different pinout; TPS2052 has
  the opposite enable polarity.
- **U2 is CD4050BE, DIP-16. Pin 1 is power and pin 8 is ground.**
  Pins 13 and 16 are unused; do not connect pin 16 to power.
- Q1–Q4 are 2N3904: the design expects physical pin **1 = emitter,
  2 = base, 3 = collector**. Check the actual manufacturer's pinout.
- On the RP2040-Zero, follow the printed **GP0, GP1, etc.** labels.
  M1 numbers in the CSV identify carrier contacts, not GPIO numbers or
  breadboard rows. Do not use underside module pads.

The module's end header is offset from the side headers' breadboard grid.
Use short leads to the end contacts instead of forcing all three rows into
incompatible holes. Keep the USB data pair wiring short, with its 22 Ω
resistors near the module. Use short, substantial supply/ground leads;
do not route the combined receiver load through long breadboard rails.

Label these separate nets before wiring: **5V_BOARD, 5V_MODULE, 3V3,
USB1_5V, USB2_5V, KBD_5V, MOUSE_5V and GND**. Equal net names mean a
connection; different power names are not interchangeable.

## 3. Wire shared power and both chips

Make these connections with power off and no X16 cable connected.

| Connection | Wire it this way |
|---|---|
| External supply positive | J1.1 → F1 → **5V_BOARD** |
| External supply negative | J1.2 → **GND** |
| Module supply jumper | **5V_BOARD** → JP1 → module **5V**, net **5V_MODULE** |
| Module ground | Module **GND** → common **GND** |
| Module regulator output | Module **3V3** → U2 pin **1** |
| U2 ground | U2 pin **8** → **GND** |
| U1 input | U1 pin **2** → **5V_BOARD** |
| U1 ground and enables | U1 pins **1, 3 and 4** → **GND** |
| C1, 470 µF | Positive → **5V_BOARD**; negative → **GND** |
| C2, 10 µF | Positive → **3V3**; negative → **GND** |
| C3, 100 nF | Between U2 pin **1** and **GND**, close to U2 |
| C4, 100 nF | Between U1 pin **2** and **GND**, close to U1 |

**For the first keyboard-only build:** ground U2 pins **7, 9, 11 and 14**.
Leave U2 pins **6, 10, 12, 13, 15 and 16** unconnected. Pins 7 and 9 are
temporary grounds that must be removed when adding the mouse.
Leave unused U1 mouse output pin 6 and fault pin 5 open for this first stage.

Both U1 power channels are always enabled. Neither the firmware nor a
module reset switches receiver power off.

**Programming:** remove JP1 before plugging the module's USB-C into the
computer. The PC then powers the module and U2; the external 5 V supply
still powers the USB receiver sockets. For standalone operation, disconnect
PC USB and reinstall JP1 with power off.

## 4. Wire the keyboard USB input

J2 is a USB-A receptacle. Use its printed breakout labels or verified
connector contact numbers, not a guessed left-to-right view.

| Part/contact | Connection |
|---|---|
| J2 pin 1, VBUS | U1 pin **7**, net **USB1_5V** |
| J2 pin 2, D− | R2 → module **GP1** |
| J2 pin 3, D+ | R1 → module **GP0** |
| J2 pin 4, GND | **GND** |
| J2 shield contacts | **GND**; local PCB pad number 5 |
| R1, 22 Ω | GP0 ↔ J2 D+ |
| R2, 22 Ω | GP1 ↔ J2 D− |
| R3, 15 kΩ | J2 D+ ↔ **GND** |
| R4, 15 kΩ | J2 D− ↔ **GND** |
| C5, 220 µF | Positive → **USB1_5V**; negative → **GND** |
| C6, 100 nF | **USB1_5V** ↔ **GND**, close to J2 |
| R5, 2.2 kΩ | **5V_BOARD** → D1 anode |
| D1 red LED | Anode → R5; cathode → U1 pin **8** |

D1 indicates a USB power fault, not USB activity. Keep the receiver
unplugged until the initial power measurements pass.

## 5. Wire the keyboard PS/2 output

Build the following circuit twice, once for DATA and once for CLOCK.
Each resistor appears once; entries in different columns describe its
complete connection rather than additional components.

| Connection | Keyboard DATA | Keyboard CLOCK |
|---|---|---|
| Drive GPIO through 2.2 kΩ to base | GP8 → R11 → Q1 pin 2 | GP10 → R15 → Q2 pin 2 |
| Base to GND through 47 kΩ | Q1 pin 2 → R12 → GND | Q2 pin 2 → R16 → GND |
| Transistor emitter | Q1 pin 1 → GND | Q2 pin 1 → GND |
| Transistor collector / cable line | Q1 pin 3 = **KBD_DATA** | Q2 pin 3 = **KBD_CLOCK** |
| 4.7 kΩ pull-up | KBD_5V → R13 → KBD_DATA | KBD_5V → R17 → KBD_CLOCK |
| 100 kΩ line pulldown | KBD_DATA → R14 → GND | KBD_CLOCK → R18 → GND |
| Buffer input | KBD_DATA → U2 pin **3** | KBD_CLOCK → U2 pin **5** |
| Buffer output to sense GPIO | U2 pin **2** → **GP9** | U2 pin **4** → **GP11** |
| Output socket J4 | KBD_DATA → J4 contact **3** | KBD_CLOCK → J4 contact **4** |

J4 contact **1** is **KBD_5V**, supplied by the X16 cable only when attached
to a powered X16. J4 contact **2** is **GND**. Leave contacts 5, 6, 7 and
the shell unconnected.

Drive GPIO HIGH pulls its cable line LOW. Drive GPIO LOW releases it.
The sense GPIO reads the actual cable level without inversion.
**Do not connect a 5 V cable signal directly to a module GPIO.**

## 6. Make and check the custom PS/2 cable

The mapping is the same for both outputs. J4 goes to the X16 keyboard port;
J5, added later, goes to its mouse port.

| Adapter 7-pin DIN contact | PS/2 6-pin mini-DIN contact | Signal |
|---:|---:|---|
| 1 | 4 | X16 +5 V reference |
| 2 | 3 | GND |
| 3 | 1 | DATA |
| 4 | 5 | CLOCK |
| 5, 6, 7 and shell | None | Leave unconnected |

Leave PS/2 contacts 2 and 6 unconnected. The front and solder-side views
are mirrored. Identify numbered contacts from the connector drawing and
continuity-test each wire; do not trust insulation colors. Your existing
DIN breakout's terminal numbers must be checked against the actual socket
contacts. Its shield terminal is not a seventh signal contact.

The PS/2 +5 V reference must stay separate from the external **5V_BOARD**
rail. Grounds are common. Keep the cable disconnected from the X16 for now.

## 7. Check the keyboard build before connecting the X16

1. With power off, check for supply-to-ground shorts, LED/capacitor polarity,
   transistor orientation, DIP pin numbers and cable continuity.
2. Apply external regulated 5 V, preferably using a current-limited supply.
   Check approximately 5 V at U1 pin 2 and J2 VBUS, and 3.3 V at U2 pin 1.
   Under the intended receiver load, verify J2 VBUS stays within 4.75–5.25 V.
3. For GPIO tests with the X16 disconnected, temporarily connect **KBD_5V**
   to the bench's regulated 5 V reference. Use test firmware to check that
   drive HIGH gives cable/sense LOW and drive LOW allows cable/sense HIGH.
   **Remove that temporary reference jumper before attaching the X16.**
4. Test USB receiver enumeration and decoded keyboard reports. Then test
   PS/2 framing, reset responses, acknowledgments and host-clock inhibit
   on a suitable fixture. The firmware requirements are in
   [firmware-contract.md](hardware/rev-d/firmware-contract.md).
5. Only after those tests pass, power off, attach the checked keyboard
   cable to the X16 and start the keyboard test.

These are instructions for tests still to be performed. The repository
contains preliminary SPICE results, not a working bridge/test application.
The [test-point guide](hardware/rev-d/test-points.md) identifies equivalent
breadboard probe nodes. Use sense GPIOs for a 3.3 V-only logic analyzer;
the cable lines and fault outputs are in the 5 V domain.

## 8. Add the mouse after keyboard testing passes

Keep power off while adding the mouse. Add the parts in the “Add mouse”
column of the parts list. **Remove the temporary ground connections from
U2 pins 7 and 9** before connecting the mouse lines.

| Part/contact | Mouse USB connection |
|---|---|
| J3 VBUS, pin 1 | U1 pin **6**, net **USB2_5V** |
| J3 D+, pin 3 | R6, 22 Ω → **GP2** |
| J3 D−, pin 2 | R7, 22 Ω → **GP3** |
| J3 GND and shield | **GND** |
| R8, 15 kΩ | J3 D+ ↔ **GND** |
| R9, 15 kΩ | J3 D− ↔ **GND** |
| C7, 220 µF | Positive → **USB2_5V**; negative → **GND** |
| C8, 100 nF | **USB2_5V** ↔ **GND**, close to J3 |
| R10 and D2 fault LED | 5V_BOARD → R10, 2.2 kΩ → D2 anode; D2 cathode → U1 pin **5** |

| Connection | Mouse DATA | Mouse CLOCK |
|---|---|---|
| Drive GPIO through 2.2 kΩ to base | GP12 → R19 → Q3 pin 2 | GP14 → R23 → Q4 pin 2 |
| Base to GND through 47 kΩ | Q3 pin 2 → R20 → GND | Q4 pin 2 → R24 → GND |
| Transistor emitter | Q3 pin 1 → GND | Q4 pin 1 → GND |
| Transistor collector / cable line | Q3 pin 3 = **MOUSE_DATA** | Q4 pin 3 = **MOUSE_CLOCK** |
| 4.7 kΩ pull-up | MOUSE_5V → R21 → MOUSE_DATA | MOUSE_5V → R25 → MOUSE_CLOCK |
| 100 kΩ line pulldown | MOUSE_DATA → R22 → GND | MOUSE_CLOCK → R26 → GND |
| Buffer input | MOUSE_DATA → U2 pin **7** | MOUSE_CLOCK → U2 pin **9** |
| Buffer output to sense GPIO | U2 pin **6** → **GP13** | U2 pin **10** → **GP15** |
| Output socket J5 | MOUSE_DATA → J5 contact **3** | MOUSE_CLOCK → J5 contact **4** |

J5 contact 1 is **MOUSE_5V**, contact 2 is **GND**; contacts 5–7 and shell
remain open. U2 unused inputs **11 and 14 stay grounded**; unused outputs
12 and 15 and unused package pins 13 and 16 stay open. Module GP4–GP7 and
GP26–GP29 remain unused; GP16 serves the onboard LED.

Repeat the power, GPIO and protocol tests for the mouse before connecting
its X16 cable. Then test keyboard and mouse at the same time.

## Full wiring CSV versus the first build

[BREADBOARD-WIRING.csv](BREADBOARD-WIRING.csv) is the **complete two-port
Rev D circuit**, copied from the canonical wiring table. It includes
optional TP1–TP26 contacts and does not represent literal breadboard rows.
For the keyboard-only stage, omit the mouse parts and use the temporary
U2 pin 7/9 grounds described above. Those temporary grounds are deliberately
absent from the final two-port CSV.
