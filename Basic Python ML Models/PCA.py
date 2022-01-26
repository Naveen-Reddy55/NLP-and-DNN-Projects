import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  sklearn.decomposition import PCA
from  sklearn.datasets import load_breast_cancer
from  sklearn.preprocessing import StandardScaler

dt=load_breast_cancer()

data=pd.DataFrame(dt['data'],columns=dt['feature_names'])
st=StandardScaler()
dataset=st.fit_transform(data)

model=PCA()
pca=model.fit_transform(dataset)


plt.plot(np.cumsum(model.explained_variance_ratio_))
plt.show()

