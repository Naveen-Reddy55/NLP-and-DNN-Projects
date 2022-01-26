import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=load_iris()
df=pd.DataFrame(data.data,columns=data.feature_names)
df['targets']=pd.Series(data.target)

y=df['targets']
X=df.drop('targets',axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

model= svm.SVC()
model.fit(X_train,y_train)
predict=model.predict(X_test)
acc=accuracy_score(y_test,predict)
print(acc)

