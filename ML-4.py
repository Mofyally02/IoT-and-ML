#ML Modules for the project

import matplotlib.pyplot as plt
import numpy as np

# Data from the classification reports
labels = ['Class 0', 'Class 1']
decision_tree = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00]
random_forest = [1.00, 0.50, 0.67, 0.50, 1.00, 0.67]
svm = [0.00, 0.00, 0.00, 0.33, 1.00, 0.50]

x = np.arange(len(labels))

fig, ax = plt.subplots(3, 1, figsize=(10, 15), facecolor='white')

# Bar width
width = 0.2

# Decision Tree
ax[0].bar(x - width, decision_tree[:2], width,
          label='Precision - Decision Tree')
ax[0].bar(x, decision_tree[2:4], width, label='Recall - Decision Tree')
ax[0].bar(x + width, decision_tree[4:], width,
          label='F1-Score - Decision Tree')
ax[0].set_title('Decision Tree Classifier')
ax[0].set_xticks(x)
ax[0].set_xticklabels(labels)
ax[0].legend()

# Random Forest
ax[1].bar(x - width, random_forest[:2], width,
          label='Precision - Random Forest')
ax[1].bar(x, random_forest[2:4], width, label='Recall - Random Forest')
ax[1].bar(x + width, random_forest[4:], width,
          label='F1-Score - Random Forest')
ax[1].set_title('Random Forest Classifier')
ax[1].set_xticks(x)
ax[1].set_xticklabels(labels)
ax[1].legend()

# SVM
ax[2].bar(x - width, svm[:2], width, label='Precision - SVM')
ax[2].bar(x, svm[2:4], width, label='Recall - SVM')
ax[2].bar(x + width, svm[4:], width, label='F1-Score - SVM')
ax[2].set_title('Support Vector Machine (SVM)')
ax[2].set_xticks(x)
ax[2].set_xticklabels(labels)
ax[2].legend()

plt.tight_layout()
plt.show()
