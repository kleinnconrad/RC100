# Hobbywing QuicRun 120A ESC


## Table of Contents
* [1. Throttle Range Calibration](#1-throttle-range-calibration)
  * [1.1 Preparation of the Transmitter](#11-preparation-of-the-transmitter)
  * [1.2 Performing the Calibration](#12-performing-the-calibration)
* [2. Parameterization of the "Punch" (Start Mode) via LED Program Card](#2-parameterization-of-the-punch-start-mode-via-led-program-card)
  * [2.1 Connecting the Program Card](#21-connecting-the-program-card)
  * [2.2 Setting the Parameter](#22-setting-the-parameter)
* [3. Ensure Correct Polarity of the Motor](#3-ensure-correct-polarity-of-the-motor)
* [4. ESC Programming](#4-esc-programming)


## 1. Throttle Range Calibration

### 1.1 Preparation of the Transmitter
* Set the Throttle Trim to the value 0 (Neutral).
* Set End Point Adjustment (EPA) for throttle and brake to 100%.
* ABS braking functions must be disabled.
* Check throttle channel inversion (usually "REV" for Futaba systems, "NOR" for other manufacturers).
* Turn on the transmitter.

### 1.2 Performing the Calibration
1. Connect the drive battery to the switched-off ESC.
2. Press and hold the SET button on the ESC.
3. Turn on the ESC using the main switch.
4. As soon as the red status LED starts flashing, release the SET button immediately.
5. **Neutral point:** Leave the throttle trigger in the neutral position. Press the SET button once. The green LED flashes once for confirmation.
6. **Full throttle endpoint:** Pull the throttle trigger to the maximum forward position (full throttle) and hold it at the mechanical stop. Press the SET button once. The green LED flashes twice.
7. **Full brake endpoint:** Push the throttle trigger to the maximum reverse position (full brake) and hold it at the mechanical stop. Press the SET button once. The green LED flashes three times.
8. Return the throttle trigger to the neutral position. The ESC completes the initialization process after approx. three seconds and is ready for operation.

---

## 2. Parameterization of the "Punch" (Start Mode) via LED Program Card

### 2.1 Connecting the Program Card
1. Make sure the ESC is turned off.
2. Plug the connection cable of the program card into the dedicated PRG port (3-pin) of the ESC.
3. Strictly observe polarity: The ground cable (black/brown) must be connected to the negative pole (-), the signal cable (white/orange) to the signal pole (S/P).
4. Connect the opposite end of the cable to the program card.

### 2.2 Setting the Parameter
1. Connect the drive battery and turn on the ESC. The numeric segment display of the program card is activated.
2. Iteratively press the **ITEM** button until the parameter for "Start Mode / Punch" (usually menu item 4) is displayed on the left display field.
3. Press the **VALUE** button to specify the numeric value.
   * *Note for the present high-load gear ratio (43/72):* Value must absolutely be set to **1 (Soft)** to minimize critical inrush currents (stall currents) and prevent triggering of the overcurrent protection circuit.
4. Press the **OK** button to write the changed value into the non-volatile memory of the ESC. (Motor usually gives an acoustic confirmation signal).
5. Turn off the ESC and disconnect the physical connection to the program card.

## 3. Ensure Correct Polarity of the Motor
The fit of the motor in the Carten requires an inverse polarity compared to the standard so that technical and physical direction of movement are congruent. The technical directions of rotation are controlled differently, so that purely inverting on the remote control is not sufficient.

## 4. ESC Programming

| Item | Programmable Items | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 | Option 6 | Option 7 | Option 8 | Option 9 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Running Mode | Forward with brake | **(Forward / Reverse with Brake)** | Forward with reverse | | | | | | |
| 2 | Cutoff Voltage | Disabled | 2.6V/Cell | 2.8V/Cell | **(3.0V/Cell)** | 3.2V/Cell | 3.4V/Cell | | | |
| 3 | Punch | **(Level 1)** | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 | Level 7 | Level 8 | Level 9 |
| 4 | Drag Brake Force | **(0%)** | 5% | 10% | 20% | 40% | 60% | 80% | 100% | |
| 5 | Max. Brake Force* | **(25%)** | 50% | 75% | 100% | Disabled | | | | |
| 6 | Max. Reverse Force | **(25%)** | 50% | 75% | 100% | | | | | |
| 7 | Neutral Range | 6% | **(9%)** | 12% | | | | | | |
| 8 | Timing | 0° | 3.75° | 7.5° | **(11.25°)** | 15° | 18.75° | 22.5° | 26.25° | |
| 9 | LiPo Cells* | **(Auto)** | 2S | 3S | 4S | 5S | 6S | | | |
| 10 | BEC Voltage | **(6.0V)** | 7.4V | | | | | | | |

![Program Card ESC](https://github.com/kleinnconrad/RC100/blob/main/photos/PXL_20260319_093605867.jpg)
