import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
golf_df = pd.read_excel('dd.xlsx', 0)
print(golf_df)
data=golf_df.iloc[:,0:4]
print(data)

y = golf_df['Play']

print('Apply Support Vector Classifier:')
clf = svm.SVC(kernel='linear')
scores = cross_val_score(clf, data, y, cv=5)
print(f"> Accuracy: {scores.mean()}")

print('Apply Random Forest Classifier:')
clf = RandomForestClassifier()
scores = cross_val_score(clf, data, y, cv=5)
print(f"> Accuracy: {scores.mean()}")


