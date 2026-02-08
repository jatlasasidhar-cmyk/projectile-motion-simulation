"""
trajectory_simulation.py

This file simulates basic projectile motion using numerical methods.
The motion is calculated step by step using the Euler method.
Only gravity is considered, and air resistance is ignored.

Outputs:
- x and y position of the projectile over time
"""
import math

# STEP 1: create storage
trajectory = []

# STEP 2: initial values
x = 0.0
y = 0.0
vx = 10.0
vy = 10.0

g = 9.81
dt = 0.1

# STEP 3: simulation loop
while y >= 0:
    vy = vy - g * dt
    x = x + vx * dt
    y = y + vy * dt

    trajectory.append((x, y))

# STEP 4: output
print("Simulation successful")
print("Points:", len(trajectory))
print(trajectory)
