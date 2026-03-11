"""
KI-Modul für Vier Gewinnt.

Dieses Modul enthält den Minimax-Algorithmus mit Alpha-Beta-Pruning,
die Bewertungsfunktion sowie die Spieler-Funktionen für Mensch und
Computer. Der Computergegner bewertet alle möglichen Züge rekursiv
und wählt den optimalen Zug aus.

Autor: Stefan Baldauf
"""

from vier_gewinnt.konstanten import SPALTEN, ZEILEN, ZELLEN, spielbrett, quads, quads_indices
from vier_gewinnt.spielfeld import spalte_ist_gueltig, finde_tiefste_zeile, spielbrett_voll
from vier_gewinnt.quad import stein_setzen


def stein_loeschen(pos, spieler):
    """
    Entfernt einen Stein vom Spielbrett und aktualisiert die Quad-Zählungen.

    Parameters
    ----------
    pos : Tuple[int, int]
        Position des Steins als (spalte, zeile).
    spieler : bool
        Spieler, dessen Stein entfernt wird (True = Gelb/O, False = Rot/X).

    Returns
    -------
    None
    """
    del spielbrett[pos]
    for i in quads_indices[pos]:
        quads[i][spieler] -= 1


def zug_liste():
    """
    Ermittelt alle möglichen gültigen Züge im aktuellen Spielzustand.

    Returns
    -------
    list of tuple
        Liste aller möglichen Züge als (spalte, zeile)-Tupel.
    """
    zuege = []
    for spalte in range(SPALTEN):
        if not spalte_ist_gueltig(spalte):
            continue
        zeile = finde_tiefste_zeile(spalte)
        zuege.append((spalte, zeile))
    return zuege


def bewerten():
    """
    Bewertet den aktuellen Zustand des Spielbretts heuristisch.

    Iteriert über alle besetzten Positionen und deren zugehörige Quads.
    Quads mit Steinen beider Spieler werden ignoriert, da sie nicht
    mehr gewinnbar sind. Für die übrigen Quads wird ein Score
    proportional zur Steinanzahl berechnet.

    Returns
    -------
    int
        Gesamtbewertung des Spielbretts. Positive Werte begünstigen
        den Computer (X), negative Werte den Menschen (O).
    """
    score = 0
    for pos in spielbrett:
        for i in quads_indices[pos]:
            gelbe, rote = quads[i]
            if gelbe > 0 and rote > 0:
                continue
            score += rote * 10
            score -= gelbe * 10
    return score


def min_max(tiefe, alpha, beta, spieler, win):
    """
    Bewertet Spielzustände mit dem Minimax-Algorithmus und Alpha-Beta-Pruning.

    Der Algorithmus durchsucht rekursiv mögliche Spielzüge bis zu einer
    bestimmten Tiefe und verwendet Alpha-Beta-Pruning, um unnötige
    Berechnungen zu vermeiden.

    Parameters
    ----------
    tiefe : int
        Maximale verbleibende Suchtiefe.
    alpha : int
        Aktueller Alpha-Wert für das Pruning (beste Bewertung des Maximierers).
    beta : int
        Aktueller Beta-Wert für das Pruning (beste Bewertung des Minimierers).
    spieler : bool
        Aktiver Spieler (True = Gelb/Maximierer, False = Rot/Minimierer).
    win : bool
        Gibt an, ob der vorherige Zug bereits zum Gewinn geführt hat.

    Returns
    -------
    int
        Bewertungswert der aktuellen Spielsituation.
    """
    if win:
        return 99999 + tiefe if spieler else -99999 - tiefe
    if tiefe == 0 or len(spielbrett) == ZELLEN:
        return bewerten()
    spieler = not spieler
    value = -999999 if spieler else 999999
    for zug in zug_liste():
        win = stein_setzen(zug, spieler)
        score = min_max(tiefe - 1, alpha, beta, spieler, win)
        stein_loeschen(zug, spieler)
        if spieler:
            value = max(value, score)
            alpha = max(value, alpha)
        else:
            value = min(value, score)
            beta = min(value, beta)
        if alpha >= beta:
            break
    return value


def spieler_computer(spieler):
    """
    Bestimmt und führt den besten Zug für den Computer aus.

    Alle möglichen Züge werden mit dem Minimax-Algorithmus mit
    Alpha-Beta-Pruning bewertet. Der Zug mit der besten Bewertung
    wird ausgeführt.

    Parameters
    ----------
    spieler : bool
        Aktiver Spieler (True = Gelb/O, False = Rot/X).

    Returns
    -------
    bool
        True wenn der ausgeführte Zug zum Gewinn führt, sonst False.
    """
    bewertete_zuege = []
    for zug in zug_liste():
        win = stein_setzen(zug, spieler)
        score = min_max(7, -999999, 999999, spieler, win)
        stein_loeschen(zug, spieler)
        bewertete_zuege.append((score, zug))

    bewertete_zuege.sort(reverse=spieler)
    score, bester_zug = bewertete_zuege[0]
    win = stein_setzen(bester_zug, spieler)

    print(f'Computer setzt {bester_zug} mit der Bewertung {score}')
    return win


def spieler_mensch(spieler):
    """
    Führt einen Zug eines menschlichen Spielers aus.

    Der Spieler gibt eine Spalte ein. Wenn der Zug gültig ist, wird
    der Stein in der tiefsten freien Zeile dieser Spalte gesetzt.
    Eingabe 'q' beendet das Spiel.

    Parameters
    ----------
    spieler : bool
        Aktiver Spieler (True = Gelb/O, False = Rot/X).

    Returns
    -------
    bool or None
        True wenn der Zug zum Gewinn führt, False sonst, None bei Abbruch.
    """
    stein = 'O' if spieler else 'X'
    while True:
        eingabe = input(f'Spieler {stein} - Ihr Zug (Spalte 0-6, oder "q" zum Beenden): ').strip()
        if eingabe.lower() == 'q':
            return None
        if not eingabe.isdigit():
            print('Ungültige Eingabe. Bitte eine Zahl zwischen 0 und 6 eingeben.')
            continue
        spalte = int(eingabe)
        if spalte_ist_gueltig(spalte):
            break
        print('Ungültige Spalte. Bitte erneut versuchen.')
    zeile = finde_tiefste_zeile(spalte)
    win = stein_setzen((spalte, zeile), spieler)
    return win