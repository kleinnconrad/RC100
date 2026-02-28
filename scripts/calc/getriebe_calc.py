import math

def calculate_rc_requirements():
    print("="*75)
    print(" 🏎️  Carten T410R Speed & Getriebe Rechner v2.0  🏎️")
    print("="*75)
    
    try:
        # Eingabe als Durchmesser (z.B. 65 oder auch 2*32.5)
        diameter_input = input("Bitte Reifen-Durchmesser in mm eingeben (z.B. 65): ")
        diameter_mm = float(eval(diameter_input))
        
        target_speed_kmh = float(input("Bitte gewünschte Zielgeschwindigkeit in km/h eingeben (z.B. 100): "))
    except Exception as e:
        print(f"Ungültige Eingabe oder Formel-Fehler: {e}")
        return

    # Konstanten für den Carten T410R
    spur_gear = 72
    internal_ratio = 2.47
    pinions = range(21, 45) # Ritzel von 21Z bis 44Z

    # Berechnungen Achse
    circumference_m = (diameter_mm * math.pi) / 1000.0
    speed_m_per_min = (target_speed_kmh * 1000.0) / 60.0
    axle_rpm = speed_m_per_min / circumference_m

    print("\n" + "="*75)
    print(" 📊 ERGEBNISSE DER ACHSE")
    print("="*75)
    print(f"Zielgeschwindigkeit:    {target_speed_kmh} km/h")
    print(f"Reifen-Durchmesser:     {diameter_mm} mm")
    print(f"Radumfang (berechnet):  {circumference_m * 1000:.1f} mm")
    print(f"Benötigte Achsdrehzahl: {axle_rpm:,.0f} U/min".replace(',', '.'))
    
    print("\n" + "="*75)
    print(" ⚙️ MOTOR ANFORDERUNGEN PRO RITZEL (Spur: 72Z)")
    print("="*75)
    print(f"{'Ritzel':<8} | {'Ratio':<6} | {'Motor U/min':<14} | {'Radlast':<8} | {'Belastungs-Zone'}")
    print("-" * 75)

    for pinion in pinions:
        gear_ratio = (spur_gear / pinion) * internal_ratio
        motor_rpm = axle_rpm * gear_ratio
        
        # Drehmoment-Faktor in Prozent (Radlast)
        load_pct = (1 / gear_ratio) * 100

        # Belastungs-Zonen für 4000kV an 3S
        if load_pct < 19.0:
            zone = "🟢 Safe (Strecke & Bashing)"
        elif load_pct < 22.0:
            zone = "🟡 Sweet Spot (100 km/h Runs)"
        elif load_pct <= 25.0:
            zone = "🔴 Gefahrenzone (Extrem-Speed)"
        else:
            zone = "💀 Hitzetod (Überlastung!)"

        # Formatierung und Warnung bei kritischen Drehzahlen
        rpm_str = f"{motor_rpm:,.0f}".replace(',', '.')
        if motor_rpm > 50000:
            rpm_str += " ⚠️"

        print(f"{pinion:<2} Zähne | {gear_ratio:<6.2f} | {rpm_str:<14} | {load_pct:>5.1f} %  | {zone}")

if __name__ == '__main__':
    calculate_rc_requirements()
