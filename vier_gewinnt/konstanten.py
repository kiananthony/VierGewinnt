"""
Konstanten und globaler Spielzustand für Vier Gewinnt.

Dieses Modul definiert alle Spielfeld-Konstanten sowie die gemeinsam
genutzten Datenstrukturen (Spielbrett, Quads), auf die alle anderen
Module zugreifen.
"""

from collections import defaultdict
from typing import Dict, List, Tuple

SPALTEN: int = 7
ZEILEN: int = 6
ZELLEN: int = SPALTEN * ZEILEN
RICHTUNGEN: List[Tuple[int, int]] = [
    (-1, -1), (0, -1), (1, -1), (-1, 0),
    (1, 0), (-1, 1), (0, 1), (1, 1)
]

# Gemeinsamer Spielzustand — wird von allen Modulen geteilt
spielbrett: Dict[Tuple[int, int], str] = {}
quads: Dict[int, List[int]] = {}
quads_indices: Dict[Tuple[int, int], List[int]] = defaultdict(list)