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
    patches.Rectangle((-7, -7), 4, 4, linewidth=1, edgecolor='blue', facecolor='blue', label='Groceries'),
    patches.Rectangle((3, -7), 4, 4, linewidth=1, edgecolor='green', facecolor='green', label='Electronics'),
    patches.Rectangle((-7, 3), 4, 4, linewidth=1, edgecolor='red', facecolor='coral', label='Apparel'),
    patches.Rectangle((3, 3), 4, 4, linewidth=1, edgecolor='purple', facecolor='plum', label='Checkout')
]

for section in sections:
    ax.add_patch(section)

# Add labels
ax.text(-5, -5, 'Groceries', fontsize=12, ha='center')
ax.text(5, -5, 'Electronics', fontsize=12, ha='center')
ax.text(-5, 5, 'Apparel', fontsize=12, ha='center')
ax.text(5, 5, 'Checkout', fontsize=12, ha='center')

# Set limits and labels
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('2D Visualization of Virtual Store Layout')

# Show plot
plt.show()