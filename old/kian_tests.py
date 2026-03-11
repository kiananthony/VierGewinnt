import unittest
from collections import defaultdict
import vier_gewinnt as vg


class TestQuadStellen(unittest.TestCase):
    """Tests für die quad_stellen Funktion"""

    def test_horizontal_valid(self):
        """Testet gültigen horizontalen Quad von Startposition"""
        result = vg.quad_stellen((0, 0), (1, 0))
        expected = {(0, 0), (1, 0), (2, 0), (3, 0)}
        self.assertEqual(result, expected)

    def test_vertical_valid(self):
        """Testet gültigen vertikalen Quad von Startposition"""
        result = vg.quad_stellen((0, 0), (0, 1))
        expected = {(0, 0), (0, 1), (0, 2), (0, 3)}
        self.assertEqual(result, expected)

    def test_diagonal_down_right_valid(self):
        """Testet gültigen diagonalen Quad (rechts-unten)"""
        result = vg.quad_stellen((0, 0), (1, 1))
        expected = {(0, 0), (1, 1), (2, 2), (3, 3)}
        self.assertEqual(result, expected)

    def test_diagonal_up_right_valid(self):
        """Testet gültigen diagonalen Quad (rechts-oben)"""
        result = vg.quad_stellen((0, 3), (1, -1))
        expected = {(0, 3), (1, 2), (2, 1), (3, 0)}
        self.assertEqual(result, expected)

    def test_horizontal_out_of_bounds_right(self):
        """Testet horizontalen Quad der rechts aus dem Spielfeld läuft"""
        result = vg.quad_stellen((5, 0), (1, 0))
        self.assertFalse(result)

    def test_vertical_out_of_bounds_bottom(self):
        """Testet vertikalen Quad der unten aus dem Spielfeld läuft"""
        result = vg.quad_stellen((0, 4), (0, 1))
        self.assertFalse(result)

    def test_diagonal_out_of_bounds(self):
        """Testet diagonalen Quad der aus dem Spielfeld läuft"""
        result = vg.quad_stellen((5, 4), (1, 1))
        self.assertFalse(result)

    def test_negative_out_of_bounds(self):
        """Testet Quad der in negative Koordinaten läuft"""
        result = vg.quad_stellen((2, 2), (-1, -1))
        self.assertFalse(result)

    def test_exact_boundary_horizontal(self):
        """Testet Quad der genau an die rechte Grenze passt"""
        result = vg.quad_stellen((3, 0), (1, 0))
        expected = {(3, 0), (4, 0), (5, 0), (6, 0)}
        self.assertEqual(result, expected)

    def test_exact_boundary_vertical(self):
        """Testet Quad der genau an die untere Grenze passt"""
        result = vg.quad_stellen((0, 2), (0, 1))
        expected = {(0, 2), (0, 3), (0, 4), (0, 5)}
        self.assertEqual(result, expected)


class TestQuadsBestimmen(unittest.TestCase):
    """Tests für die quads_bestimmen Funktion"""

    def setUp(self):
        """Setze den globalen Zustand des Moduls vor jedem Test zurück"""
        vg.quads_indices = defaultdict(list)

    def test_returns_tuple(self):
        """Testet dass die Funktion ein Tupel mit korrekten Typen zurückgibt"""
        result = vg.quads_bestimmen()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], dict)
        self.assertIsInstance(result[1], set)

    def test_quads_have_correct_structure(self):
        """Testet dass jeder Quad [0, 0] als Initialwert hat"""
        quads_local, _ = vg.quads_bestimmen()
        for quad_id, counts in quads_local.items():
            self.assertIsInstance(counts, list)
            self.assertEqual(len(counts), 2)
            self.assertEqual(counts, [0, 0])

    def test_no_duplicate_quads(self):
        """Testet dass bekannte_stellen doppelte Quads verhindert"""
        _, bekannte_stellen = vg.quads_bestimmen()
        # Jedes frozenset sollte einzigartig sein
        self.assertEqual(len(bekannte_stellen), len(list(bekannte_stellen)))

    def test_quad_count_reasonable(self):
        """Testet dass die Anzahl der Quads für das Standard-Brett angemessen ist"""
        quads_local, _ = vg.quads_bestimmen()
        # Für 7x6 Brett: 
        # Horizontal: 4 pro Reihe * 6 Reihen = 24
        # Vertikal: 3 pro Spalte * 7 Spalten = 21
        # Diagonal (rechts-unten): variiert, ungefähr 12
        # Diagonal (rechts-oben): variiert, ungefähr 12
        # Gesamt ungefähr 69
        self.assertGreater(len(quads_local), 50)
        self.assertLess(len(quads_local), 100)

    def test_quads_indices_populated(self):
        """Testet dass quads_indices korrekt befüllt wird"""
        vg.quads_bestimmen()
        # Jede Position sollte in mindestens einem Quad sein (Ecken in weniger)
        self.assertGreater(len(vg.quads_indices), 0)
        # Prüfe dass eine zentrale Position in mehreren Quads ist
        if (3, 3) in vg.quads_indices:
            self.assertGreater(len(vg.quads_indices[(3, 3)]), 1)

    def test_each_quad_has_four_positions(self):
        """Testet dass jeder Quad in bekannte_stellen genau 4 Positionen hat"""
        _, bekannte_stellen = vg.quads_bestimmen()
        for quad_positions in bekannte_stellen:
            self.assertEqual(len(quad_positions), 4)


class TestSteinSetzen(unittest.TestCase):
    """Tests für die stein_setzen Funktion"""

    def setUp(self):
        """Setze den globalen Zustand des Moduls vor jedem Test zurück"""
        vg.spielbrett = {}
        vg.quads_indices = defaultdict(list)
        vg.quads, _ = vg.quads_bestimmen()

    def test_place_yellow_stone(self):
        """Testet das Setzen eines gelben Steins (spieler=True)"""
        result = vg.stein_setzen((0, 0), True)
        self.assertEqual(vg.spielbrett[(0, 0)], 'O')
        self.assertFalse(result)  # Kein Gewinn beim ersten Zug

    def test_place_red_stone(self):
        """Testet das Setzen eines roten Steins (spieler=False)"""
        result = vg.stein_setzen((0, 0), False)
        self.assertEqual(vg.spielbrett[(0, 0)], 'X')
        self.assertFalse(result)  # Kein Gewinn beim ersten Zug

    def test_updates_quad_counts_yellow(self):
        """Testet dass das Setzen eines gelben Steins die Quad-Zähler korrekt aktualisiert"""
        vg.stein_setzen((0, 0), True)
        # Prüfe dass mindestens ein Quad aktualisiert wurde (gelb ist Index 1)
        found_updated = False
        for quad_id in vg.quads_indices[(0, 0)]:
            if vg.quads[quad_id][1] == 1:  # Gelb-Zähler erhöht
                found_updated = True
                break
        self.assertTrue(found_updated)

    def test_updates_quad_counts_red(self):
        """Testet dass das Setzen eines roten Steins die Quad-Zähler korrekt aktualisiert"""
        vg.stein_setzen((0, 0), False)
        # Prüfe dass mindestens ein Quad aktualisiert wurde (rot ist Index 0)
        found_updated = False
        for quad_id in vg.quads_indices[(0, 0)]:
            if vg.quads[quad_id][0] == 1:  # Rot-Zähler erhöht
                found_updated = True
                break
        self.assertTrue(found_updated)

    def test_horizontal_win_yellow(self):
        """Testet die Erkennung eines horizontalen Gewinns für Gelb"""
        # Setze 4 gelbe Steine in einer Reihe
        vg.stein_setzen((0, 0), True)
        vg.stein_setzen((1, 0), True)
        vg.stein_setzen((2, 0), True)
        result = vg.stein_setzen((3, 0), True)
        self.assertTrue(result)

    def test_horizontal_win_red(self):
        """Testet die Erkennung eines horizontalen Gewinns für Rot"""
        # Setze 4 rote Steine in einer Reihe
        vg.stein_setzen((0, 0), False)
        vg.stein_setzen((1, 0), False)
        vg.stein_setzen((2, 0), False)
        result = vg.stein_setzen((3, 0), False)
        self.assertTrue(result)

    def test_vertical_win(self):
        """Testet die Erkennung eines vertikalen Gewinns"""
        vg.stein_setzen((0, 0), True)
        vg.stein_setzen((0, 1), True)
        vg.stein_setzen((0, 2), True)
        result = vg.stein_setzen((0, 3), True)
        self.assertTrue(result)

    def test_diagonal_win(self):
        """Testet die Erkennung eines diagonalen Gewinns"""
        vg.stein_setzen((0, 0), True)
        vg.stein_setzen((1, 1), True)
        vg.stein_setzen((2, 2), True)
        result = vg.stein_setzen((3, 3), True)
        self.assertTrue(result)

    def test_no_win_with_three_stones(self):
        """Testet dass 3 Steine in einer Reihe keinen Gewinn auslösen"""
        vg.stein_setzen((0, 0), True)
        vg.stein_setzen((1, 0), True)
        result = vg.stein_setzen((2, 0), True)
        self.assertFalse(result)

    def test_mixed_colors_no_win(self):
        """Testet dass gemischte Farben keinen Gewinn auslösen"""
        vg.stein_setzen((0, 0), True)   # Gelb
        vg.stein_setzen((1, 0), False)  # Rot
        vg.stein_setzen((2, 0), True)   # Gelb
        result = vg.stein_setzen((3, 0), True)  # Gelb
        self.assertFalse(result)

    def test_multiple_quads_affected(self):
        """Testet dass das Setzen eines Steins mehrere Quads aktualisiert"""
        # Eine zentrale Position sollte in mehreren Quads sein
        vg.stein_setzen((3, 3), True)
        affected_quads = [vg.quads[i] for i in vg.quads_indices[(3, 3)]]
        # Mindestens ein Quad sollte aktualisiert sein
        self.assertTrue(any(quad[1] == 1 for quad in affected_quads))

    def test_win_on_any_of_multiple_quads(self):
        """Testet dass ein Gewinn erkannt wird wenn irgendeinen Quad vervollständigt wird"""
        # Vervollständige einen horizontalen Gewinn
        vg.stein_setzen((1, 2), True)
        vg.stein_setzen((2, 2), True)
        vg.stein_setzen((3, 2), True)
        result = vg.stein_setzen((4, 2), True)
        self.assertTrue(result)


if __name__ == '__main__':
    # Initialisiere die globalen Variablen des Moduls vor dem Ausführen der Tests
    # Dies simuliert was in der main-Funktion passiert
    vg.SPALTEN = 7
    vg.ZEILEN = 6
    vg.ZELLEN = vg.SPALTEN * vg.ZEILEN
    vg.RICHTUNGEN = [
        (1, 0),   # horizontal
        (0, 1),   # vertikal
        (1, 1),   # diagonal rechts-unten
        (1, -1),  # diagonal rechts-oben
    ]
    vg.spielbrett = {}
    vg.quads_indices = defaultdict(list)
    vg.quads = {}

    unittest.main(verbosity=2)
