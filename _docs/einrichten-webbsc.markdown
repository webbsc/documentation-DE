# Einrichten „meiner“ WebBSC

## Überblick

Um eine WebBSC für ein Unternehmen einzurichten sind folgende Schritte erforderlich:

1. Festlegen der Kennzahlen

2. Festlegen der abzubildenden Unternehmensorganisation

3. Anlegen der Uploaddatei

4. Festlegen der Datenquellen im Unternehmen.

5. Einrichten der Schnittstelle zwischen Datenquellen und Uploaddatei

6. Konfiguration der WebBSC

7. Datenimport

8. Fertig. Die Daten können nun in der WebBSC angezeigt und übersichtlich analysiert werden.

Bei der Einrichtung des Systems und bei allen dafür notwendigen Überlegungen kann die ARGE WebBSC gerne unterstützen. Leistungsangebote dafür sind unter [https://www.webbsc.at/de/produkte-und-services/](https://www.webbsc.at/de/produkte-und-services/) ersichtlich.

## Festlegen der Kennzahlen

**Festlegen der Kennzahlen, die im System dargestellt werden sollen**

Die leitende Fragestellung dazu ist, auf Basis welcher Kennzahlen das Unternehmen gesteuert wird bzw. bisher bewertet wurde und welche Kennzahlen in Zukunft für die Bewertung herangezogen werden sollen. Das ist von der Unternehmensleitung zu entscheiden. Für jede der Kennzahlen sind folgende Charakteristika zu notieren:

1. Name

2. Kurzbezeichnung

3. Beschreibung

4. Kennzahldomain (beliebig benennbare Kennzahlengruppe (nur zur Dokumentation))

5. Unteres Limit für Ampelschaltung (ab welchem Prozentwert schaltet die Ampel auf „gelb“)

6. Oberes Limit für Ampelschaltung (ab welchem Prozentwert schaltet die Ampel auf „grün“)

7. Richtung: „aufsteigend“ (größer = besser), „absteigend“ (weniger = besser) oder „optimal“= soll in einem gewissen Bereich sein

8. Aggregierung: „Summe“, „Durchschnitt“, „Durchschnitt pro Organisation”

## Festlegen der abzubildenden Unternehmensorganisation

Es geht um das Festlegen der Organisationsbereiche, Standorte, Branchen/Produktgruppen die getrennt ausgewertet werden sollen (bzw. für welche regelmäßig Kennzahlergebnisse verfügbar sind bzw. sein werden. Dabei sind folgende Fragen zu beantworten und die Uploaddatei(en) entsprechend anzulegen.

1. Welche Standorte werden als eigenes Profit- oder Costcenter geführt und sollen daher in der WebBSC entsprechend abgebildet werden?

2. Welche Organisationseinheiten werden als eigenes Profit- oder Costcenter geführt und sollen daher in der WebBSC entsprechend abgebildet werden?

3. Welche Produkt- und Leistungsbereiche (Branchen) werden als eigenes Profit- oder Costcenter geführt und sollen daher in der WebBSC entsprechend abgebildet werden.

Im einfachsten Fall gibt nur die Gesamtsicht auf das Unternehmen (z.B. nur ein Profitcenter in der G&V und in der Kostenrechnung wie es zum Beispiel bei einem Kleinunternehmen mit einem Standort der Fall sein kann).

## Anlegen der Uploaddatei

Entsprechend der Ergebnisse zu Kennzahlen und Organisationseinheiten (Abschnitte 4.1 und 4.2.) (Abschnitte [Festlegen der Kennzahlen](#festlegen der kennzahlen) und [Festlegen der abzubildenden Unternehmensorganisation](#festlegen der abzubildenden unternehmensorganisation)) werden in der Uploaddatei nun ein Excel-Worksheet für jede Organisationseinheit und die Kennzahlnamen für jedes Worksheet angelegt.

## Festlegen der Datenquellen im Unternehmen

Folgende Fragestellungen können dafür hilfreich sein:

* Woher kommen die Daten für die bisherigen Analysen. Kandidaten dafür sind zum Beispiel eventuell vorhandene Buchhaltungssysteme, Lagerverwaltungssysteme, Zeiterfassungssysteme oder auch ein Kostenrechnungssystem. Vielleicht gibt es für den einen oder anderen Bereich auch Excel Tabellen oder eine andere Art von Listen, in die laufend aktuelle Ergebnisse eingebracht werden.

* Welche neuen Wünsche und Anforderungen gibt es für Kennzahlen, deren Ergebnisse regelmäßig analysiert werden sollen?

* Aus welchen Systemen und Datenquellen können daher in Zukunft Kennzahldaten regelmäßig wie in die Uploaddatei(en) übernommen werden?

## Einrichten der Schnittstelle zwischen Datenquellen und Uploaddatei

Wie kommen die neuen Kennzahldaten von den selektierten Datenquellen im richtigen Format in die Uploaddatei zur regelmäßigen Überleitung der Periodenergebnisse in die WebBSC?

Alle gängigen Lösungen für Unternehmenssoftware bieten Schnittstellen zu Excel an. Diese Schnittstellen werden genutzt, um die Daten zum Beispiel mit den unterschiedlichen Arten von Excel-Verweisen oder mit einfacher Excel-Verlinkung in die vorbereitete Uploaddatei zu übernehmen.

## Konfiguration der WebBSC

Konfiguration der oben festgelegten Standorte, Branchen/Leistungsbereiche, Organisationsbereiche und Kennzahlen, Konfiguration des Cockpit (Welche Kennzahlen sollen in welchem Kennzahlblock (Widget) angezeigt werden, Konfiguration erster Diagramme in Reports, Konfiguration weiterer Benutzer mit Berechtigungen - falls gewünscht.

Die Konfiguration der WebBSC muss bezüglich Kennzahlen und Organisationseinheiten mit der Uploaddatei übereinstimmen, damit das System beim Upload die Daten richtig zuordnen kann.

## Datenimport

Nachdem die WebBSC konfiguriert und die Uploaddatei mit ersten Daten befüllt ist, kann die Uploaddatei in die WebBSC im Modul „Konfiguration“ mittels Button „Datenimport“ übernommen werden.

Die neu importierten Daten stehen anschließend sofort für die Analysen im Cockpit und im Report Modul zur Verfügung.

*Hinweis zum Datenupload:*

Hilfestellung für den Datenupload gibt es in einem Video unter [https://www.webbsc.at/de/ressourcen/anleitungen/](https://www.webbsc.at/de/ressourcen/anleitungen/):

[![WebBSC Datenimport](http://img.youtube.com/vi/PM6b2ur6shQ/0.jpg)](https://www.youtube.com/watch?v=PM6b2ur6shQ)
