import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans

Dataset = pd.DataFrame({'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
       })


model=KMeans(n_clusters=3,max_iter=400)
Nav=model.fit(Dataset)
predict=model.predict(Dataset)
centroids=model.cluster_centers_
plt.scatter(Dataset['x'],Dataset['y'],c=predict,s= 50)
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=100)
plt.show()


