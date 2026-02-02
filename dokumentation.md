# Dokumentation Vier Gewinnt
## Aufgabenverteilung
### Mostafa
- [ ] Deutsch Überprüfung

### Kian
- [ ] Code Überprüfung
- [x] Repository einrichten + erste Planung

## Merkmalen
### Basis Merkmalen
- [ ] 6 Reihen & 7 Spalten
- [ ] 4 horizontale, vertikale oder diagnoale Steine in einer Farbe führen zu Spielgewinn
- [ ] Gamemode: Computer (nicht intelligent)
- [ ] Gamemode: 1v1 (mit Freund)
- [ ] Nach jedem Spielzeug, Spiel überprüfen und bzw beenden
- [ ] Spielbrett anzeigen (mittels matrix, textbasiert)

### Erweiterte Merkmalen
- [ ] Interaktiv Spielmenü
- [ ] Intelligente Computer mode
- [ ] Spielbrett anzeigen (Pygame)

### Übrig
- [ ] Unittests
- [ ] Docstrings


## Vorgehensweise:

### Ansatz
Wir beginnen mit der Entwicklung eines einfachen Spiels, das die Anforderungen der Aufgabe erfüllt. Sobald dies erreicht ist, können wir entscheiden, ob wir das Spiel interaktiver gestalten möchten. Je nach Zeitaufwand und Ressourcen können wir dies mithilfe von KI-Tools, Tutorials oder durch eigenständiges Programmieren realisieren.

### Branches
Das Projekt ist mit drei Branches strukturiert: „dev“, „test“ und „main“. Im Branch „dev“ können wir frei entwickeln und unsere Entwürfe hochladen. Sobald eine Klasse oder Funktion fertig ist, ziehen wir sie in den Branch „test“. Dort wird die Kompatibilität mit anderen Funktionen geprüft, Docstrings und Unittests werden geschrieben (im Branch „dev“, dann in den Branch „test“). Nur eine stabile Version wird in den Branch „main“ übertragen. Das bedeutet, dass wir die Basisversion erst dann in „main“ veröffentlichen, wenn sie fertig ist. Sollten wir uns entscheiden, das Projekt fortzusetzen und eine interaktivere Version zu erstellen, können wir diese Version 2.0 ebenfalls in „main“ veröffentlichen. Der Branch-Schutz verhindert direkte Commits in den Branch „test“ oder „main“. Dadurch wird sichergestellt, dass der Code von mindestens einem anderen Mitwirkenden geprüft wird und ein linearer Entwicklungsablauf gewährleistet ist.

### Fokus
Das ist ein Teamprojekt, wir sind beide für das Ergebnis verantwortlich. Wir werden alles gemeinsam überprüfen, aber Mostafas Fokus liegt etwas stärker auf Deutsch und Kians Fokus etwas stärker auf dem Programmieren, um unsere Stärken optimal zu nutzen.

## Klasse & Attribute
### Basis
Klasse `VierGewinnt`:
* Attribute
    * A
    * B
* Methoden
    * A
    * B

Funktionen

### Erweiterte
Klasse `VierGewinnt`:
* Attribute
    * A
    * B
* Methoden
    * A
    * B

Funktionen

## Theorie Software Design
## Theorie Design Patterns
