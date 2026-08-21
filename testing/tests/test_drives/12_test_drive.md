# Report 12. Test Drive

## Table of Contents
- [Basic Data and Setup](#basic-data-and-setup)
- [Results](#results)
- [Measures](#measures)

## Basic Data and Setup
- **Date:** 2026-08-09
- **Location:** Bauhaus
- **Goal:** Checking the straight-line driving behavior during strong acceleration.
- **Background:** Rebuilding the vehicle after a total loss in the 4th speedrun session.
- **Setup changes compared to previous version:**
  - Installation of a front spool.
  - Mounting of 150 g additional weight on the front bumper (added during the test).

## Results
- The optimized chassis geometry did not lead to an improvement in driving behavior at high speeds.
- The installation of the front spool did not improve driving behavior.
- The mounting of the additional weight on the front bumper does not improve driving behavior.
- The vehicle breaks out to the left during strong acceleration. The cause is very likely torque twist due to the high-torque motorization.

## Measures
- Replacement of the motor from a high-torque to a high-speed design (Priority 1). QuicRun 3652SL G2 Sensorless Motor 5400kV 3.175mm Shaft
- Increase in spring stiffness.
- Checking the tires.
- Checking servo and servo saver or steering precision
- Installation of "perfect pass" https://github.com/ambrmart/arduino-rc-launch-control
- Installation of a gyro
