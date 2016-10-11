Datenimport
============

Hilfestellung für den Datenupload gibt es in einem Video:

.. raw:: html
  
  <iframe width="560" height="315" src="https://www.youtube.com/embed/PM6b2ur6shQ" frameborder="0" allowfullscreen></iframe>

Mit dem Konfigurationsmodul „Datenimport“ (grüner Button) werden neue Daten ins System eingebracht. Sofort nach dem Datenimport sind die neuen Daten für alle Anzeigen verfügbar.

**Upload Datei und Namen der Worksheets:**

Die Daten werden aus einer Uploaddatei in das System importiert. Eine Uploaddatei ist eine ExcelDateie mit der Endung .xls oder .xlsx. Innerhalb einer Uploaddatei müssen in einem Excel-Worksheet Daten für eine Organisation und die Monate eines Jahres definiert werden. Die Namen der Worksheets müssen aus zwei Teilen bestehen. Die ersten vier Ziffern bedeuten das Jahr (z.B. 2016) und die restlichen Buchstaben müssen den Namen der Organisation darstellen. In der WebBSC Demo steht zum Beispiel das Worksheet “2016KARG“ für die Kennzahlwerte der Jahres 2016 für die Organisation KARG = Karton Graz. KARG ist in diesem Fall ist eine frei gewählte Abkürzung.

![worksheet.png](../_uploads/worksheet.png)

**Aufbau und Struktur eines Worksheets in der Uploaddatei:**

Die Excel-Worksheets einer Uploaddatei haben ein fixes Format.

*Spalten:*

* In der 1. Spalte steht immer der Namen der Kennzahl.

* In der nächsten Spalte (in der zweiten Spalte) steht Planwert der Kennzahl für den Monat Jänner.

* In der dritten Spalte steht der Istwert der Kennzahl für den Monat Jänner.

* In der vierten Spalte steht der Planwert und in der fünften der Istwert der Kennzahl für den Monat Februar.

* usw.

* In der Spalte vierundzwanzig steht der Planwert und in der Spalte fünfundzwanzig der Istwert der Kennzahl für den Monat Dezember. Weitere Spalten werden ignoriert.

*Zeilen:*

* Die Kennzahlen müssen in den Zeilen 7 bis 300 stehen

* Es können auch Leerzeilen dazwischen vorhanden sein.

* Die ersten 6 Zeilen und die Zeilen nach der Zeile 300 werden vom System ignoriert.

* In der WebBSC müssen alle Kennzahlen vorhanden sein, die in der ersten Spalte der Uploaddatei vorkommen.

Das Programm ersetzt beim Datenupload immer alle eingelesenen Werte für jede eingelesene Kennzahl entsprechend dem Namen des Worksheets für den Monat entsprechend der Spalte, in der der Wert im Worksheet steht. D.h. wenn nur Werte für den Monat Juni des aktuellen Jahres eingebracht werden sollen, brauchen nur die Werte für Juni (Plan- und/oder Istwert) in der Uploaddatei angegeben werden. Leere Zellen (Zellen mit Nullwerten) führen zu keinen Veränderungen für die entsprechenden Monate in der WebBSC.

![data_upload.png](../_uploads/data_upload.png)

*Mehrere Upload-Dateien:* 

Für unterschiedliche Kennzahlen, Organisationsbereiche oder Zeitperioden können unterschiedliche Uploaddateien oder auch mehrere Worksheets in einer Uploaddatei verwendet werden. Entscheidend ist immer nur die Bezeichnung des Worksheets in der Uploaddatei und dessen Aufbau und Inhalt.

*Empfehlung:*

Es ist zu empfehlen, dass alle Uploaddateien lokal gesichert werden. Damit kann man jederzeit, auch wenn Kennzahlen mit Ihren Werten im System irrtümlich gelöscht worden sein sollten, der gesamte Datenbestand in der WebBSC wieder hergestellt werden.
