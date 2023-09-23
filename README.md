# Drone School Simulator

## Overview
The Drone Simulator is a basic user interface (UI) application designed to mimic the controls and telemetry readings of a drone. Users can monitor real-time telemetry such as speed, heading, and altitude, and also set desired parameters for the drone's autopilot system.

## Features
1. **Telemetry Readings**: Real-time display of the drone's:
   - Speed
   - Heading
   - Altitude

2. **Autopilot Settings**: Allows users to set desired values for:
   - Speed
   - Heading
   - Altitude

3. **Toggles**: Activate or deactivate certain drone functionalities:
   - Landing Gear
   - Auto Land
   - Deploy Load

   Each toggle has an LED-like indicator to show its current status (red for inactive, green for active).

## How to Use
1. **Setting Desired Telemetry**: Enter the desired values for speed, heading, and altitude in the provided entry boxes and click the "Apply" button.

2. **Toggling Features**: Click on the respective buttons to toggle the Landing Gear, Auto Land, or Deploy Load features.

3. **Monitoring Real-time Telemetry**: The real-time values for speed, heading, and altitude are displayed on the left section of the UI. These values smoothly approach the user-set values to simulate real-world drone behavior.

## Dependencies
- Python (with `tkinter` library)

## Installation and Running
1. Ensure Python and `tkinter` are installed.
2. Execute the `drone_school_simulator.py` script:
