import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans

input_file = 'data_perf.txt'
x = []
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = [float(i) for i in line.split(',')]
        x.append(data)

data = np.array(x)

# Determine the optimal number of clusters
scores = []
range_values = np.arange(2, 10)
for i in range_values:
    kmeans = KMeans(init='k-means++', n_clusters=i, n_init=10)
    kmeans.fit(data)
    score = metrics.silhouette_score(data, kmeans.labels_, metric='euclidean', sample_size=len(data))
    scores.append(score)
    print(f"Number of clusters = {i}, Silhouette score = {score}")

# Plot silhouette scores
plt.figure()
plt.bar(range_values, scores, width=0.6, color='blue', align='center')
plt.title('Silhouette score vs number of clusters')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')

# Cluster data into 5 groups
kmeans = KMeans(init='k-means++', n_clusters=5, n_init=10)
kmeans.fit(data)
cluster_labels = kmeans.labels_

# Plot clustered data
plt.figure()
colors = ['r', 'g', 'b', 'y', 'c']
for i, color in enumerate(colors):
    plt.scatter(data[cluster_labels == i, 0], data[cluster_labels == i, 1],
                color=color, label=f'Cluster {i+1}')

plt.title('Input data clustered into 5 groups')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

plt.show()
