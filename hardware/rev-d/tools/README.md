# Rebuilding and checking Rev D

`circuit.json` is the component/pin/net source. `design.py` loads it.
The schematic embeds its symbols and the PCB uses the supplied local
footprint library. The editable files can be opened directly in KiCad.

`python3 tools/build.py` redraws the single-page schematic and regenerates
the BOM/wiring tables, including the root `BREADBOARD-PARTS.csv`,
`BREADBOARD-WIRING.csv` and the generated parts table inside `BREADBOARD.md`.
The root wiring CSV is the full two-port circuit; keyboard-only temporary
connections are described in the root guide. It preserves the routed PCB. After schematic changes,
export a fresh XML netlist with KiCad and run `python3 tools/check_design.py`.
That check compares actual exported nets with the source, and separately
checks the two-port PS/2 interface, non-inverted sense signals, USB power
switch enables, unused pins and supply separation.

Scripts that import `pcbnew` use `tools/run-kicad-python`. Its default
KiCad installation path is specific to the development machine; set
`LC_KICAD_ROOT` to your extracted KiCad root or run the scripts with your
own matching KiCad Python environment. CAD was generated and checked with
KiCad 7.0.11. The native files do not require this wrapper to open in KiCad.

## Rebuilding the PCB replaces its routing

1. `layout.py` creates the unrouted 140 × 80 mm, two-layer board and restores
   project net classes from `project-template.json`. It copies the two
   standard logo footprints from the installed KiCad library.
2. `prepare_route.py` writes the placement DRC and exports the Specctra DSN
   with explicit routing settings. The supplied DSN uses two signal layers.
3. Route with Freerouting 1.9 using one worker thread. Use the project's
   trace widths and clearances; do not relax them to get a completed route.
4. `finish_board.py` imports the complete SES into an **unrouted** board and
   adds/fills the B.Cu ground pour. Its limited importer checks units,
   layer names and via size. The supplied session contains the complete route.
5. `check_board.py` verifies the saved board's populated pad nets, through-hole
   pad types, two-layer stack, ground pour and complete DRC result.
6. `export_review.py` regenerates layer plots without changing the PCB.
   Use KiCad CLI exports for the PDF, cropped SVG and assembly views.

The checks are file/connectivity checks, not a full electrical simulation,
standard-symbol ERC, USB impedance verification or proof of X16 operation.
Keep those distinctions in any regenerated validation report.
