import matplotlib.pyplot as plt
import numpy as np
import math

def plot_dashboard():
    # 1. Konstanten & Eingabedaten für 3660 Motor (3700KV an 3S)
    motor_kv = 3700
    akku_v = 11.1
    spur_gear = 72
    internal_ratio = 2.47
    tire_diameter_mm = 65.0

    # 2. Berechnungen
    pinions = np.arange(21, 45)
    fdr = (spur_gear / pinions) * internal_ratio
    radlast = (1 / fdr) * 100
    motor_rpm = motor_kv * akku_v
    achsdrehzahl = motor_rpm / fdr

    # 3. Plot-Setup
    fig, ax1 = plt.subplots(figsize=(10, 7))

    # Y-Achse 1: Radlast (Blau)
    color1 = 'tab:blue'
    ax1.set_xlabel('Ritzelgröße (Zähne)', fontsize=12)
    ax1.set_ylabel('Radlast (%)', color=color1, fontsize=12)
    line1, = ax1.plot(pinions, radlast, color=color1, label='Radlast (%)', linewidth=2, marker='o')
    ax1.tick_params(axis='y', labelcolor=color1)

    # Y-Achse 2: Achsdrehzahl (Rot)
    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel('Achsdrehzahl (U/min) bei Vollgas', color=color2, fontsize=12)
    line2, = ax2.plot(pinions, achsdrehzahl, color=color2, label='Achsdrehzahl', linewidth=2, marker='x')
    ax2.tick_params(axis='y', labelcolor=color2)

    # 4. Mehrere Ziellinien (100, 110, 120, 130) als Baseline einzeichnen
    circumference_m = (tire_diameter_mm * math.pi) / 1000.0
    target_speeds = [100.0, 110.0, 120.0, 130.0]
    line_colors = ['black', '#4a4a4a', '#7a7a7a', '#a3a3a3']
    target_lines = []

    for speed, color in zip(target_speeds, line_colors):
        target_rpm = (speed * 1000.0 / 60.0) / circumference_m
        # Die 100 km/h Linie leicht dicker machen, um sie als Primärziel hervorzuheben
        lw = 2 if speed == 100.0 else 1.5
        line = ax2.axhline(target_rpm, color=color, linestyle='--', linewidth=lw, 
                           label=f'{int(speed)} km/h Ziel (~{int(target_rpm)} U/min)')
        target_lines.append(line)

    # 5. Thermische Zonen für 3660 Motor (Hintergrundfarben)
    ax1.axhspan(10, 22.0, color='green', alpha=0.15)
    ax1.axhspan(22.0, 25.0, color='yellow', alpha=0.15)
    ax1.axhspan(25.0, 28.0, color='red', alpha=0.15)

    # Text-Labels für Zonen
    ax1.text(21.5, 16, '🟢 Safe Zone (< 22%)', color='darkgreen', fontsize=11, fontweight='bold')
    ax1.text(21.5, 23.5, '🟡 Sweet Spot (22% - 25%)', color='olive', fontsize=11, fontweight='bold')
    ax1.text(21.5, 26.5, '🔴 Gefahrenzone (> 25%)', color='darkred', fontsize=11, fontweight='bold')

    # Achsen-Limits und Styling
    ax1.set_ylim(10, 28)
    ax1.set_xlim(20.5, 44.5)
    ax1.set_xticks(np.arange(21, 45, 2))

    # Führt alle Legenden zusammen
    lines = [line1, line2] + target_lines
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=9)

    plt.title('Antriebs-Dashboard: Carten T410R (Erweiterte Speed-Ziele)', fontsize=14, fontweight='bold')
    fig.tight_layout()
    ax1.grid(True, linestyle=':', alpha=0.7)

    # Bild speichern
    filename = 'antriebs_plot_multi_speed.png'
    plt.savefig(filename, dpi=300)
    print(f"✅ Dashboard erfolgreich als '{filename}' gespeichert.")

if __name__ == '__main__':
    plot_dashboard()
