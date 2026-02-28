import math

def calculate_max_speed():
    print("="*75)
    print(" 🚀 Carten T410R Top-Speed & Limit Rechner 🚀")
    print("="*75)
    
    try:
        kv = float(input("Motor kV (z.B. 4000): "))
        volts = float(input("Akku Spannung unter Last in V (z.B. 11.1 für 3S): "))
        diameter_mm = float(eval(input("Reifen-Durchmesser in mm (z.B. 65): ")))
        max_load = float(input("Maximal tolerierte Radlast in % (z.B. 22.0 für Sweet Spot, 25.0 für Limit): "))
    except Exception as e:
        print(f"Eingabefehler oder Formel-Fehler: {e}")
        return

    # Konstanten für den Carten T410R laut Handbuch
    spur_gear = 72
    internal_ratio = 2.47
    
    # Maximale Motordrehzahl berechnen
    max_rpm = kv * volts
    circumference_m = (diameter_mm * math.pi) / 1000.0

    best_safe_pinion = None
    best_safe_speed = 0
    best_safe_ratio = 0
    best_safe_load = 0

    # Absolutes Limit des Chassis (44Z Ritzel laut Carten Tabelle)
    absolute_max_pinion = 44
    abs_ratio = (spur_gear / absolute_max_pinion) * internal_ratio
    abs_load = (1 / abs_ratio) * 100
    abs_axle_rpm = max_rpm / abs_ratio
    abs_speed = (abs_axle_rpm * circumference_m * 60) / 1000.0

    # Iteration durch alle möglichen Ritzel (21Z bis 44Z)
    for pinion in range(21, 45):
        gear_ratio = (spur_gear / pinion) * internal_ratio
        load_pct = (1 / gear_ratio) * 100
        
        # Prüfen, ob das Ritzel noch in deiner Toleranz liegt
        if load_pct <= max_load:
            axle_rpm = max_rpm / gear_ratio
            speed_kmh = (axle_rpm * circumference_m * 60) / 1000.0
            
            # Das größte erlaubte Ritzel finden
            if speed_kmh > best_safe_speed:
                best_safe_speed = speed_kmh
                best_safe_pinion = pinion
                best_safe_ratio = gear_ratio
                best_safe_load = load_pct

    print("\n" + "="*75)
    print(" 🏁 MAXIMAL MÖGLICHE GESCHWINDIGKEITEN")
    print("="*75)
    print(f"Motor-Drehzahl (max): {max_rpm:,.0f} U/min".replace(',', '.'))
    print(f"Radumfang:            {circumference_m * 1000:.1f} mm")
    
    if best_safe_pinion:
        print("\n✅ THERMISCH SICHERS MAXIMUM (Innerhalb deines Limits)")
        print(f"Max. erlaubte Last:   {max_load} %")
        print(f"Optimales Ritzel:     {best_safe_pinion} Zähne (Ratio: {best_safe_ratio:.2f})")
        print(f"Tatsächliche Last:    {best_safe_load:.1f} %")
        print(f"Berechneter Top-Speed:{best_safe_speed:.1f} km/h")
    else:
        print("\n❌ Kein Ritzel gefunden, das unter der angegebenen Radlast bleibt!")

    print("\n💀 ABSOLUTES CHASSIS-LIMIT (Vorsicht: Überhitzungsgefahr!)")
    print(f"Größtes Ritzel:       {absolute_max_pinion} Zähne (Ratio: {abs_ratio:.2f})")
    print(f"Tatsächliche Last:    {abs_load:.1f} %")
    print(f"Theoretischer Speed:  {abs_speed:.1f} km/h")
    print("="*75)

if __name__ == '__main__':
    calculate_max_speed()
