# Smoke Test


## Table of Contents
* [Current Setup](#current-setup)
* [Test Report & Problem Description](#test-report--problem-description)
* [Solution & Next Steps](#solution--next-steps)


## Current Setup
* **Motor:** 3660 Brushless
* **Specification:** 3700 KV
* **Pinion:** 43 Teeth (43T)
* **ESC Punch Level:** 5 (Default)

## Test Report & Problem Description
During the initial smoke test, it became apparent that the **punch (start behavior/acceleration aggressiveness) was set too hard**. 
Due to the combination of the 3660 / 3700 KV motorization and the 43T gear ratio, the vehicle is difficult to start with the standard punch level of 5.

## Solution & Next Steps
* **Measure:** Order a Hobbywing programming card.
* **Goal:** Significantly reduce the punch value via the ESC to ensure a smoother starting behavior and better control.
