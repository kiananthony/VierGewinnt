spielbrett = {}  # dictionary

SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN
RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                  (1, 0), (-1, 1), (0, 1), (1, 1)]

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