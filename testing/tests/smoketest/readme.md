# Smoke test


## Table of contents
* [Current setup](#current-setup)
* [Test report & problem description](#test-report--problem-description)
* [Solution & next steps](#solution--next-steps)


## Current setup
* **Motor:** 3660 brushless
* **Specification:** 3700 KV
* **Pinion:** 43 teeth (43T)
* **ESC punch level:** 5 (default)

## Test report & problem description
During the initial smoke test, it became apparent that the **punch (start behavior/acceleration aggressiveness) was set too hard**. 
Due to the combination of the 3660 / 3700 KV motorization and the 43T gear ratio, the vehicle is difficult to start with the standard punch level of 5.

## Solution & next steps
* **Measure:** Order a hobbywing programming card.
* **Goal:** Significantly reduce the punch value via the ESC to ensure a smoother starting behavior and better control.
