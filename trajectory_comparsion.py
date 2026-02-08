"""
trajectory_comparison.py

This file compares projectile motion under three conditions:
1. Ideal motion (no forces)
2. Motion under gravity only
3. Motion with gravity and air resistance

The trajectories are plotted to visualize the differences.
"""
import math
import matplotlib.pyplot as plt

# --------------------
# CONSTANTS
# --------------------
g = 9.81
rho = 1.225
Cd = 0.5
r = 0.05
A = math.pi * r**2
m = 1.0
dt = 0.01

v0 = 30
angle = 45
theta = math.radians(angle)

# --------------------
# CASE 1: NO GRAVITY, NO DRAG
# --------------------
x = y = 0.0
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)
traj_no_force = []

for _ in range(300):
    x += vx * dt
    y += vy * dt
    traj_no_force.append((x, y))

# --------------------
# CASE 2: GRAVITY ONLY
# --------------------
x = y = 0.0
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)
traj_gravity = []

while y >= 0:
    vy -= g * dt
    x += vx * dt
    y += vy * dt
    traj_gravity.append((x, y))

# --------------------
# CASE 3: GRAVITY + DRAG
# --------------------
x = y = 0.0
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)
traj_drag = []

while y >= 0:
    v = math.sqrt(vx**2 + vy**2)
    Fd = 0.5 * rho * Cd * A * v**2

    if v != 0:
        Fdx = -Fd * vx / v
        Fdy = -Fd * vy / v
    else:
        Fdx = Fdy = 0

    ax = Fdx / m
    ay = -g + Fdy / m

    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt

    traj_drag.append((x, y))

# --------------------
# PLOTTING
# --------------------
def split(traj):
    return [p[0] for p in traj], [p[1] for p in traj]

x1, y1 = split(traj_no_force)
x2, y2 = split(traj_gravity)
x3, y3 = split(traj_drag)

plt.figure()
plt.plot(x1, y1, label="No Gravity / No Drag")
plt.plot(x2, y2, label="Gravity Only")
plt.plot(x3, y3, label="Gravity + Air Drag")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Trajectory Comparison Under Different Forces")
plt.legend()
plt.grid(True)
plt.show()
