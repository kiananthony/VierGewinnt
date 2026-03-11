"""
Spielfeld-Modul für Vier Gewinnt.

Dieses Modul enthält alle grundlegenden Spielfeld-Funktionen:
die visuelle Darstellung des Bretts, Validierung von Spielzügen
sowie die Gewinn- und Unentschieden-Erkennung.

Autor: Mostafa Fayz
"""

from vier_gewinnt.konstanten import SPALTEN, ZEILEN, ZELLEN, RICHTUNGEN
from vier_gewinnt.konstanten import spielbrett


def print_spielbrett():
    """
    Gibt das aktuelle Spielbrett in der Konsole aus.

    Zeigt das Spielfeld mit Spaltennummern (0-6) und Zeilennummern (0-5).
    Leere Felder werden als '.' dargestellt, gesetzte Steine als 'O' oder 'X'.

    Returns
    -------
    None
    """
    print("\n  0 1 2 3 4 5 6")
    print(" +" + "-" * (SPALTEN * 2 - 1) + "+")
    for zeile in range(ZEILEN):
        print(f"{zeile}|", end="")
        for spalte in range(SPALTEN):
            if (spalte, zeile) in spielbrett:
                print(spielbrett[(spalte, zeile)], end=" ")
            else:
                print(".", end=" ")
        print("|")
    print(" +" + "-" * (SPALTEN * 2 - 1) + "+")


def finde_tiefste_zeile(spalte):
    """
    Ermittelt die unterste freie Zeile in einer gegebenen Spalte.

    Durchsucht die Spalte von unten nach oben und gibt die erste
    freie Position zurück.

    Parameters
    ----------
    spalte : int
        Spaltenindex (0-6).

    Returns
    -------
    int or None
        Index der untersten freien Zeile, oder None wenn die Spalte voll ist.
    """
    for zeile in reversed(range(ZEILEN)):
        if (spalte, zeile) not in spielbrett:
            return zeile
    return None


def spalte_ist_gueltig(spalte):
    """
    Überprüft ob ein Zug in der angegebenen Spalte gültig ist.

    Eine Spalte ist gültig wenn sie innerhalb des Spielfelds liegt
    und das oberste Feld noch nicht belegt ist.

    Parameters
    ----------
    spalte : int
        Spaltenindex (0-6).

    Returns
    -------
    bool
        True wenn die Spalte bespielbar ist, False sonst.
    """
    if (spalte, 0) in spielbrett:
        return False
    if 0 <= spalte < SPALTEN:
        return True
    return False


# Diese Funktion brauchen wir nicht mehr, hab ich schon ersetzt in stein_setzen funktion.
def gewonnen(spieler):
    """
    Prüft ob der angegebene Spieler gewonnen hat.

    Durchsucht alle Positionen auf dem Spielbrett nach vier aufeinander-
    folgenden Steinen desselben Spielers in einer der acht Richtungen.

    Hinweis: Diese Funktion wird nicht mehr aktiv verwendet, da die
    Gewinnprüfung in stein_setzen() über das Quad-System erfolgt.

    Parameters
    ----------
    spieler : bool
        True für Spieler 1 (O), False für Spieler 2 (X).

    Returns
    -------
    bool
        True wenn der Spieler gewonnen hat, False sonst.
    """
    stein = 'O' if spieler else 'X'
    for pos in spielbrett:
        for richtung in RICHTUNGEN:
            vier_in_einer_reihe = True
            for i in range(4):
                spalte, zeile = pos
                delta_spalte, delta_zeile = richtung
                p1 = (spalte + delta_spalte * i, zeile + delta_zeile * i)
                if p1 in spielbrett and spielbrett[p1] == stein:
                    continue
                vier_in_einer_reihe = False
                break
            if vier_in_einer_reihe:
                return True
    return False


def spielbrett_voll():
    """
    Prüft ob das Spielbrett vollständig belegt ist.

    Returns
    -------
    bool
        True wenn alle Felder belegt sind (Unentschieden), False sonst.
    """
    return len(spielbrett) == SPALTEN * ZEILEN