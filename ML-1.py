import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.cluster import KMeans

# Sample data creation for demonstration
data = {
    'age': [25, 34, 45, 23, 35, 40, 50, 29, 31, 38],
    'spend': [200, 300, 400, 150, 250, 350, 450, 220, 280, 330],
    'feedback': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Data Preprocessing
processed_df = df[['age', 'spend']]

# Splitting data
X = processed_df
y = df['feedback']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Visualization
plt.figure(facecolor='white')
plt.scatter(df['age'], df['spend'], c=df['cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Spend')
plt.title('Customer Segmentation')
plt.show()

# Print results
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_rep)