"""
8. Apply EM algorithm to cluster a set of data stored in a .CSV file. Use the same data
set for clustering using k-Means algorithm. Compare the results of these two
algorithms and comment on the quality of clustering. You can add Java/Python ML
library classes/API in the program.
"""
from sklearn import datasets, metrics
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

import matplotlib.pyplot as plt
import pandas as pd

dataset = datasets.load_iris()

X = pd.DataFrame(dataset.data)
y = pd.DataFrame(dataset.target)
model = KMeans(n_clusters=3)
model.fit(X)

plt.figure()

plt.subplot(3, 2, 1)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y.iloc[:, 0], s=10, cmap='viridis')
plt.title("Actual Classification - Sepal")
plt.subplot(3, 2, 2)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=model.labels_, s=10, cmap='viridis')
plt.title("K-Means Classification - Sepal")

plt.subplot(3, 2, 3)
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=y.iloc[:, 0], s=10, cmap='viridis')
plt.title("Actual Classification - Petal")
plt.subplot(3, 2, 4)
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=model.labels_, s=10, cmap='viridis')
plt.title("K-Means Classification - Petal")

print('K-Means Accuracy : ', metrics.accuracy_score(y, model.labels_))

# EM Algorithm
gmm = GaussianMixture(n_components=3)
gmm.fit(X)
y_predict = gmm.predict(X)

plt.subplot(3, 2, 5)
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=y.iloc[:, 0], s=10, cmap='viridis')
plt.title("Actual Classification - Petal")
plt.subplot(3, 2, 6)
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=y_predict, s=10, cmap='viridis')
plt.title("GMM Classification - Petal")
print('GMM Accuracy : ', metrics.accuracy_score(y, y_predict))
print("Confusion Matrix : \n", metrics.confusion_matrix(y, y_predict))
plt.show()
