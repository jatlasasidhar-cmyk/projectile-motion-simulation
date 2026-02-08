"""
trajectory_with_drag.py

This file simulates projectile motion with air resistance.
The drag force is proportional to the square of velocity.

Physics model used:
- Gravity
- Quadratic air drag

The trajectory is calculated using numerical time stepping.
"""
import math

# -----------------------------
# CONSTANTS
# -----------------------------
g = 9.81          # gravity (m/s^2)
rho = 1.225       # air density (kg/m^3)
Cd = 0.5          # drag coefficient
r = 0.05          # radius (m)
A = math.pi * r**2
m = 1.0           # mass (kg)
dt = 0.01         # time step

# -----------------------------
# INITIAL CONDITIONS
# -----------------------------
x = 0.0
y = 0.0

v0 = 30.0
angle = 45
theta = math.radians(angle)

vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

# -----------------------------
# STORAGE
# -----------------------------
trajectory = []

# -----------------------------
# SIMULATION LOOP
# -----------------------------
while y >= 0:
    # speed
    v = math.sqrt(vx**2 + vy**2)

    # drag force
    Fd = 0.5 * rho * Cd * A * v**2

    # drag components
    if v != 0:
        Fdx = -Fd * (vx / v)
        Fdy = -Fd * (vy / v)
    else:
        Fdx = 0
        Fdy = 0

    # acceleration
    ax = Fdx / m
    ay = (-g) + (Fdy / m)

    # update velocity
    vx = vx + ax * dt
    vy = vy + ay * dt

    # update position
    x = x + vx * dt
    y = y + vy * dt

    # store
    trajectory.append((x, y))

# -----------------------------
# OUTPUT
# -----------------------------
print("Simulation with drag completed")
print("Total points:", len(trajectory))
print("Final range (m):", trajectory[-1][0])
import matplotlib.pyplot as plt

# Extract x and y values
x_vals = [point[0] for point in trajectory]
y_vals = [point[1] for point in trajectory]

# Plot the trajectory
plt.figure()
plt.plot(x_vals, y_vals)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Projectile Trajectory with Air Drag")
plt.grid(True)
plt.show()
