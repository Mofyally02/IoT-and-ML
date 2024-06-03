import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
plt.figure(facecolor='white')

# Add walls
walls = [
    patches.Rectangle((-10, -10), 20, 0.2, linewidth=1, edgecolor='black', facecolor='grey'),  # Bottom wall
    patches.Rectangle((-10, 9.8), 20, 0.2, linewidth=1, edgecolor='black', facecolor='grey'),  # Top wall
    patches.Rectangle((-10, -10), 0.2, 20, linewidth=1, edgecolor='black', facecolor='grey'),  # Left wall
    patches.Rectangle((9.8, -10), 0.2, 20, linewidth=1, edgecolor='black', facecolor='grey')   # Right wall
]

for wall in walls:
    ax.add_patch(wall)

# Add product sections
sections = [
    patches.Rectangle((-7, -7), 4, 4, linewidth=1, edgecolor='blue', facecolor='lightblue', label='Groceries'),
    patches.Rectangle((3, -7), 4, 4, linewidth=1, edgecolor='green', facecolor='lightgreen', label='Electronics'),
    patches.Rectangle((-7, 3), 4, 4, linewidth=1, edgecolor='red', facecolor='lightcoral', label='Apparel'),
    patches.Rectangle((3, 3), 4, 4, linewidth=1, edgecolor='purple', facecolor='plum', label='Checkout')
]

for section in sections:
    ax.add_patch(section)

# Add IoT sensors
sensors = [
    patches.Circle((-5, -5), 0.5, linewidth=1, edgecolor='orange', facecolor='yellow', label='Motion Sensor'),
    patches.Circle((5, -5), 0.5, linewidth=1, edgecolor='orange', facecolor='yellow', label='Motion Sensor'),
    patches.Circle((-5, 5), 0.5, linewidth=1, edgecolor='orange', facecolor='yellow', label='Motion Sensor'),
    patches.Circle((5, 5), 0.5, linewidth=1, edgecolor='orange', facecolor='yellow', label='Motion Sensor'),
    patches.Circle((0, 0), 0.5, linewidth=1, edgecolor='brown', facecolor='brown', label='RFID Tag'),
    patches.Circle((0, -5), 0.5, linewidth=1, edgecolor='brown', facecolor='brown', label='RFID Tag'),
    patches.Circle((0, 5), 0.5, linewidth=1, edgecolor='brown', facecolor='brown', label='RFID Tag'),
    patches.Circle((5, 0), 0.5, linewidth=1, edgecolor='brown', facecolor='brown', label='RFID Tag'),
    patches.Circle((-5, 0), 0.5, linewidth=1, edgecolor='brown', facecolor='brown', label='RFID Tag'),
    patches.Circle((0, 0), 0.5, linewidth=1, edgecolor='black', facecolor='grey', label='Camera'),
    patches.Circle((0, -5), 0.5, linewidth=1, edgecolor='black', facecolor='grey', label='Camera'),
    patches.Circle((0, 5), 0.5, linewidth=1, edgecolor='black', facecolor='grey', label='Camera'),
    patches.Circle((5, 0), 0.5, linewidth=1, edgecolor='black', facecolor='grey', label='Camera'),
    patches.Circle((-5, 0), 0.5, linewidth=1, edgecolor='black', facecolor='grey', label='Camera'),
    patches.Circle((0, 0), 0.5, linewidth=1, edgecolor='green', facecolor='lightgreen', label='Environmental Sensor'),
    patches.Circle((0, -5), 0.5, linewidth=1, edgecolor='green', facecolor='lightgreen', label='Environmental Sensor'),
    patches.Circle((0, 5), 0.5, linewidth=1, edgecolor='green', facecolor='lightgreen', label='Environmental Sensor'),
    patches.Circle((5, 0), 0.5, linewidth=1, edgecolor='green', facecolor='lightgreen', label='Environmental Sensor'),
    patches.Circle((-5, 0), 0.5, linewidth=1, edgecolor='green', facecolor='lightgreen', label='Environmental Sensor')
]

for sensor in sensors:
    ax.add_patch(sensor)

# Add labels
ax.text(-5, -5, 'Groceries', fontsize=12, ha='center')
ax.text(5, -5, 'Electronics', fontsize=12, ha='center')
ax.text(-5, 5, 'Apparel', fontsize=12, ha='center')
ax.text(5, 5, 'Checkout', fontsize=12, ha='center')

# Set limits and title
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_title('Virtual Retail Store Layout with IoT Sensors')

# Add legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys())

plt.show()
print('done')