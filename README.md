# Vier Gewinnt
## Beschreibung
Dieses Repository enthält eine in Python entwickelte Version von Vier Gewinnt.

## Spielregeln
1. Das Spielfeld wird zu Beginn jeder Runde angezeigt (`.` = leeres Feld, `O` = Ihre Steine, `X` = Computer-Steine)
2. Sie werden aufgefordert, eine Spalte zu wählen (0-6)
3. Ihr Stein wird in der gewählten Spalte nach unten fallen
4. Danach macht der Computer automatisch seinen Zug
5. Das Spiel endet, wenn ein Spieler vier Steine in einer Reihe hat oder das Spielfeld voll ist (Unentschieden)


## Projektbeschreibung

Dieses Projekt implementiert das klassische Strategiespiel "Vier Gewinnt" (Connect Four) in Python. Das Spiel ermöglicht es einem menschlichen Spieler gegen eine computergesteuerte KI anzutreten, die den Minimax-Algorithmus mit Alpha-Beta-Pruning verwendet. Der Computer bewertet mögliche Züge strategisch und versucht, den Spieler zu schlagen, indem er mehrere Züge im Voraus berechnet.

Das Spielfeld besteht aus 7 Spalten und 6 Zeilen. Ziel ist es, vier eigene Steine in einer Reihe (horizontal, vertikal oder diagonal) zu platzieren. Der menschliche Spieler spielt mit 'O' (gelb) und beginnt immer, während der Computer mit 'X' (rot) spielt.

## Installation & Abhänigkeiten

Dieses Projekt benötigt Python 3.6 oder höher. Es werden keine externen Packages benötigt, da nur die Python-Standardbibliothek verwendet wird.

```bash
# Repository klonen oder Dateien herunterladen
git clone 
cd VierGewinnt
```

## Spielstart

Um das Spiel zu starten, führen Sie einfach die Code aus:

```bash
python -m main.py
```


## Kontakte
* Fayz, Mostafa (s55460@edu.campus02.at)
* van Holst, Kian (s58003@edu.campus02.at)
* Baldauf, Stefan (s58033@edu.campus02.at)
 
## Anerkennung

## Referenzen & Unterstützung
* [pygame] https://www.youtube.com/watch?v=XpYz-q1lxu8
* [textbasiert] https://www.youtube.com/watch?v=NkmYfTl2L_Y
* [german] https://www.youtube.com/watch?v=dCLFA-eHDg0
