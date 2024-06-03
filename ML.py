#Machine Learnig Algorithms and Tools
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Define the tools and libraries layout
sections = [
    patches.Rectangle((-10, -10), 20, 20, linewidth=1, edgecolor='r',
                      facecolor='none', label='Machine Learning Algorithms'),
    patches.Rectangle((-8, -8), 6, 6, linewidth=1,
                      edgecolor='b', facecolor='none', label='Python'),
    patches.Rectangle((2, -8), 6, 6, linewidth=1, edgecolor='g',
                      facecolor='none', label='Pandas and NumPy'),
    patches.Rectangle((-8, 2), 6, 6, linewidth=1, edgecolor='y',
                      facecolor='none', label='Scikit-Learn'),
    patches.Rectangle((2, 2), 6, 6, linewidth=1, edgecolor='m',
                      facecolor='none', label='TensorFlow/PyTorch'),
    patches.Rectangle((10, 10), 6, 6, linewidth=1,
                      edgecolor='c', facecolor='none', label='R'),
    patches.Rectangle((18, 10), 6, 6, linewidth=1,
                      edgecolor='k', facecolor='none', label='ggplot2'),
    patches.Rectangle((26, 10), 6, 6, linewidth=1,
                      edgecolor='orange', facecolor='none', label='dplyr'),
    patches.Rectangle((34, 10), 6, 6, linewidth=1,
                      edgecolor='purple', facecolor='none', label='JavaScript'),
    patches.Rectangle((42, 10), 6, 6, linewidth=1,
                      edgecolor='brown', facecolor='none', label='React/Angular')
]

# Add sections to the plot
for section in sections:
    ax.add_patch(section)

# Set the limits and labels
ax.set_xlim(-15, 50)
ax.set_ylim(-15, 20)
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('Machine Learning Algorithms and Tools')
ax.legend()

# Show the plot
plt.show()
