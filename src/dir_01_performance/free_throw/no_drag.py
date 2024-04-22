import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 0.4  # Mass in kilograms
h = 0.75  # Initial height in meters
g = 9.81  # Acceleration due to gravity in m/s²

# Initial conditions
v0 = 6  # Initial velocity in m/s
launch_angle = 30  # Launch angle in degrees
v0x = v0 * np.cos(np.radians(launch_angle))  # Horizontal velocity
v0y = v0 * np.sin(np.radians(launch_angle))  # Vertical velocity

# Time of flight
time_of_flight = (v0y + np.sqrt(v0y**2 + 2 * g * h)) / g

# Time intervals for plotting
t = np.linspace(0, time_of_flight, num=100)  # Creating time steps

# Equations of motion
x = v0x * t  # Horizontal position
y = h + v0y * t - 0.5 * g * t**2  # Vertical position

# Plotting the trajectory
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title('Projectile motion without air resistance')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.show()
