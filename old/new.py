from typing import Set, Tuple, Dict, List, Optional, Union
from collections import defaultdict


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
    Optional[Set[Tuple[int, int]]]
        Set mit vier Positionen oder False, wenn außerhalb des Spielfelds
    """
    stellen = set()
    spalte, zeile = stelle
    rsp, rze = richtung

    # Berechne die Endposition (3 Schritte in die Richtung)
    spalte_ende, zeile_ende = spalte + rsp * 3, zeile + rze * 3

    # Prüfe ob die Endposition noch innerhalb des Spielfelds liegt
    if spalte_ende < 0 or spalte_ende >= SPALTEN or \
    zeile_ende < 0 or zeile_ende >= ZEILEN:
        return False
    # Sammle alle vier Positionen in der Richtung
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
          Steine speichert
    bekannte_stellen : Set[frozenset]
        Set aller bereits identifizierten Quad-Positionen zur Vermeidung von
         Duplikaten

    Ein Quad ist nur "lebendig" wenn entweder gelbe ODER rote Steine > 0 sind,
      nicht beide.
    """
    zaehler = 0  # Zähler für eindeutige Quad-IDs
    quads = {}
    bekannte_stellen = set()  # Verhindert doppelte Quads

    # Durchlaufe alle Zellen des Spielfelds (1D-Index)
    for i in range(ZELLEN):
        # Durchlaufe alle 8 möglichen Richtungen
        for richtung in RICHTUNGEN:
            # Konvertiere 1D-Index zu 2D-Position im Spielbrett
            stelle = (i % SPALTEN, i // SPALTEN)

            # Ermittle die vier Positionen in dieser Richtung
            stellen = quad_stellen(stelle, richtung)

            # Überspringe, wenn ungültig oder bereits bekannt
            if not stellen or frozenset(stellen) in bekannte_stellen:
                continue

            # Initialisiere neuen Quad mit [gelb_anzahl, rot_anzahl]
            # Der Quad ist nur "lebendig" wenn gelb ODER rot > 0, nicht beide
            quads[zaehler] = [0, 0]

            # Markiere diesen Quad als bekannt (verhindert Duplikate)
            bekannte_stellen.add(frozenset(stellen))

            # Für jede Position im Quad: Speichere die Quad-ID
            # Ermöglicht schnelles Nachschlagen welche Quads betroffen sind
            for stelle in stellen:
                quads_indices[stelle].append(zaehler)

            # Erhöhe Zähler für nächsten Quad
            zaehler += 1

    return quads, bekannte_stellen


def stein_setzen(stelle: Tuple[int, int], spieler: bool) -> bool:
    """
    Setzt einen Stein auf das Spielfeld und aktualisiert alle betroffenen
    Quads.

    Diese Funktion platziert einen Stein auf dem Spielfeld und aktualisiert die
    Zähler aller Quads, in denen diese Position vorkommt. Gleichzeitig prüft
    sie, ob durch diesen Zug ein Quad komplett gefüllt wurde.

    Parameters
    ----------
    stelle : Tuple[int, int]
        Position als Tupel (spalte, zeile)
    spieler : bool
        True für Spieler 1 (gelb/O), False für Spieler 2 (rot/X)

    Returns
    -------
    bool
        True wenn dieser Zug zum Gewinn führt, False sonst

    Ein Gewinn tritt ein, wenn ein Quad 4 Steine derselben Farbe enthält.
    """
    win = False

    # Setze den Stein auf das Spielfeld ('O' für gelb, 'X' für rot)
    spielbrett[stelle] = 'O' if spieler else 'X'

    # Durchlaufe alle Quads, in denen diese Position vorkommt
    for i in quads_indices[stelle]:
        # Erhöhe den entsprechenden Zähler im Quad
        # Index 0 = rote Steine (spieler=False=0)
        # Index 1 = gelbe Steine (spieler=True=1)
        quads[i][1 if spieler else 0] += 1

        # Prüfe ob dieser Quad nun 4 Steine derselben Farbe hat
        if quads[i][1 if spieler else 0] == 4:
            win = True

    return win


def stein_loeschen(pos, spieler):
    """
    Entfernt einen Stein vom Spielbrett und aktualisiert die Quad-Zählungen.

    Parameters
    ----------
    pos : tuple
        Position des Steins als (Spalte, Zeile).
    spieler : bool
        Spieler, dessen Stein entfernt wird (True = Rot, False = Gelb).

    Returns
    -------
    None
        Der Stein wird aus dem Spielbrett gelöscht und die Zählung
        der betroffenen Vierergruppen (Quads) angepasst.
    """

    del spielbrett[pos]
    for i in quads_indices[pos]:
        quads[i][spieler] -=1


def spieler_computer(spieler):
    """
    Bestimmt und führt den besten Zug für den Computer aus.

    Alle möglichen Züge werden mit dem Minimax-Algorithmus mit
    Alpha-Beta-Pruning bewertet. Der Zug mit der besten Bewertung
    wird ausgeführt.

    Parameters
    ----------
    spieler : bool
        Aktiver Spieler (True = Rot, False = Gelb).

    Returns
    -------
    bool
        True, wenn der ausgeführte Zug zum Gewinn führt, sonst False.
    """
    bewertete_zuege = []
    for zug in zug_liste():
        win = stein_setzen(zug, spieler)
        score = min_max(7, -999999, 999999, spieler, win)
        stein_loeschen(zug, spieler)
        bewertete_zuege.append((score,zug))

    bewertete_zuege.sort(reverse=spieler)
    score, bester_zug = bewertete_zuege[0]
    win = stein_setzen(bester_zug, spieler)

    print(bewertete_zuege)
    print(f'Spieler {1 if spieler else 2} setzt {bester_zug} mit der Bewertung {score}')
    return win


# rekursiver Alpha-Beta-Suchalgorithmus
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
        Aktiver Spieler (True = Rot/Maximierer, False = Gelb/Minimierer).
    win : bool
        Gibt an, ob der vorherige Zug bereits zum Gewinn geführt hat.

    Returns
    -------
    int
        Bewertungswert der aktuellen Spielsituation.
    """
    if win:
        return 99999+tiefe if spieler else -99999-tiefe
    if tiefe == 0 or len(spielbrett) == ZELLEN:
        return bewerten()
    spieler = not spieler
    value = -999999 if spieler else 999999
    for zug in zug_liste():
        win = stein_setzen(zug, spieler)
        score = min_max(tiefe-1, alpha, beta, spieler, win)
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


def bewerten():
    """
    Bewertet den den Zustand des Spielbretts.

    Die Funktion iteriert über alle Positionen im Spielbrett und
    überprüft die zugehörigen Vierergruppen (Quads). Gruppen, die
    sowohl gelbe als auch rote Steine enthalten, werden ignoriert.
    Für verbleibende Gruppen wird der Score proportional zur Anzahl
    der Steine einer Farbe berechnet.

    Returns
    -------
    int
        Gesamtbewertung des Spielbretts.
        Positive Werte begünstigen Rot, negative Werte Gelb.

    """

    score = 0
    for pos in spielbrett:
        for i in quads_indices[pos]:
            gelbe, rote = quads[i]
        if gelbe > 0 and rote > 0: continue
        score += rote*10
        score -= gelbe*10
    return score


def zug_liste():
    """
    Ermittelt alle möglichen gültigen Züge im aktuellen Spielzustand.

    Returns
    -------
    list of tuple
        Liste aller möglichen Züge als (Spalte, Zeile)-Tupel, in denen
        ein Stein gesetzt werden kann.
    """

    zuege = []
    for spalte in range(SPALTEN):
        if not spalte_ist_gueltig(spalte): continue
        zeile = finde_tiefste_zeile(spalte)
        zuege.append((spalte,zeile))
    return zuege


def spieler_mensch(spieler):
    """
    Führt einen Zug eines menschlichen Spielers aus.

    Der Spieler gibt eine Spalte ein. Wenn der Zug gültig ist, wird
    der Stein in der tiefsten freien Zeile dieser Spalte gesetzt.

    Parameters
    ----------
    spieler : bool
        Aktiver Spieler (True = Rot, False = Gelb).

    Returns
    -------
    bool
        True, wenn der Zug zu einem Gewinn geführt hat, sonst False.
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


def hauptmenu():
    print("\n=== VIER GEWINNT ===")
    print("1 - Spieler vs Computer")
    print("2 - Spieler vs Spieler")
    print("q - Beenden")
    while True:
        wahl = input("Auswahl: ").strip().lower()
        if wahl in ('1', '2', 'q'):
            return wahl
        print('Ungültige Auswahl.')


if __name__ == "__main__":

    # Konstanten
    SPALTEN = 7
    ZEILEN = 6
    ZELLEN = SPALTEN * ZEILEN
    RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                    (1, 0), (-1, 1), (0, 1), (1, 1)]

    wahl = hauptmenu()
    if wahl == 'q':
        print('Auf Wiedersehen!')
    else:
        # Globale Datenstrukturen für das Quad-System
        quads_indices: Dict[Tuple[int, int], List[int]] = defaultdict(list)
        quads: Dict[int, List[int]] = {}
        spielbrett = {}

        quads, _ = quads_bestimmen()

        spieler = True  # True = Spieler 1 (O), False = Spieler 2 / Computer (X)
        abgebrochen = False

        while True:
            print_spielbrett()

            if wahl == '1':
                # Spieler vs Computer
                if spieler:
                    win = spieler_mensch(spieler)
                    if win is None:
                        abgebrochen = True
                        break
                else:
                    win = spieler_computer(spieler)
            else:
                # Spieler vs Spieler
                win = spieler_mensch(spieler)
                if win is None:
                    abgebrochen = True
                    break

            if win:
                print_spielbrett()
                if wahl == '1':
                    print("Spieler O hat gewonnen!" if spieler else "Computer hat gewonnen!")
                else:
                    print(f"Spieler {'O' if spieler else 'X'} hat gewonnen!")
                break

            if spielbrett_voll():
                print_spielbrett()
                print("Unentschieden!")
                break

            spieler = not spieler

        if abgebrochen:
            print('Spiel beendet.')