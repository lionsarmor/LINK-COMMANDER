#!/usr/bin/env python3
"""Redraw schematic and tables without replacing routed copper."""
import runpy
from pathlib import Path
for name in ['schematic.py','tables.py']:runpy.run_path(str(Path(__file__).with_name(name)),run_name='__main__')
