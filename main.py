"""
Einstiegspunkt für Vier Gewinnt.

Startet das Spiel, zeigt das Hauptmenü und führt die Spielschleife
für den gewählten Spielmodus aus.

Verwendung
----------
    python main.py
"""

from vier_gewinnt.konstanten import spielbrett, quads, quads_indices
from vier_gewinnt.spielfeld import print_spielbrett, spielbrett_voll
from vier_gewinnt.quad import quads_bestimmen
from vier_gewinnt.ki import spieler_mensch, spieler_computer


def hauptmenu():
    """
    Zeigt das Hauptmenü und gibt die Spielmodus-Auswahl zurück.

    Returns
    -------
    str
        '1' für Spieler vs Computer, '2' für Spieler vs Spieler, 'q' zum Beenden.
    """
    print("\n=== VIER GEWINNT ===")
    print("1 - Spieler vs Computer")
    print("2 - Spieler vs Spieler")
    print("q - Beenden")
    while True:
        wahl = input("Auswahl: ").strip().lower()
        if wahl in ('1', '2', 'q'):
            return wahl
        print('Ungültige Auswahl.')


def spiel_starten(wahl):
    """
    Führt die Hauptspielschleife für den gewählten Spielmodus aus.

    Parameters
    ----------
    wahl : str
        '1' für Spieler vs Computer, '2' für Spieler vs Spieler.
    """
    # Spielzustand initialisieren
    spielbrett.clear()
    quads.clear()
    quads_indices.clear()
    quads_neu, _ = quads_bestimmen()
    quads.update(quads_neu)

    spieler = True  # True = Spieler 1 (O), False = Spieler 2 / Computer (X)

    while True:
        print_spielbrett()

        if wahl == '1':
            if spieler:
                win = spieler_mensch(spieler)
                if win is None:
                    print('Spiel beendet.')
                    return
            else:
                win = spieler_computer(spieler)
        else:
            win = spieler_mensch(spieler)
            if win is None:
                print('Spiel beendet.')
                return

        if win:
            print_spielbrett()
            if wahl == '1':
                print("Spieler O hat gewonnen!" if spieler else "Computer hat gewonnen!")
            else:
                print(f"Spieler {'O' if spieler else 'X'} hat gewonnen!")
            return

        if spielbrett_voll():
            print_spielbrett()
            print("Unentschieden!")
            return

        spieler = not spieler


if __name__ == "__main__":
    wahl = hauptmenu()
    if wahl == 'q':
        print('Auf Wiedersehen!')
    else:
        spiel_starten(wahl)