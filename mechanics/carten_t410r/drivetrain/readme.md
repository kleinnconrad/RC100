## Drivetrain Dashboard: Speed Targets & Thermal Zones


## Table of Contents
* [Drivetrain Dashboard: Speed Targets & Thermal Zones](#drivetrain-dashboard-speed-targets--thermal-zones)
  * [Reading guide for the dashboard:](#reading-guide-for-the-dashboard)
* [The "Wheel Load %" Formula](#the-wheel-load--formula)
  * [The calculation](#the-calculation)
  * [The load zones (for 3650 motors / 4000kV on 3S)](#the-load-zones-for-3650-motors--4000kv-on-3s)


The following dashboard visualizes the physical limits of the **Carten T410R** in combination with the specified **3660 Brushless Motor (3700KV on 3S)**. 

It shows the direct correlation between the chosen pinion size, the resulting mechanical load (wheel load in %) and the achievable axle speed.

![Drivetrain dashboard with speed targets](https://github.com/kleinnconrad/RC100/blob/main/photos/1772373437236.png)

### Reading guide for the dashboard:
* **The dashed lines (grayscale):** Mark the required axle speed for our milestones (100, 110, 120 and 130 km/h) with a tire diameter of 65 mm.
* **The red curve (axle speed):** Shows the theoretically applied speed of the wheels at full throttle per pinion. Where this curve intersects one of the dashed lines, the respective speed target is reached.
* **The blue curve (wheel load):** Shows the mechanical load of the motor. 
* **The colored zones (background):** Define the thermal tolerance limits of the 3660 motor.
  * 🟢 **Safe Zone (< 22 %):** Continuous load possible without problems.
  * 🟡 **Sweet Spot (22 % - 25 %):** optimal for speedruns, keep an eye on thermal limit.
  *  **Danger Zone (> 25 %):** Acute risk of overheating, only for extreme short sprints.

**Conclusion of the visualization:** The primary project goal of **100 km/h** is achieved from a **35T/36T pinion**. The wheel load is at this point still absolutely safe in the deep green zone. The setup offers mechanical reserves up to approx. 125 km/h.


## The "Wheel Load %" Formula

The **wheel load in percent** calculated in our scripts is an empirical indicator for the mechanical load on the motor. It is based on the reciprocal of the Final Drive Ratio (FDR). 

The smaller the FDR (i.e. the "taller" the gear ratio), the less leverage the motor has. It must consequently apply more raw power to push the car against the exponentially increasing air resistance.

### The calculation
1. **Calculate Final Drive Ratio (FDR):**
   FDR = (Spur gear / Motor pinion) * Internal ratio
   *(On the Carten T410R, the internal ratio is 2.47)*

2. **Calculate wheel load factor:**
   Wheel load (%) = (1 / FDR) * 100

**Example:** With a 72T spur gear and a 36T pinion, the FDR is `(72 / 36) * 2.47 = 4.94`.
The wheel load is thus `(1 / 4.94) * 100 = 20.2 %`.

### The load zones (for 3650 motors / 4000kV on 3S)
These zones have established themselves in practice as guide values for temperature and current monitoring:

* **< 19.0 % (Green Zone):** High leverage. optimal for twisty tracks, stop-and-go and long bashing. Electronics stay cool.
* **19.0 % - 22.0 % (Yellow Sweet Spot):** Ideal balance for speedruns. The car reaches top speed, electronics get very warm, needs cooling down after 1-2 runs.
* **22.0 % - 25.0 % (Red Danger Zone):** Extreme load. Exclusively suitable for short, linear acceleration races with active fan cooling.
* **> 25.0 % (Heat Death):** The leverage is no longer sufficient. The motor draws stalling currents, converts energy almost entirely into heat and risks the immediate destruction of ESC or rotor.
