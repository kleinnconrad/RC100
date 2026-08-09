# Bericht 12. Testfahrt

## Inhaltsverzeichnis
- [Rahmendaten und Setup](#rahmendaten-und-setup)
- [Ergebnisse](#ergebnisse)
- [Maßnahmen](#maßnahmen)

## Rahmendaten und Setup
- **Datum:** 09.08.2026
- **Ort:** Bauhaus
- **Ziel:** Überprüfung des Geradeauslaufverhaltens bei starker Beschleunigung.
- **Hintergrund:** Neuaufbau des Fahrzeugs nach Totalschaden bei der 4. Speedrun-Session.
- **Setup-Änderungen gegenüber Vorversion:**
  - Einbau eines Front Spools.
  - Montage von 150 g Zusatzgewicht am Frontbumper (im Testverlauf hinzugefügt).

## Ergebnisse
- Die optimierte Fahrwerksgeometrie führte zu keiner Verbesserung des Fahrverhaltens bei hohen Geschwindigkeiten.
- Der Einbau des Front Spools bewirkte keine Verbesserung des Fahrverhaltens.
- Die Montage des Zusatzgewichts am Frontbumper bewirkt keine Verbesserung des Fahrverhaltens.
- Das Fahrzeug bricht bei starker Beschleunigung nach links aus. Die Ursache ist sehr wahrscheinlich Torque Twist durch die drehmomentstarke Motorisierung.

## Maßnahmen
- Austausch des Motors von einer drehmomentstarken zu einer drehzahlstarken Auslegung (Priorität 1).
- Einbau von "perfect pass" https://github.com/ambrmart/arduino-rc-launch-control
- Erhöhung der Federhärte.
- Überprüfung der Bereifung.
- Überprüfung von Servo und Servosaver.
