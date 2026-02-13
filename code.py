from collections import defaultdict

spielbrett = {}  # dictionary

SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN
RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                  (1, 0), (-1, 1), (0, 1), (1, 1)]
quads_indices = defaultdict(list)

def print_spielbrett():
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
    for zeile in reversed(range(ZEILEN)):
        if (spalte, zeile) not in spielbrett:
            return zeile
    return None

def spalte_ist_gueltig(spalte):
    if (spalte, 0) in spielbrett:
        return False
    if 0 <= spalte < SPALTEN:
        return True
    return False
## Diese Funktion brauchen wir nicht mehr, hab ich schon ersetzt in stein_setzen funktion.
def gewonnen(spieler):
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
    return len(spielbrett) == SPALTEN * ZEILEN
from typing import Set, Tuple, Dict, List, Optional
from collections import defaultdict

# Globale Datenstrukturen für das Quad-System
quads_indices: Dict[Tuple[int, int], List[int]] = defaultdict(list)
quads: Dict[int, List[int]] = {}


def quad_stellen(stelle: Tuple[int, int], richtung: Tuple[int, int]) -> Optional[Set[Tuple[int, int]]]:
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
    if spalte_ende < 0 or spalte_ende >= SPALTEN or zeile_ende < 0 or zeile_ende >= ZEILEN:
        return False
    
    # Sammle alle vier Positionen in der Richtung
    for i in range(4):
        stellen.add((spalte + rsp * i, zeile + rze * i))
    
    return stellen


def quads_bestimmen() -> Tuple[Dict[int, List[int]], Set[frozenset]]:
    """
    Erstellt alle möglichen Viererreihen (Quads) auf dem Spielfeld.
    
    Diese Funktion durchläuft alle Positionen und Richtungen auf dem Spielfeld
    und identifiziert alle eindeutigen Kombinationen von vier aufeinanderfolgenden
    Feldern. Jeder Quad wird mit einer ID versehen und in zwei Datenstrukturen
    gespeichert.
    
    Returns
    -------
    quads : Dict[int, List[int]]
        Dictionary das für jeden Quad die Anzahl gelber [0] und roter [1] Steine speichert
    bekannte_stellen : Set[frozenset]
        Set aller bereits identifizierten Quad-Positionen zur Vermeidung von Duplikaten
    
    Ein Quad ist nur "lebendig" wenn entweder gelbe ODER rote Steine > 0 sind, nicht beide.
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
            # Dies ermöglicht schnelles Nachschlagen welche Quads betroffen sind
            for stelle in stellen:
                quads_indices[stelle].append(zaehler)
            
            # Erhöhe Zähler für nächsten Quad
            zaehler += 1
    
    return quads, bekannte_stellen


def stein_setzen(stelle: Tuple[int, int], spieler: bool) -> bool:
    """
    Setzt einen Stein auf das Spielfeld und aktualisiert alle betroffenen Quads.
    
    Diese Funktion platziert einen Stein auf dem Spielfeld und aktualisiert die 
    Zähler aller Quads, in denen diese Position vorkommt. Gleichzeitig prüft sie, 
    ob durch diesen Zug ein Quad komplett gefüllt wurde.
    
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
        quads[i][0 if spieler else 1] += 1

        # Prüfe ob dieser Quad nun 4 Steine derselben Farbe hat
        if quads[i][0 if spieler else 1] == 4:
            win = True
    
    return win


if __name__ == "__main__":
    quads, _ = quads_bestimmen()
    spielfeld = {}  # Key = (spalte, zeile), Value = 'O' oder 'X'

    spieler = True
    while True:
        print_spielbrett()
        if spieler:
            win = spieler_mensch(spieler)
        else:
            win = spieler_computer(spieler)
        if win:
            print_spielbrett()
            print('GEWONNEN!')
            break
        spieler = not spieler