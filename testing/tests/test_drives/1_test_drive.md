# Test log: 1. Test drive

## Table of contents
* [Metadata](#metadata)
* [Goal of the test drive](#goal-of-the-test-drive)
* [Test course and result](#test-course-and-result)
* [Error pattern and problems encountered](#error-pattern-and-problems-encountered)
* [Planned measures](#planned-measures)
* [Implemented adjustments](#implemented-adjustments)

## Metadata
* **Date:** 2026-03-17
* **Focus:** Exploration
* **Status:** Failed (test aborted).

## Goal of the test drive
No special findings.

## Test course and result
No special findings.

## Error pattern and problems encountered
* **Critical assembly error (drivetrain):** The grub screw of the motor pinion was insufficiently fixed (or not correctly positioned on the flat spot of the motor shaft). Due to the high centrifugal forces and vibrations, the hard steel pinion slipped forward on the shaft.
* **Total loss of gearbox:** The slipping led to an asymmetrical engagement of the gears. The main gear (spur gear) made of plastic was completely shaved off/destroyed as a result. At the same time, the bore of the motor pinion deformed irreparably due to the extreme leverage and spinning on the shaft.

* **Punch set too high for the tall gear ratio:**
The motor could not or hardly start with the gear ratio of 43 to 72 teeth and a punch of 5. **It is absolutely necessary to set the punch to 1 and slightly push the vehicle to start**. During the test drive, the ESC often went into emergency shutdown when starting.

* **Motor polarity reversed:**
The chosen polarity (technical forward gear) did not correspond to the physical forward gear. Assuming the rotation directions were commutative, the throttle setting on the remote control was set to "REV" during the test drive. This caused the car to drive forward in the technical reverse gear. This explains the difficult starting in addition to the punch and the tall gear ratio.

## Planned measures
1. Procurement of a new 48DP motor pinion made of hardened steel (5mm bore).
2. Procurement of an upgrade main gear (e.g. Kimbrough 72T 48DP) compatible with the Carten T410R hub.
3. Secure mounting of the new pinion with medium strength threadlocker (Loctite).
4. Recalibration of the hobbywing ESC to the carson remote control (teach mechanical endpoints).
5. Absolutely set punch to 1.
6. Push the vehicle slightly when starting to prevent emergency shutdowns of the ESC.
7. Reverse motor polarity.

## Implemented adjustments
No special findings.
