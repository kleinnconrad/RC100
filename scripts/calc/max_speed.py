import math

def calculate_max_speed():
    print("="*75)
    print(" 🚀 Carten T410R Real-World Top-Speed Rechner v3.0 🚀")
    print("="*75)
    
    try:
        kv = float(input("Motor kV (z.B. 4000 oder 3700): "))
        cells = int(input("LiPo Zellen (z.B. 3 für 3S): "))
        diameter_mm = float(eval(input("Reifen-Durchmesser in mm (z.B. 65): ")))
        
        motor_size = input("Motor Baugröße (3650 oder 3660): ").strip()
        if motor_size == "3660":
            max_load = 25.0  # Erhöhtes Limit für den größeren Motor
        else:
            max_load = 22.0  # Standard-Limit
            motor_size = "3650 (Standard)"
            
    except Exception as e:
        print(f"Eingabefehler: {e}")
        return

    print(f"\n-> Setze thermisches Limit für {motor_size} Motor automatisch auf {max_load} % Radlast.")

    v_max = cells * 4.2  
    v_nom = cells * 3.7  

    spur_gear = 72
    internal_ratio = 2.47
    
    rpm_max = kv * v_max
    rpm_nom = kv * v_nom
    circumference_m = (diameter_mm * math.pi) / 1000.0

    best_safe_pinion = None
    best_safe_speed_nom = 0
    best_safe_speed_max = 0
    best_safe_ratio = 0
    best_safe_load = 0

    absolute_max_pinion = 44
    abs_ratio = (spur_gear / absolute_max_pinion) * internal_ratio
    abs_load = (1 / abs_ratio) * 100
    abs_speed_nom = ((rpm_nom / abs_ratio) * circumference_m * 60) / 1000.0
    abs_speed_max = ((rpm_max / abs_ratio) * circumference_m * 60) / 1000.0

    for pinion in range(21, 45):
        gear_ratio = (spur_gear / pinion) * internal_ratio
        load_pct = (1 / gear_ratio) * 100
        
        if load_pct <= max_load:
            speed_nom = ((rpm_nom / gear_ratio) * circumference_m * 60) / 1000.0
            speed_max = ((rpm_max / gear_ratio) * circumference_m * 60) / 1000.0
            
            if speed_nom > best_safe_speed_nom:
                best_safe_speed_nom = speed_nom
                best_safe_speed_max = speed_max
                best_safe_pinion = pinion
                best_safe_ratio = gear_ratio
                best_safe_load = load_pct

    print("\n" + "="*75)
    print(" 🔋 MOTOR & AKKU DATEN")
    print("="*75)
    print(f"Akku unter Last:      {v_nom:.1f} V (Realistischer Voltage Sag)")
    print(f"Motor-U/min (Last):   {rpm_nom:,.0f} U/min".replace(',', '.'))
    
    if best_safe_pinion:
        print("\n✅ THERMISCH SICHERS MAXIMUM (Auf der Straße)")
        print(f"Optimales Ritzel:     {best_safe_pinion} Zähne (Ratio: {best_safe_ratio:.2f})")
        print(f"Tatsächliche Last:    {best_safe_load:.1f} % (Limit war {max_load} %)")
        print(f"Realer Top-Speed:     {best_safe_speed_nom:.1f} km/h")
    else:
        print("\n❌ Kein Ritzel gefunden, das unter der angegebenen Radlast bleibt!")

    print("\n💀 ABSOLUTES CHASSIS-LIMIT (44Z - Vorsicht!)")
    print(f"Tatsächliche Last:    {abs_load:.1f} %")
    print(f"Realer Top-Speed:     {abs_speed_nom:.1f} km/h")
    print("="*75)

if __name__ == '__main__':
    calculate_max_speed()
