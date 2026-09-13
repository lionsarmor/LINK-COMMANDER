"""Rev D canonical circuit loader: keyboard and mouse only."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
PARTS=json.loads((ROOT/"circuit.json").read_text())
