
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Visualization
plt.scatter(df['age'], df['spend'], c=df['cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Spend')
plt.title('Customer Segmentation')
plt.show()