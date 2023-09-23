import tkinter as tk
from tkinter import ttk
import random

class DroneSchool:

    def __init__(self, root):
        self.root = root
        self.root.title("Drone Simulator")

        self.speed = 0
        self.heading = 0
        self.altitude = 0

        self.target_speed = 0
        self.target_heading = 0
        self.target_altitude = 0

        self.landing_gear_status = False
        self.auto_land_status = False
        self.deploy_load_status = False

        # UI Setup
        self.setup_ui()

        self.root.after(500, self.update_telemetry)

    def setup_ui(self):
        # LED Status Lights for Toggles
        self.landing_gear_led = ttk.Label(self.root, text='●', foreground='red')
        self.auto_land_led = ttk.Label(self.root, text='●', foreground='red')
        self.deploy_load_led = ttk.Label(self.root, text='●', foreground='red')

        self.landing_gear_led.grid(row=4, column=1)
        self.auto_land_led.grid(row=5, column=1)
        self.deploy_load_led.grid(row=6, column=1)

        ttk.Label(self.root, text="Telemetry").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.root, text="Autopilot").grid(row=1, column=2, padx=10, pady=10)

        # Telemetry Data
        ttk.Label(self.root, text="Speed:").grid(row=2, column=0)
        ttk.Label(self.root, text="Heading:").grid(row=3, column=0)
        ttk.Label(self.root, text="Altitude:").grid(row=4, column=0)

        self.speed_label = ttk.Label(self.root, text="0 mph")
        self.heading_label = ttk.Label(self.root, text="0 °")
        self.altitude_label = ttk.Label(self.root, text="0 feet")

        self.speed_label.grid(row=2, column=1)
        self.heading_label.grid(row=3, column=1)
        self.altitude_label.grid(row=4, column=1)

        # Autopilot Input
        ttk.Label(self.root, text="Set Speed:").grid(row=2, column=2)
        ttk.Label(self.root, text="Set Heading:").grid(row=3, column=2)
        ttk.Label(self.root, text="Set Altitude:").grid(row=4, column=2)

        self.speed_input = ttk.Entry(self.root)
        self.heading_input = ttk.Entry(self.root)
        self.altitude_input = ttk.Entry(self.root)

        self.speed_input.grid(row=2, column=3)
        self.heading_input.grid(row=3, column=3)
        self.altitude_input.grid(row=4, column=3)

        # Toggles
        self.landing_gear_btn = ttk.Button(self.root, text="Landing Gear", command=self.toggle_landing_gear)
        self.auto_land_btn = ttk.Button(self.root, text="Auto Land", command=self.auto_land)
        self.deploy_load_btn = ttk.Button(self.root, text="Deploy Load", command=self.deploy_load)

        self.landing_gear_btn.grid(row=5, column=2)
        self.auto_land_btn.grid(row=5, column=3)
        self.deploy_load_btn.grid(row=6, column=2, columnspan=2)

        # Apply Autopilot Settings
        self.apply_btn = ttk.Button(self.root, text="Apply", command=self.apply_settings)
        self.apply_btn.grid(row=7, column=2, columnspan=2)

    def update_telemetry(self):
        self.speed += (self.target_speed - self.speed) / 10 + random.uniform(-0.2, 0.2)
        self.heading += (self.target_heading - self.heading) / 10 + random.uniform(-0.2, 0.2)
        self.altitude += (self.target_altitude - self.altitude) / 10 + random.uniform(-0.2, 0.2)

        self.speed_label["text"] = f"{self.speed:.2f}"
        self.heading_label["text"] = f"{self.heading:.2f}"
        self.altitude_label["text"] = f"{self.altitude:.2f}"

        self.root.after(500, self.update_telemetry)

    def apply_settings(self):
        self.target_speed = float(self.speed_input.get())
        self.target_heading = float(self.heading_input.get())
        self.target_altitude = float(self.altitude_input.get())

    def toggle_landing_gear(self):
        self.landing_gear_status = not self.landing_gear_status
        self.landing_gear_led['foreground'] = 'green' if self.landing_gear_status else 'red'
        print("Toggled Landing Gear!")

    def auto_land(self):
        self.auto_land_status = not self.auto_land_status
        self.auto_land_led['foreground'] = 'green' if self.auto_land_status else 'red'
        self.target_altitude = 0
        print("Auto Landing!")

    def deploy_load(self):
        self.deploy_load_status = not self.deploy_load_status
        self.deploy_load_led['foreground'] = 'green' if self.deploy_load_status else 'red'
        print("Deployed Load!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DroneSchool(root)
    root.mainloop()
