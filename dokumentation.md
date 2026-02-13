# Dokumentation Vier Gewinnt
## Aufgabenverteilung

### 1. Mostafa - Spielfeld-Grundlagen & Basis-Logik

- [ ] Spielfeld-Konstanten definiert
  - `SPALTEN`, `ZEILEN`, `ZELLEN`, `RICHTUNGEN`
  
- [ ] Spielfeld-Darstellung implementiert
  - `print_spielbrett()` - Visuelle Ausgabe des Spielfelds mit Rahmen
  
- [ ] Grundlegende Spielfeld-Funktionen
  - `finde_tiefste_zeile(spalte)` - Ermittelt freie Position in Spalte
  - `spalte_ist_gueltig(spalte)` - Validierung von Spielzügen
  - `gewonnen(spieler)` - Gewinnbedingung prüfen (4 in einer Reihe)
  - `spielbrett_voll()` - Unentschieden-Erkennung



### 2. Kian - Repository-Setup, Dokumentation & Quad-System

- [ ] Projekt-Infrastruktur
  - Repository erstellt und initialisiert
  - README.md mit Projektbeschreibung erstellt
  - Dokumentationsstruktur aufgesetzt
  
- [ ] Quad-System implementiert
  - `quad_stellen(stelle, richtung)` - Ermittelt 4er-Sequenzen
  - `quads_bestimmen()` - Erstellt alle möglichen Gewinn-Kombinationen
  - `stein_setzen(stelle, spieler)` - Setzt Stein und aktualisiert Quads



### 3. Stefan - KI-Implementierung & Minimax-Algorithmus
- [ ] Spielzug-Verwaltung
  - `stein_loeschen(pos, spieler)` - Rückgängig-Funktion für Minimax
  - `zug_liste()` - Generiert alle möglichen Züge
  
- [ ] Bewertungsfunktion
  - `bewerten()` - Bewertet Spielsituation heuristisch
  
- [ ] Spieler-Implementierungen
  - `spieler_mensch(spieler)` - Mensch-Computer-Interaktion
  - `spieler_computer(spieler)` - KI-Züge mit Bewertung
  
- [ ] Minimax-Algorithmus
  - `min_max(tiefe, alpha, beta, spieler, win)` - Alpha-Beta-Pruning


## Gemeinsame Verantwortlichkeiten (Alle Teammitglieder)

### Integration & Testing:
- [ ] End-to-End Tests schreiben
- [ ] Bug-Fixing nach Testing-Phase

### Dokumentation:
- [ ] Jeder dokumentiert seine eigenen Funktionen (Docstrings)
- [ ] Code-Kommentare für komplexe Logik hinzufügen
- [x] Benutzerhandbuch erweitern

### Unit-Tests:
- [ ] **Mostafa**: Tests für seine Funktionen
- [ ] **Kian**: Tests für seine Funktionen
- [ ] **Stefan**: Tests für seine Funktionen

### Code-Qualität:
- [ ] Code-Review durchführen
- [ ] PEP 8 Konformität sicherstellen
- [ ] Refactoring nach Best Practices


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


## Vorgehensweise Planung Umsetzung:

### Ansatz
Wir beginnen mit der Entwicklung eines einfachen Spiels, das die Anforderungen der Aufgabe erfüllt. Sobald dies erreicht ist, können wir entscheiden, ob wir das Spiel interaktiver gestalten möchten. Je nach Zeitaufwand und Ressourcen können wir dies mithilfe von KI-Tools, Tutorials oder durch eigenständiges Programmieren realisieren.

### Branches
Das Projekt ist mit zwei Branches strukturiert: „dev“ und „main“. Im Branch „dev“ können wir frei entwickeln und unsere Entwürfe hochladen. Sobald eine Klasse oder Funktion fertig ist, wird die Kompatibilität mit anderen Funktionen geprüft, Docstrings und Unittests werden geschrieben. Nur eine stabile Version wird in den Branch „main“ übertragen. Das bedeutet, dass wir die Basisversion erst dann in „main“ veröffentlichen, wenn sie fertig ist. Sollten wir uns entscheiden, das Projekt fortzusetzen und eine interaktivere Version zu erstellen, können wir diese Version 2.0 ebenfalls in „main“ veröffentlichen. Der Branch-Schutz verhindert direkte Commits in den Branch „main“. Dadurch wird sichergestellt, dass der Code von mindestens einem anderen Mitwirkenden geprüft wird und ein linearer Entwicklungsablauf gewährleistet ist.

### Fokus
Mostafa konzentriert sich auf die grundlegenden Spielfeld-Funktionen wie `print_spielbrett`, `finde_tiefste_zeile`, `spalte_ist_gueltig`, gewonnen und `spielbrett_voll`, die die Basis-Spiellogik und Visualisierung implementieren.

Kian fokussiert sich auf das Repository-Setup, die Dokumentation und das Quad-System mit den Funktionen `quad_stellen`, `quads_bestimmen` und `stein_setzen`, das alle möglichen Gewinnkombinationen effizient verwaltet.

Stefan implementiert die Bewertungsfunktion bewerten, die Spielzug-Verwaltung (`stein_loeschen`, `zug_liste`), die Spieler-Funktionen (`spieler_mensch`, `spieler_computer`) sowie den Minimax-Algorithmus mit Alpha-Beta-Pruning.

## Theorie Software Design
## Theorie Design Patterns
