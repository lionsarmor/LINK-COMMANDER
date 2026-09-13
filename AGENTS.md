# LINK COMMANDER project rules

These are design requirements explicitly confirmed by the user:

- The controller is the user's **RP2040-Zero module**, currently the hiBCTR
  listing ASIN B0DXL12W59. Put male headers on the module and through-hole
  female sockets on the carrier. Keep the module removable.
- Every other carrier component must be **through-hole**. Use socketed DIP
  ICs and leaded passives/transistors. No additional SMD modules or adapters.
- Use only the module's perimeter header contacts; do not silently add
  soldered wires to underside GPIO pads.
- Rev D has two USB inputs: keyboard and mouse only. No gamepad support or USB hub.
  Manufacturers' USB receivers handle 2.4 GHz; no onboard Bluetooth/radio.
- Two 7-pin DIN sockets solder directly to the carrier. Use custom cables
  for the X16 PS/2 keyboard and mouse ports.
- Support extensible receiver drivers and normalized input state. Do not
  describe all 2.4 GHz receivers as standard HID or universally compatible.
- Keep schematic, PCB, BOM, cable pinouts and breadboard wiring consistent.

The current design is `hardware/rev-d/`. Read its README and validation
reports before changing it. It is an untested engineering prototype, not a
fabrication release. CAD checks do not establish physical connector fit,
USB signal integrity, receiver compatibility or safe electrical operation.

`circuit.json` defines the checked circuit. `tools/schematic.py` generates
its one-page schematic without changing the PCB. `tools/layout.py` resets
all routing; read `tools/README.md` before using it. Preserve the routed
board for ordinary schematic/documentation edits. Verify the saved board
with `check_board.py` and exported schematic XML with `check_design.py`.
Rev A, B and C remain historical local revisions. Publish Rev D as the active design.
