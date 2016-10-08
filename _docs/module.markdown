---
title: Module
date: 2016-10-07 16:06:00 Z
published: false
---

# Module der WebBSC und der WebBSC Demo

## Einstiegsmenü

Nach dem Einstieg in das System öffnet sich das Cockpit mit den für alle Module fixen Hauptmenüpunkten in der oberen Menüleiste:

* Cockpit

* Reports

* Konfiguration

* Benutzername (hier im Screenshot "DEMO")

![menu.png](/_uploads/menu.png)

Ganz rechts in der Menüleiste erscheint der Benutzername, mit dem Sie sich angemeldet haben. Im Falle der WebBSC Demo ist das „DEMO“. Durch Anwahl dieses Menüpunktes öffnet sich ein Untermenü zum Abmelden vom System:

![logout.png](/_uploads/logout.png)

Wiedereinstieg in die WebBSC Demo ist wie bereits oben beschrieben über die Webseite [www.webbsc.at](http://www.webbsc.at) möglich.

## Funktionsumfang der WebBSC Demo (Demosystem)

Das Demosystem arbeitet vor dem Hintergrund eines vordefinierten Modellunternehmens mit festgelegten Einstellungen für die Organisationsstruktur, Standorte, Branchen sowie Plan- und Istwerten für die ebenfalls exemplarisch vordefinierten Kennzahlen. Das Demosystem kann damit einen Eindruck über eine Reihe von Möglichkeiten der WebBSC vermitteln. Man kann im Cockpit Einstellungen zu unterschiedlichen Vergleichszeiträumen, Organisationsbereichen, Produktbereichen und Standorten vornehmen, im Report-Modul vordefinierte Reports und Diagramme ansehen, einzelne Bereiche des Konfigurationsmenüs durchsehen und sich damit einen Überblick über einige Grundfunktionen der WebBSC verschaffen.

Basis für die Darstellungen ist eine fiktive \*\*Demoorganisation \*\*mit fixen Plan- und Istdaten für mehrere Jahre:

* Vertriebsorganisation mit 2 Standorten in Österreich (Bregenz und Graz)

* Festgelegte Angebotspalette mit mehreren Produktbereichen (Branchen: Karton, Papier, Zubehör)

* Vordefinierte Kennzahlen für die Demoorganisation

* Vordefinierte Kennzahlblöcke für die Ampeldarstellung im Cockpit

* Vordefinierte Übersichtsdiagramme im Report Modul

Die **WebBSC Demo** ist nur für den **lesenden Zugriff** freigegeben. Es können keine Daten verändert, auch keine individuellen Daten hochgeladen und keine eigenen Kennzahlen definiert werden. Die dazu notwendigen Berechtigungen sind für Demouser gesperrt. Der Anwender bekommt dennoch einen ersten Eindruck vom Nutzen, den die WebBSC für ein Unternehmen bringen kann: Übersichtlichen Darstellung der Entwicklung zentraler Kennzahlen, Vergleiche in Ampeldarstellung und aussagekräftige Diagramme.

## Das Modul „Cockpit“

Das Cockpit gibt eine Übersicht über den aktuellen Stand der Kennzahlen des Unternehmens im Vergleich zum Plan oder zu einem frei wählbaren Vergleichszeitraum. Die übersichtliche Ampeldarstellung liefert auf einen Blick eine Grundaussage zum Grad der Zielerreichung für die angewählten Kennzahlen, je nach Einstellung der Zeitperiode, der Teilorganisation oder des gewählten Produktbereiche bzw. der Branche. Der Vergleich von Plan- oder Istwerten aus frei wählbaren Perioden macht auf einen Blick den Unternehmensfortschritt in absoluten Zahlen und in Prozentwerten sichtbar.

Welche Kennzahlen dargestellt werden sollen kann frei im Hauptmenüpunkt „Konfiguration“ eingestellt werden.

Das folgende Bild zeigt das Cockpit der WebBSC Demo:

![cockpit.png](/uploads/cockpit.png)

### Begriffe zum Modul Cockpit

* Ein Cockpit besteht aus Blöcken von Kennzahlen, sogenannte Widgets

* In Widgets können mehrere Kennzahlen zusammengefasst werden. Das Beispiel oben zeigt 4 Widgets, und zwar

  * Widget „Bilanz“ mit ausgewählten Kennzahlen aus der Bilanz

  * Widget „Umsatz und Ertrag“ mit ausgewählten Kennzahlen aus der G&V

  * Widget „Mitarbeiter und Kunden“ mit ausgewählten Kennzahlen zu Mitarbeitern und Kunden

  * Widget „Kosten GKV“ mit ausgewählten Kennzahlen aus der Kostenrechnung (in diesem Fall Gesamtkostenverfahren)

### Einstellungen im Cockpit und Anzeige in den Widgets

Die Kennzahlen sind im Screenshot oben in 4 Blöcke gegliedert: Umsatz und Ertrag, Bilanzwerte, Kosten Gesamtkostenverfahren, Mitarbeiter und Kunden.

Jedes Widget zeigt für eine Reihe von Kennzahlen die absolute Zahl für den Istwert und für den Vergleichswert, eine Prozentzahl für den Prozentvergleich und weiters ein Ampellicht mit grün für „OK“, orange für „fast OK“ und rot für „nicht OK“, und zwar für Produktbereiche/Branchen, Standorte und Vergleichszeiträume entsprechend den „Einstellungen“ ganz rechts im Cockpit. Ein Istwert von 8,0 (Ref) und ein Vergleichswert von 10 (Vgl.) liefert z.B. 80% Zielerreichung.

Im Block „Einstellungen“ können die zu betrachtenden Organisationsbereiche (Branche und Standort), der zu betrachtende Zeitraum (Jahr, Periode) und der Vergleichszeitraum (Vergleich mit Planzahlen für eine zu wählende Periode oder Vergleich mit den Istzahlen einer zu wählenden Periode) eingestellt werden. Das Cockpit zeigt die entsprechenden Werte an.

So ist die Entwicklung der Kennzahlen des Unternehmens in den einzelnen Bereichen auf einen Blick einzusehen.

### Grafen im Cockpit

Mit einem Klick auf eine beliebige Kennzahl in einem Widget kann die Entwicklung dieser Kennzahl im Vergleich zum Plan genauer dargestellt werden. Hier am Beispiel „Gesamtumsatz“:

![diagram1.png](/uploads/diagram1.png)

Durch Verschieben des Ausschnittes entlang der Zeitleiste im unteren Bereich der Grafik kann der jeweilige Zeitraum im oberen Teil des Grafen genauer angezeigt werden, um Details analysieren zu können- Siehe nächstes Bild im Vergleich zum vorigen:

![diagram2.png](/uploads/diagram2.png)

### Individuelle Cockpits für unterschiedliche Benutzer

Cockpits können pro Benutzer konfiguriert werden. So ist es zum Beispiel möglich, für Mitarbeiter oder Leiter eines Geschäftsbereiches Werte nur für Ihren eigenen Organisationsbereich anzuzeigen, während die Geschäftsführung Einblick in alle einzelnen Bereiche sowie über alle konsolidierten Gesamtwerte und Summen bekommen wird. Der Aufbau des Cockpits wird im Modul „Konfiguration“ konfiguriert.

Bemerkung: In der WebBSC Demo sind das Cockpit und die Widgets fix vordefiniert und können vom Anwender nicht geändert werden.

## Das Modul „Reports“

Im Menüpunkt Reports werden speziell für das Unternehmen während der Systeminstallation oder jederzeit auch danach definierte grafische Übersichten (Diagramme) angezeigt, die die Entwicklung und den Stand von Kennzahlen sichtbar machen. Die Grundeinheit zur Darstellung im Modul Reports ist das Diagramm. Jedes Diagramm wird in einem eigenen Grafen dargestellt. Mit den Diagrammen kann die Entwicklung einzelner Kennzahlen oder Kennzahlvergleiche in Form unterschiedlicher Diagrammtypen dargestellt werden (siehe weiter unten).

Diagramme werden in Gruppen zusammengefasst, genannt Reports. Im Untermenü „Reports“ rechts oben im nachfolgenden Screenshot können die im Konfigurationsmenü definierten Reports angewählt werden, um die entsprechenden Diagramme in einer Kleinformat-Darstellung anzuzeigen. Im folgenden Bild sind das: Basisreports, Branchenvergleiche, Standortreports und Gruppenreports.

Das folgende Bild zeigt sich beim Einstieg in das Modul Reports der WebBSC Demo:

![reports.png](/uploads/reports.png)

Durch Anwahl einer Reportgruppe werden alle Diagramme angezeigt, die dieser Reportgruppe im Menü Konfiguration zugeordnet worden sind.

Bild oben zeigt die Kleinformat-Darstellung folgender Diagramme aus der angewählten Gruppe „Basisreports“:

* „Standortvergleich Ergebnis pro Quartal“ – Horizontalbalkendiagramm

* „Standortvergleich Ergebnis“ – Liniendiagramm

* „Branchenvergleich Umsatz jährlich“ – Multi-Säulendiagramm

* „G&V Auszug Jahre“ – Multi-Säulendiagramm

* „G%V Auszug Quartal“ – Multisäulendiagramm

* „Standortvergleich Umsatz“ – Liniendiagramm

Die Diagramme im Kleinformat sind durch drücken auf den roten Balken des Diagrammes erweiterbar, sodass das Diagramm in Großformat erscheint. Hier am Beispiel „G&V Auszug Jahre – 2012-2016“:

![report_big-47fc95.png](/uploads/report_big-47fc95.png)

Rechts oben im Bild ist die Legende Führt man den Cursor auf einen der Balken eines Jahres, werden die Werte genau angezeigt, hier:

![report_legend.png](/uploads/report_legend.png)

**Folgende Diagrammtypen stehen zur Verfügung:**

* Liniendiagramm

* Liniendiagramm it Fokus

* Gestapeltes Ebenendiagramm

* Horizontalsäulendiagramm

* Streudiagramm

* Multi-Säulendiagramm

Das System biete umfangreiche Möglichkeiten neue Reports selbst zu definieren. Die Definition der Diagramme erfolgt im Modul „Konfiguration“ mittels Button „Diagramme“. Diagrammgruppen (Reports) werden im Konfigurationsmenü mittels Button „Reports“ angelegt.

Bemerkung: In der WebBSC Demo sind die Reports und Diagramme fix vordefiniert und können vom Anwender nicht geändert werden.

## Das Modul „Konfiguration“

Nach dem Einstieg in die WebBSC Demo zeigt sich folgendes Bild:

![demo-conf.png](/uploads/demo-conf.png)

Beim Einstieg in ein Kundensystem werden zusätzliche Punkte angezeigt:

![user-conf.png](/uploads/user-conf.png)

Mit den einzelnen Sub-Menüpunkten können unterschiedliche Aspekte des Unternehmens, und was davon in der WebBSC dargestellt werden soll, festgelegt werden. Im Detail wie folgt:

 1. Benutzer:

    * Wer darf das System nutzen, welche Daten sollen für wen sichtbar sein?

    * Welche Benutzernamen? Ändern des Pases. Welches Cockpit, welche Widgetsnamme sollen angezeigt werden.

    * Welche Berechtigungsgruppe (Rolle)? Darf nur gelesen oder auch z.B. neue Kennzahlen angelegt werden. Dürfen Daten hochgeladen werden? Welche Organisationsbereiche, Produktbereiche, Standorte dürfen gesehen werden?

 2. Rollen:

    * Welche Berechtigungstypen sollen definiert werden, die dann einzelnen Benutzern zugeordnet werden.

    * Z.B.: Administrator, Geschäftsleiter, Vertriebsleiter. Mitarbeiter im Vertrieb, Mitarbeiter im Backoffice.

    * In der Rollenverwaltung kann konfiguriert werden, welche Menüpunkte für die jeweilige Rolle erlaubt sind.

 3. Standorte, (Teil-)Organisationen, Branchen:

    * Wie ist die Organisation strukturiert und welche Produktbereiche bzw. Branchen gibt es im Unternehmen in welchen Hierarchieebenen?

    * Wie sind Leistungsbereiche/Produktbereiche und Standorte zu Organisationseinheiten hierarchisch zusammengefasst, für die z.B. eine eigene Gewinn und Verlustrechnung gemacht wird (Profitcenter). Wie erfolgt daher die Summenbildung für höhere Hierarchieebenen.

    * Branchen sind zum Beispiel Produktbereiche des Unternehmens (z.B. „Papier“ oder „Zubehör“ im Demosystem), oder Leistungsbereiche.

 4. Cockpits: Siehe auch unter „Erstellen von Widgets und Cockpits“ weiter unten.

    * Jedem Benutzer kann ein eigenes Cockpit zugeordnet werden, sodass je nach Aufgabenbereich die entsprechenden Kennzahlen angezeigt werden (siehe Rollen und Benutzerrechte).

    * Jedem Cockpit werden bestimmte Widgets (Kennzahlgruppen) zugeordnet, die dann im Cockpit angezeigt werden.

 5. Widgets: Siehe auJedem Benutzer kann ein eigenes Cockpit zugeordnet werden, sodass je nach Aufgabenbereich die entsprechenden Kennzahlen angezeigt werden (siehe Rollen und Benutzerrechte).ch unter „Erstellen von Widgets und Cockpits“ weiter unten.

    * Welche Kennzahlen werden im Cockpit in welchen Kennzahlgruppen (Widgets) zusammengefasst dargestellt?

    * z.B. „Umsatz und Ertrag“ oder „Bilanz“ im Demosystem

 6. Reports: Siehe auch unter „Erstellen von Diagrammen und Reports“ weiter unten.

    * Definition der Report-Gruppen, die es geben soll, und Zuordnung der Diagramme zu den Reports (Diagrammgruppen).

 7. Diagramme: Siehe auch unter „Erstellen von Diagrammen und Reports“ weiter unten.

 8. 

 9. Kennzahldefinitionen:

10. Datenimport:

11. Data Setup: