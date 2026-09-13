# LINK COMMANDER product brief — Rev D

## Goal

Let a Commander X16 use a supported modern USB keyboard and mouse,
including devices with their own 2.4 GHz USB receivers, through the X16's
PS/2 keyboard and mouse ports. Keep the design straightforward to explain,
breadboard and solder in a student setting.

## Active scope

- Two independent USB-A host inputs, assigned to keyboard and mouse.
- Two directly mounted 7-pin DIN outputs and custom PS/2 cables.
- User's RP2040-Zero module on removable perimeter-header sockets.
- All other carrier components through-hole; socketed DIP ICs.
- No USB hub, onboard radio, Bluetooth or gamepad support.
- Extensible HID keyboard/mouse parsing; receiver compatibility must be tested.
- One-page student schematic with functional sections and actual wires.
- Rounded, elongated board with KiCad/open-hardware silkscreen graphics.

## Rev D implementation

One TPS2042P DIP-8 dual switch protects both receiver supplies. One CD4050BE
DIP-16 reads four PS/2 lines at 3.3 V. Four 2N3904 transistors provide
low-only DATA/CLOCK drive. The RP2040 runs USB host and PS/2 device firmware.
The supply-switch enables are grounded; receiver power is always on when
external 5 V is present. There is no RUN_ENABLE signal.

The 140 × 80 mm, two-layer PCB has 80 CAD positions: 50 electrical parts, four
mounting holes and 26 bare test contacts. USB data uses existing resistor
pads for probing; power and PS/2 signals have dedicated test holes. Both DIN target +5 V reference nets remain separate from
board power. JP1 is a manual programming-power interlock.

## Delivery and limits

Current CAD, BOM, student guide, breadboard tables, cable pinout, firmware
contract and validation reports are in [hardware/rev-d](../hardware/rev-d/README.md).
The schematic netlist and saved board are checked against the same canonical
pin assignments. DRC does not prove USB signal integrity or actual X16
operation. Firmware, receiver tests, physical footprint fit, power sequencing
and PS/2 timing remain bench acceptance work.

Earlier four-port/gamepad designs are historical and are not Rev D build
instructions. The current GitHub design is keyboard/mouse only.
