# Build Log - Carten T410R Speedrun Projekt

## Tag 1 - Mechanische Grundstruktur & Fahrwerk
**Datum:** 14.03.2026
**Status:** Erledigt

## Fortschritt & Technische Erkenntnisse

* **Differential-Setup:** Die Differentiale wurden gemäß der Baukastenanleitung vorerst komplett leer gelassen (ungesperrt). 
  > **Note für spätere Iterationen:** Bei den ersten Testläufen muss das Ausbrechverhalten überwacht werden. Für strikte 100 km/h Geradeausläufe könnte es später notwendig sein, zumindest das vordere Differential mit extrem zähem Silikonöl (z.B. 100.000 cSt bis 1.000.000 cSt) teilweise zu sperren, um ein "Ausbluten" der Leistung an ein einzelnes Rad zu verhindern.

* **Fahrwerk & Dämpfer-Kalibrierung:** Die Öldruckstoßdämpfer wurden ganz bewusst weich abgestimmt. Ziel dieses Setups ist es, sicherzustellen, dass das Fahrzeug bei kleinen Unebenheiten auf unpräpariertem Parkplatz-Asphalt den Bodenkontakt hält und nicht zu springen beginnt (Gefahr von Aerodynamik-Abriss).
  Beim Befüllen wurde strikte Qualitätskontrolle angewandt: Es wurde darauf geachtet, jegliche Luftblasen aus dem Öl zu ziehen, um ein "Emulgieren" und damit ein unvorhersehbares Dämpfungsverhalten zu vermeiden.

* **Montage-Optimierung (Kunststoff-Gewinde):** Die harten M3-Industrieschrauben ließen sich anfangs nur mit hohem Widerstand in die neuen Kunststoffteile eindrehen (Gefahr von Materialermüdung oder beschädigten Schraubenköpfen).
  > **Lösung:** Durch das Applizieren einer minimalen Menge Dämpferöl in die Bohrungen konnte der Reibungswiderstand drastisch reduziert werden. Die Schrauben ließen sich danach sauber und materialschonend eindrehen.

* **Antriebsstrang:** Für die Lagerung der drehenden Massen wurden die beiliegenden Baukasten-Standardkugellager verwendet und im gesamten Antriebsstrang implementiert.

## Visuelle Dokumentation

![Mechanik Aufbau Detail 1](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260313_223025406.jpg?raw=true)
![Mechanik Aufbau Detail 2](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260313_223029415.jpg?raw=true)
![Mechanik Aufbau Detail 3](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260313_223034370.jpg?raw=true)

## Tag 2 - Fahrwerksgeometrie, Lenkung & Elektronik-Prep
**Datum:** 15.03.2026
**Status:** Erledigt

## Fortschritt & Technische Erkenntnisse

* **Radstand & Fahrwerksgeometrie:** An der Hinterradaufhängung wurden 3mm Spacer in Richtung Vorderrad verbaut. Dies kalibriert den Radstand exakt auf die vom Hersteller vorgesehenen 258 mm. 
  > **Technische Erkenntnis:** Ein Verbauen der Spacer in Richtung Heck würde den Radstand auf 255 mm verkürzen. Durch diese Anpassbarkeit lässt sich das Chassis bei Bedarf perfekt in den Radkästen der Karosserie zentrieren.

* **Montage der Stabilisatoren (Interimslösung):** Die im Baukasten mitgelieferten Madenschrauben (kopflose Schrauben) für die Stabilisatoren erwiesen sich als zu klein/kurz. 
  > **Workaround:** Interimsweise wurde auf reguläre M3x6 Schrauben ausgewichen. Dies ist mechanisch absolut unbedenklich und erfüllt den Zweck, entspricht jedoch nicht der finalen ästhetischen Zielsetzung.

* **Lenk-Infrastruktur:** Das Amewi-Lenkservo wurde vor dem Einbau elektronisch in die absolute Neutralstellung ("genullt") gebracht. Dies ist ein kritischer Schritt, um später bei 100 km/h asymmetrische Lenkausschläge und einen schiefen Geradeauslauf zu verhindern. Anschließend wurde das Servo final im Chassis verbaut.

* **Kunststoff-Toleranzen (Kugelgelenke):** Die Kugelgelenkaufnahmen (Kugelpfannen) weisen extrem enge Toleranzen auf und sind von Werk aus sehr klein dimensioniert. 
  > **Lösung:** Um die Kugelköpfe einzupassen, ohne das Material durch Kaltverformung zu überlasten oder Risse im Kunststoff zu riskieren, wurden die Aufnahmen vor der Montage leicht erhitzt. 

* **Energie-Management:** Der Absima 3S LiPo-Akku wurde zur Akkupflege und Sicherheit an das Ladegerät angeschlossen und auf Lagerspannung (Storage-Spannung, ca. 3.8V pro Zelle) gebracht, bis der Antriebsstrang final verkabelt und einsatzbereit ist.

## Visuelle Dokumentation

![Fahrwerksgeometrie & Lenkung Detail 1](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260314_163940602.jpg?raw=true)
![Fahrwerksgeometrie & Lenkung Detail 2](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260314_163954210.jpg?raw=true)
![Fahrwerksgeometrie & Lenkung Detail 3](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260314_164003786.jpg?raw=true)
![Fahrwerksgeometrie & Lenkung Detail 4](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260314_164056785.jpg?raw=true)
![Fahrwerksgeometrie & Lenkung Detail 5](https://github.com/kleinnconrad/RC100/blob/main/mechanik/fotos/PXL_20260314_170154252.jpg)
