# Ideas for Follow-up Projects

**Sensors/Telemetry** [![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kleinnconrad/carten_telemetrie)
* Microcontroller/sensor solution for measuring ESC and motor temperature and the speed at the driveshaft. 

**IoT Cloud Data Platform** [![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/kleinnconrad/carten_telemetrie)
* Setup of a real-time streaming pipeline (ESP32 via LTE) for GPS and ESC telemetry.
* Implementation of a cloud infrastructure for scalable storage and processing of vehicle data.
* Live dashboarding for real-time performance analysis during speedruns.

**Hardware Scaling**
* Dual motor configuration for the Carten T410R chassis (CAD project).

**Data Analytics (GPS and ESC Telemetry)**
* Development of a regression model to estimate the real speed from ESC telemetry data.
* Structured evaluation of relevant experiments and speedrun test runs.
* Derivation of data-driven optimization approaches for maximum battery efficiency and absolute top speed.

**Assistance Systems**
* Integration of hardware and software for assisted driving with the Carten T410R.

**Predictive Maintenance**
* Development of a model for predicting thermal limits (motor/ESC) based on load profiles, RPM and ambient temperature.
* Long-term analysis of voltage sag under full load for data-driven evaluation of battery degradation (state of health).

**Computer Vision & FPV Systems**
* Integration of an FPV camera system with On-Screen-Display (OSD) for overlaying relevant live telemetry (speed, temperatures, battery level).
* Implementation of camera-based environment detection (e.g. via Raspberry Pi) to expand the assistance systems with lane detection and obstacle avoidance.
