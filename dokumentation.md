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
- [x] **Kian**: Tests für seine Funktionen
- [ ] **Stefan**: Tests für seine Funktionen

### Code-Qualität:
- [ ] Code-Review durchführen
- [ ] PEP 8 Konformität sicherstellen
- [ ] Refactoring nach Best Practices


## Merkmalen
### Basis Merkmalen
- [x] 6 Reihen & 7 Spalten
- [x] 4 horizontale, vertikale oder diagnoale Steine in einer Farbe führen zu Spielgewinn
- [x] Gamemode: Computer (nicht intelligent)
- [ ] Gamemode: 1v1 (mit Freund)
- [x] Nach jedem Spielzeug, Spiel überprüfen und bzw beenden
- [x] Spielbrett anzeigen (mittels matrix, textbasiert)

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

## Reflexion

Aufgrund von Zeitmangel und anderen Verpflichtungen konnten wir als Team nur die Basisimplementierung des Projekts realisieren. Ein wesentlicher Faktor war, dass wir zu spät mit der Arbeit begonnen haben, wodurch uns die notwendige Zeit fehlte, um die erweiterten Features umzusetzen.

Im Rückblick hätten wir früher mit der Planung und Entwicklung beginnen sollen, um ausreichend Zeit für die Implementierung der erweiterten Merkmale wie das interaktive Spielmenü, die intelligente Computer-KI und die grafische Darstellung mittels Pygame zu haben. Auch die Erstellung von Unittests und vollständigen Docstrings blieb aufgrund der Zeitknappheit unvollständig.

Trotz dieser Einschränkungen haben wir die grundlegenden Anforderungen erfüllt und ein funktionsfähiges Vier-Gewinnt-Spiel entwickelt. 

Ein weiterer Kompromiss, den wir aufgrund der Zeitknappheit eingehen mussten, war der Verzicht auf einen objektorientierten Ansatz mit Klassen. Stattdessen haben wir uns für eine prozedurale Implementierung entschieden, um schneller zu einem funktionsfähigen Ergebnis zu kommen. Obwohl das Spiel dadurch seine Grundfunktionalität erfüllt, hat dieser Ansatz deutliche Nachteile: Der Code ist schwerer erweiterbar, weniger modular und die Wiederverwendbarkeit ist eingeschränkt. Eine klassenbasierte Struktur mit separaten Klassen für das Spielbrett, die Spieler und die Spiellogik hätte eine klarere Trennung der Verantwortlichkeiten ermöglicht und würde das Hinzufügen neuer Features wie verschiedene Spielmodi oder KI-Gegner erheblich vereinfachen. Mit mehr Zeit hätten wir das Projekt definitiv mit einem objektorientierten Design umgesetzt, um eine wartbarere und professionellere Codebasis zu schaffen.

## Theorie Software Design

Wenn ein Modul nur aus wenigen Klassen mit sehr langen Methoden besteht und kaum dokumentiert ist, ergeben sich mehrere Nachteile:

**Schwierige Wartbarkeit**
Lange Methoden sind schwer zu verstehen und zu debuggen. Änderungen können ungewollte Nebeneffekte verursachen.
**Geringe Wiederverwendbarkeit**
Funktionalität ist stark gekoppelt und lässt sich nur schwer in anderen Modulen wiederverwenden.
**Hohe Komplexität**
Es ist schwer, den Überblick zu behalten, welche Logik wo implementiert ist, und Tests werden aufwendig.
**Schwierige Erweiterbarkeit**
Neue Features einzubauen, ohne bestehenden Code zu brechen, wird riskant.

Verletzte grundlegende Software-Design-Prinzipien:

**Single Responsibility Principle (SRP)**
Jede Methode/Klasse sollte nur eine Aufgabe haben. Sehr lange Methoden verstoßen häufig dagegen.
**Separation of Concerns**
Logik verschiedener Verantwortlichkeiten ist vermischt.
**DRY – Don’t Repeat Yourself**
Bei langen Methoden wird oft Code wiederholt.
**Kapselung / Information Hiding**
Kaum Dokumentation und starke Abhängigkeiten erschweren den kontrollierten Zugriff auf Daten.
**Testbarkeit** 
Lange, gekoppelte Methoden sind schwer isoliert testbar.


## Theorie Design Patterns - Kians Funktionen
Ich nutze dieses Pattern **Flyweight** bereits in meiner `quads_bestimmen()` Funktion, wo ich mit `bekannte_stellen` sicherstelle, dass jede einzigartige Viererreihe nur einmal gespeichert wird - wenn ich zum Beispiel die vier Felder (0,0), (1,0), (2,0), (3,0) finde. Dann wird diese exakte Kombination nicht nochmal gespeichert, selbst wenn ich später von einer anderen Startposition auf dieselben vier Felder stoße, denn das frozenset erkennt dass es dieselben Positionen sind und ich überspringe sie mit continue. Was bedeutet dass ich bei einem 7×6 Brett nur 69 einzigartige Quads speichere statt möglicherweise 200+ Duplikate, und das spart massiv Speicher und macht mein Programm schneller weil bei jedem Zug nur diese 69 Quads geprüft werden müssen statt hunderte redundanter Kopien durchzugehen.

Ich nutze das **Iterator** Pattern implizit in meiner `stein_setzen()` Funktion mit der Zeile for i in `quads_indices[stelle]:`. Hier iteriere ich über alle betroffenen Quad-IDs, ohne dass ich wissen muss wie viele es sind oder wie sie intern gespeichert sind. Die quads_indices Datenstruktur ist ein defaultdict(list), die für jede Position eine Liste von Quad-IDs speichert. Wenn ich einen Stein setze, muss ich nur durch diese Liste durchgehen mit `for i in quads_indices[stelle]` und dann` quads[i][1 if spieler else 0] += 1` aufrufen. Ich brauche keinen Index manuell hochzuzählen oder die Länge der Liste zu kennen.

## Theorie Design Patterns - Stefan Min-Max Suchstrategie

Ein Problem bei vielen Spielen mit zwei Spielern ist, zu entscheiden welcher Zug langfristig am besten ist. Dabei müssen auch zukünftige Züge des anderen Spielers berücksichtigt werden. Der Lösungsansatz mit dem Minimax-Algorithmus wird hierbei häufig verwendet. Er erzeugt einen Spielbaum von möglichen zukünftigen Spielzügen, also simuliert Spielverläufe bis zu einer bestimmten Tiefe und bewertet anschließend die resultierenden Positionen. Daraus wird dann ausgewählt. In unserem Spiel verwenden wir hierzu die Funktion `min_max()`, sie arbeitet rekursiv und bewertet jeden möglichen Zug und unterscheidet zwischen maximierendem und minimierendem Spieler mit der Funktion `bewerten()`. Um den Algorithmus effizienter zu gestalten, verwenden wir das Alpha-Beta-Pruning. Damit werden Zweige des Suchbaums frühzeitig abgeschnitten, bei denen klar ist, dass sie keine bessere Lösung liefern können. 
