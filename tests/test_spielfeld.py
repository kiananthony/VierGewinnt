import pytest
from collections import defaultdict

# ── Zu testende Funktionen importieren (Datei heißt z.B. vier_gewinnt.py) ──
from vier_gewinnt.konstanten import (
    spielbrett, quads_indices,
    SPALTEN, ZEILEN, ZELLEN, RICHTUNGEN
)
from vier_gewinnt.spielfeld import (
    finde_tiefste_zeile, spalte_ist_gueltig,
    gewonnen, spielbrett_voll
)
from vier_gewinnt.quad import (
    quad_stellen, quads_bestimmen, stein_setzen
)

# ═══════════════════════════════════════════════════════
#  Fixtures
# ═══════════════════════════════════════════════════════

@pytest.fixture(autouse=True)
def leeres_spielbrett():
    """Setzt spielbrett und quads_indices vor jedem Test zurück."""
    spielbrett.clear()
    quads_indices.clear()
    yield


@pytest.fixture
def quads():
    """Gibt ein frisch berechnetes quads-Dictionary zurück."""
    q, _ = quads_bestimmen()
    return q


# ═══════════════════════════════════════════════════════
#  Konstanten
# ═══════════════════════════════════════════════════════

class TestKonstanten:
    def test_spalten(self):
        assert SPALTEN == 7

    def test_zeilen(self):
        assert ZEILEN == 6

    def test_zellen(self):
        assert ZELLEN == SPALTEN * ZEILEN

    def test_richtungen_anzahl(self):
        assert len(RICHTUNGEN) == 8

    def test_richtungen_sind_einzigartig(self):
        assert len(set(RICHTUNGEN)) == 8


# ═══════════════════════════════════════════════════════
#  finde_tiefste_zeile
# ═══════════════════════════════════════════════════════

class TestFindeTiefsteZeile:
    def test_leere_spalte_gibt_unterste_zeile(self):
        assert finde_tiefste_zeile(0) == ZEILEN - 1

    def test_teilweise_gefuellte_spalte(self):
        spielbrett[(0, ZEILEN - 1)] = 'X'
        assert finde_tiefste_zeile(0) == ZEILEN - 2

    def test_volle_spalte_gibt_none(self):
        for zeile in range(ZEILEN):
            spielbrett[(0, zeile)] = 'X'
        assert finde_tiefste_zeile(0) is None

    def test_nur_oberste_zeile_frei(self):
        for zeile in range(1, ZEILEN):
            spielbrett[(3, zeile)] = 'O'
        assert finde_tiefste_zeile(3) == 0


# ═══════════════════════════════════════════════════════
#  spalte_ist_gueltig
# ═══════════════════════════════════════════════════════

class TestSpalteIstGueltig:
    def test_leere_spalte_ist_gueltig(self):
        assert spalte_ist_gueltig(0) is True

    def test_alle_leeren_spalten_gueltig(self):
        for s in range(SPALTEN):
            assert spalte_ist_gueltig(s) is True

    def test_volle_spalte_ist_ungueltig(self):
        spielbrett[(0, 0)] = 'X'  # oberste Zeile belegt
        assert spalte_ist_gueltig(0) is False

    def test_negative_spalte_ungueltig(self):
        assert spalte_ist_gueltig(-1) is False

    def test_spalte_zu_gross_ungueltig(self):
        assert spalte_ist_gueltig(SPALTEN) is False


# ═══════════════════════════════════════════════════════
#  spielbrett_voll
# ═══════════════════════════════════════════════════════

class TestSpielbrrettVoll:
    def test_leeres_brett_nicht_voll(self):
        assert spielbrett_voll() is False

    def test_teilweise_gefuellt_nicht_voll(self):
        spielbrett[(0, 0)] = 'X'
        assert spielbrett_voll() is False

    def test_volles_brett_ist_voll(self):
        for spalte in range(SPALTEN):
            for zeile in range(ZEILEN):
                spielbrett[(spalte, zeile)] = 'X'
        assert spielbrett_voll() is True

    def test_eine_zelle_fehlt_nicht_voll(self):
        for spalte in range(SPALTEN):
            for zeile in range(ZEILEN):
                spielbrett[(spalte, zeile)] = 'X'
        del spielbrett[(0, 0)]
        assert spielbrett_voll() is False


# ═══════════════════════════════════════════════════════
#  quad_stellen
# ═══════════════════════════════════════════════════════

class TestQuadStellen:
    def test_gueltiges_quad_horizontal(self):
        stellen = quad_stellen((0, 0), (1, 0))
        assert stellen == {(0, 0), (1, 0), (2, 0), (3, 0)}

    def test_gueltiges_quad_vertikal(self):
        stellen = quad_stellen((0, 0), (0, 1))
        assert stellen == {(0, 0), (0, 1), (0, 2), (0, 3)}

    def test_gueltiges_quad_diagonal(self):
        stellen = quad_stellen((0, 0), (1, 1))
        assert stellen == {(0, 0), (1, 1), (2, 2), (3, 3)}

    def test_quad_ausserhalb_rechts_gibt_false(self):
        assert quad_stellen((5, 0), (1, 0)) is False

    def test_quad_ausserhalb_unten_gibt_false(self):
        assert quad_stellen((0, 4), (0, 1)) is False

    def test_quad_ausserhalb_negativ_gibt_false(self):
        assert quad_stellen((1, 0), (-1, 0)) is False

    def test_quad_hat_genau_vier_stellen(self):
        stellen = quad_stellen((0, 0), (1, 0))
        assert len(stellen) == 4


# ═══════════════════════════════════════════════════════
#  quads_bestimmen
# ═══════════════════════════════════════════════════════

class TestQuadsBestimmen:
    def test_gibt_dict_zurueck(self, quads):
        assert isinstance(quads, dict)

    def test_keine_doppelten_quads(self):
        _, bekannte_stellen = quads_bestimmen()
        # Jedes Element ist ein frozenset → bereits dedupliziert
        laengen = [len(fs) for fs in bekannte_stellen]
        assert all(l == 4 for l in laengen)

    def test_quads_indices_befuellt(self, quads):
        assert len(quads_indices) > 0

    def test_jede_stelle_in_mindestens_einem_quad(self, quads):
        for spalte in range(SPALTEN):
            for zeile in range(ZEILEN):
                assert len(quads_indices[(spalte, zeile)]) >= 1

    def test_quads_zaehler_initialisiert(self, quads):
        for wert in quads.values():
            assert wert == [0, 0]


# ═══════════════════════════════════════════════════════
#  stein_setzen & gewonnen
# ═══════════════════════════════════════════════════════

class TestSteinSetzen:
    def test_stein_wird_ins_brett_eingetragen_O(self, quads):
        stein_setzen((0, 5), True)
        assert spielbrett[(0, 5)] == 'O'

    def test_stein_wird_ins_brett_eingetragen_X(self, quads):
        stein_setzen((0, 5), False)
        assert spielbrett[(0, 5)] == 'X'

    def test_kein_sieg_nach_einem_stein(self, quads):
        assert stein_setzen((0, 5), True) is False

    def test_sieg_horizontal(self, quads):
        """Vier O-Steine nebeneinander in unterster Zeile."""
        for spalte in range(3):
            stein_setzen((spalte, 5), True)
        assert stein_setzen((3, 5), True) is True

    def test_sieg_vertikal(self, quads):
        """Vier O-Steine übereinander in Spalte 0."""
        for zeile in range(5, 2, -1):
            stein_setzen((0, zeile), True)
        assert stein_setzen((0, 2), True) is True

    def test_sieg_diagonal(self, quads):
        """Vier O-Steine diagonal von (0,5) nach (3,2)."""
        positionen = [(0, 5), (1, 4), (2, 3), (3, 2)]
        for pos in positionen[:-1]:
            stein_setzen(pos, True)
        assert stein_setzen(positionen[-1], True) is True

    def test_kein_sieg_gemischte_steine(self, quads):
        """Abwechselnd X und O – kein Sieg möglich."""
        stein_setzen((0, 5), True)
        stein_setzen((1, 5), False)
        stein_setzen((2, 5), True)
        assert stein_setzen((3, 5), False) is False


# ═══════════════════════════════════════════════════════
#  gewonnen (legacy)
# ═══════════════════════════════════════════════════════

class TestGewonnen:
    def test_kein_sieg_leeres_brett(self):
        assert gewonnen(True) is False
        assert gewonnen(False) is False

    def test_sieg_horizontal_O(self):
        for spalte in range(4):
            spielbrett[(spalte, 0)] = 'O'
        assert gewonnen(True) is True

    def test_sieg_horizontal_X(self):
        for spalte in range(4):
            spielbrett[(spalte, 0)] = 'X'
        assert gewonnen(False) is True

    def test_kein_sieg_nur_drei_in_reihe(self):
        for spalte in range(3):
            spielbrett[(spalte, 0)] = 'O'
        assert gewonnen(True) is False

    def test_sieg_vertikal(self):
        for zeile in range(4):
            spielbrett[(0, zeile)] = 'O'
        assert gewonnen(True) is True

    def test_sieg_diagonal(self):
        for i in range(4):
            spielbrett[(i, i)] = 'O'
        assert gewonnen(True) is True

    def test_kein_fremder_sieg(self):
        for spalte in range(4):
            spielbrett[(spalte, 0)] = 'O'
        assert gewonnen(False) is False  # X hat nicht gewonnen