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

def quad_stellen(stelle, richtung):
    stellen = set()
    spalte, zeile = stelle 
    rsp, rze = richtung
    spalte_ende, zeile_ende = spalte + rsp * 3, zeile + rze * 3
    if spalte_ende < 0 or spalte_ende >= SPALTEN or zeile_ende < 0 or zeile_ende >= ZEILEN:
        return False
    for i in range(4):
        stellen.add((spalte+rsp*i, zeile+rze*i))
    return stellen
    
def quads_bestimmen():
    zaehler = 0
    quads = {}
    bekannte_stellen = set()
    for i in range(ZELLEN):
        for richtung in RICHTUNGEN:
            stelle = (i % SPALTEN, i  // SPALTEN) # Setzt 1D koordinat um nach 2D position im Spielbrett
            stellen = quad_stellen(stelle, richtung)
            if not stellen or stellen in bekannte_stellen: continue
            quads[zaehler] =  [0, 0] # Anzahl gelben [0], roten [1] Steinen im Quad, weil der Quad nicht lebendig ist wann gelb und rot > 0
            bekannte_stellen.add(frozenset(stellen))
            for stelle in stellen:
                quads_indices[stelle].append(zaehler)
            zaehler += 1
    return quads, bekannte_stellen

def stein_setzen(stelle, spieler):
    win = False
    spielfeld[stelle] = 'O' if spieler else 'X'
    for i in quads_indices[stelle]:
        if spieler:
            quads[i][1]  =+ 1
        else:
            quads[i][0] =+ 1
    if quads[i][spieler ==4]:
        win = True
    return win
