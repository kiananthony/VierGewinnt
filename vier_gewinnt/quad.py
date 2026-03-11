"""
Quad-Modul für Vier Gewinnt.

Dieses Modul verwaltet das Quad-System: alle möglichen Viererreihen
auf dem Spielfeld werden einmalig berechnet und effizient gespeichert.
Beim Setzen oder Löschen eines Steins werden nur die betroffenen
Quads aktualisiert, was eine schnelle Gewinnprüfung ermöglicht.

Autor: Kian van Holst
"""

from typing import Set, Tuple, Dict, List, Union
from vier_gewinnt.konstanten import SPALTEN, ZEILEN, ZELLEN, RICHTUNGEN
from vier_gewinnt.konstanten import spielbrett, quads, quads_indices


def quad_stellen(
    stelle: Tuple[int, int],
    richtung: Tuple[int, int]
) -> Union[Set[Tuple[int, int]], bool]:
    """
    Ermittelt vier aufeinanderfolgende Positionen in einer bestimmten Richtung.

    Diese Funktion prüft, ob ausgehend von einer Startposition vier Felder
    in einer gegebenen Richtung innerhalb des Spielfelds liegen.

    Parameters
    ----------
    stelle : Tuple[int, int]
        Startposition als Tupel (spalte, zeile)
    richtung : Tuple[int, int]
        Richtungsvektor als Tupel (delta_spalte, delta_zeile)

    Returns
    -------
    Union[Set[Tuple[int, int]], bool]
        Set mit vier Positionen oder False, wenn außerhalb des Spielfelds.
    """
    stellen = set()
    spalte, zeile = stelle
    rsp, rze = richtung

    spalte_ende, zeile_ende = spalte + rsp * 3, zeile + rze * 3

    if spalte_ende < 0 or spalte_ende >= SPALTEN or \
    zeile_ende < 0 or zeile_ende >= ZEILEN:
        return False

    for i in range(4):
        stellen.add((spalte + rsp * i, zeile + rze * i))

    return stellen


def quads_bestimmen() -> Tuple[Dict[int, List[int]], Set[frozenset]]:
    """
    Erstellt alle möglichen Viererreihen (Quads) auf dem Spielfeld.

    Diese Funktion durchläuft alle Positionen und Richtungen auf dem Spielfeld
    und identifiziert alle eindeutigen Kombinationen von 4 aufeinanderfolgenden
    Feldern. Jeder Quad wird mit einer ID versehen und in zwei Datenstrukturen
    gespeichert.

    Returns
    -------
    quads : Dict[int, List[int]]
        Dictionary das für jeden Quad die Anzahl gelber [0] und roter [1]
        Steine speichert.
    bekannte_stellen : Set[frozenset]
        Set aller bereits identifizierten Quad-Positionen zur Vermeidung
        von Duplikaten.

    Notes
    -----
    Ein Quad ist nur "lebendig" wenn entweder gelbe ODER rote Steine > 0
    sind, nicht beide.
    """
    zaehler = 0
    bekannte_stellen = set()

    for i in range(ZELLEN):
        for richtung in RICHTUNGEN:
            stelle = (i % SPALTEN, i // SPALTEN)
            stellen = quad_stellen(stelle, richtung)

            if not stellen or frozenset(stellen) in bekannte_stellen:
                continue

            quads[zaehler] = [0, 0]
            bekannte_stellen.add(frozenset(stellen))

            for stelle in stellen:
                quads_indices[stelle].append(zaehler)

            zaehler += 1

    return quads, bekannte_stellen


def stein_setzen(stelle: Tuple[int, int], spieler: bool) -> bool:
    """
    Setzt einen Stein auf das Spielfeld und aktualisiert alle betroffenen Quads.

    Diese Funktion platziert einen Stein auf dem Spielfeld und aktualisiert die
    Zähler aller Quads, in denen diese Position vorkommt. Gleichzeitig prüft
    sie, ob durch diesen Zug ein Quad komplett gefüllt wurde.

    Parameters
    ----------
    stelle : Tuple[int, int]
        Position als Tupel (spalte, zeile).
    spieler : bool
        True für Spieler 1 (gelb/O), False für Spieler 2 (rot/X).

    Returns
    -------
    bool
        True wenn dieser Zug zum Gewinn führt, False sonst.

    Notes
    -----
    Ein Gewinn tritt ein, wenn ein Quad 4 Steine derselben Farbe enthält.
    """
    win = False

    spielbrett[stelle] = 'O' if spieler else 'X'

    for i in quads_indices[stelle]:
        quads[i][1 if spieler else 0] += 1

        if quads[i][1 if spieler else 0] == 4:
            win = True

    return win