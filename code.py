python
from collections import defaultdict

spielbrett = {}
"""Globales Dictionary für den Spielzustand.
Schlüssel: (spalte, zeile)-Tupel, Wert: 'X' oder 'O'."""

SPALTEN = 7
"""Anzahl der Spalten des Spielbretts."""

ZEILEN = 6
"""Anzahl der Zeilen des Spielbretts."""

ZELLEN = SPALTEN * ZEILEN
"""Gesamtanzahl der Zellen auf dem Spielbrett."""

RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1)]
"""Alle 8 möglichen Bewegungsrichtungen als (delta_spalte, delta_zeile)-Tupel,
zur Überprüfung von Viererreihen in alle Richtungen."""

quads_indices = defaultdict(list)
"""Mapping von jeder Brettposition auf alle Quad-Indizes, zu denen sie gehört.
Schlüssel: (spalte, zeile)-Tupel, Wert: Liste von Quad-Indizes."""


def print_spielbrett():
    """Gibt das aktuelle Spielbrett formatiert in der Konsole aus.

    Zeigt Spaltenindizes (0–6) als Kopfzeile, Zeilenindizes (0–5) links,
    Spielersteine als 'X' bzw. 'O' und leere Felder als '.'.
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
    """Ermittelt die unterste freie Zeile in einer gegebenen Spalte.

    Durchsucht die Spalte von unten nach oben und gibt die erste
    freie Position zurück (Schwerkraft-Simulation).

    Args:
        spalte (int): Index der zu prüfenden Spalte (0-basiert).

    Returns:
        int: Index der untersten freien Zeile, oder None falls die Spalte voll ist.
    """
    for zeile in reversed(range(ZEILEN)):
        if (spalte, zeile) not in spielbrett:
            return zeile
    return None


def spalte_ist_gueltig(spalte):
    """Prüft, ob ein Zug in die angegebene Spalte gültig ist.

    Eine Spalte ist ungültig, wenn sie außerhalb des Spielfelds liegt
    oder bereits in der obersten Zeile belegt ist.

    Args:
        spalte (int): Index der zu prüfenden Spalte (0-basiert).

    Returns:
        bool: True wenn der Zug erlaubt ist, sonst False.
    """
    if (spalte, 0) in spielbrett:
        return False
    if 0 <= spalte < SPALTEN:
        return True
    return False


# Diese Funktion brauchen wir nicht mehr, hab ich schon ersetzt in stein_setzen funktion.
def gewonnen(spieler):
    """Überprüft, ob der angegebene Spieler das Spiel gewonnen hat.

    Prüft für jeden belegten Stein des Spielers in alle 8 Richtungen,
    ob vier gleichartige Steine in einer Reihe liegen.

    Veraltet:
        Diese Funktion wurde durch die Gewinnprüfung in stein_setzen() ersetzt
        und wird nicht mehr aktiv verwendet.

    Args:
        spieler (bool): True für Spieler 'O', False für Spieler 'X'.

    Returns:
        bool: True wenn der Spieler vier in einer Reihe hat, sonst False.
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
    """Prüft, ob das Spielbrett vollständig belegt ist.

    Returns:
        bool: True wenn alle Zellen belegt sind, sonst False.
    """
    return len(spielbrett) == SPALTEN * ZEILEN


def quad_stellen(stelle, richtung):
    """Berechnet die vier Positionen eines Quads ausgehend von einer Startstelle.

    Ein Quad ist eine Gruppe von vier aufeinanderfolgenden Zellen in einer
    bestimmten Richtung. Gibt False zurück, wenn das Quad außerhalb des
    Spielfelds liegen würde.

    Args:
        stelle (tuple): Startposition als (spalte, zeile)-Tupel.
        richtung (tuple): Richtungsvektor als (delta_spalte, delta_zeile)-Tupel.

    Returns:
        set: Menge der vier (spalte, zeile)-Positionen des Quads,
             oder False wenn das Quad das Spielfeld verlässt.
    """
    stellen = set()
    spalte, zeile = stelle
    rsp, rze = richtung
    spalte_ende, zeile_ende = spalte + rsp * 3, zeile + rze * 3
    if spalte_ende < 0 or spalte_ende >= SPALTEN or zeile_ende < 0 or zeile_ende >= ZEILEN:
        return False
    for i in range(4):
        stellen.add((spalte + rsp * i, zeile + rze * i))
    return stellen


def quads_bestimmen():
    """Ermittelt alle eindeutigen Quads auf dem Spielbrett und ihre Zuordnungen.

    Iteriert über alle Zellen und Richtungen, um jede mögliche Viererreihe
    (Quad) zu finden. Doppelte Quads werden durch frozenset-Vergleich
    ausgeschlossen. Befüllt dabei das globale quads_indices-Dictionary,
    das jeder Zelle ihre zugehörigen Quad-Indizes zuweist.

    Returns:
        tuple:
            - quads (dict): Dictionary mit Quad-Index als Schlüssel und
              [gelb_count, rot_count] als Wert. Ein Quad gilt als 'lebendig',
              solange nur eine Farbe darin vertreten ist.
            - bekannte_stellen (set): Menge aller gefundenen Quads als
              frozensets zur Duplikaterkennung.
    """
    zaehler = 0
    quads = {}
    bekannte_stellen = set()
    for i in range(ZELLEN):
        for richtung in RICHTUNGEN:
            stelle = (i % SPALTEN, i // SPALTEN)  # Setzt 1D-Koordinate um nach 2D-Position im Spielbrett
            stellen = quad_stellen(stelle, richtung)
            if not stellen or stellen in bekannte_stellen:
                continue
            quads[zaehler] = [0, 0]  # Anzahl gelber [0] und roter [1] Steine im Quad
            bekannte_stellen.add(frozenset(stellen))
            for stelle in stellen:
                quads_indices[stelle].append(zaehler)
            zaehler += 1
    return quads, bekannte_stellen


def stein_setzen(stelle, spieler):
    """Setzt einen Stein auf das Spielfeld und prüft auf Gewinn.

    Trägt den Stein ins Spielbrett ein, aktualisiert alle betroffenen Quads
    und prüft, ob durch diesen Zug vier in einer Reihe erreicht wurden.

    Args:
        stelle (tuple): Zielposition als (spalte, zeile)-Tupel.
        spieler (bool): True für Spieler 'O' (gelb), False für Spieler 'X' (rot).

    Returns:
        bool: True wenn der Zug zum Sieg geführt hat, sonst False.
    """
    win = False
    spielbrett[stelle] = 'O' if spieler else 'X'
    for i in quads_indices[stelle]:
        if spieler:
            quads[i][1] += 1
        else:
            quads[i][0] += 1
    if quads[i][spieler] == 4:
        win = True
    return win
