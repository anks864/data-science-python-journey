"""
File: no08_matplotlib_tutorial.py
Topic: Matplotlib Visualization
Description: Covers line plots, multiple plots, bar charts, pie charts, scatter plots, and 3D plots.
"""

import matplotlib.pyplot as plt
import numpy as np

# ==============================
# 1. Line Plot (Sine & Cosine)
# ==============================
x_values = np.linspace(0, 10, 100)
sine_values = np.sin(x_values)
cosine_values = np.cos(x_values)

plt.plot(x_values, sine_values)
plt.xlabel("X Values")
plt.ylabel("Sine")
plt.title("Sine Wave")
plt.show()

plt.plot(x_values, cosine_values)
plt.xlabel("X Values")
plt.ylabel("Cosine")
plt.title("Cosine Wave")
plt.show()


# ==============================
# 2. Multiple Plots
# ==============================
x_multi = np.linspace(-10, 10, 20)
y_square = x_multi ** 2
y_double = x_multi * 2
y_half = x_multi / 2

plt.plot(x_multi, y_square, 'r+')
plt.plot(x_multi, y_double, 'g.')
plt.plot(x_multi, y_half, 'b*')
plt.title("Multiple Functions Plot")
plt.show()


# ==============================
# 3. Bar Plot
# ==============================
languages = ['English', 'Spanish', 'French', 'Latin', 'Bengali']
people_count = [100, 50, 30, 65, 95]

plt.bar(languages, people_count)
plt.xlabel("Languages")
plt.ylabel("Number of People")
plt.title("Language Popularity")
plt.show()


# ==============================
# 4. Pie Chart
# ==============================
plt.pie(people_count, labels=languages, autopct='%1.1f%%')
plt.title("Language Distribution")
plt.show()


# ==============================
# 5. Scatter Plot
# ==============================
x_scatter = np.linspace(0, 10, 30)
y_sin = np.sin(x_scatter)
y_cos = np.cos(x_scatter)

plt.scatter(x_scatter, y_sin)
plt.scatter(x_scatter, y_cos)
plt.title("Scatter Plot (Sin & Cos)")
plt.show()


# ==============================
# 6. 3D Scatter Plot
# ==============================
fig = plt.figure()
ax = plt.axes(projection='3d')

z_vals = 20 * np.random.random(1000)
x_vals = np.sin(z_vals)
y_vals = np.cos(z_vals)

ax.scatter(x_vals, y_vals, z_vals, c=z_vals, cmap='Blues')
plt.title("3D Scatter Plot")
plt.show()


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
