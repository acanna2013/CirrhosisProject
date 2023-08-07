# -*- coding: utf-8 -*-
"""Copy of Copy of Cirrhosis Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1elJfN05vyw8QJ_1yt5JYD_9BM1an3JWX
"""

import pandas
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/gdrive')
df = pd.read_csv('/content/gdrive/My Drive/cirrhosis.csv', encoding='ISO-8859-1')

df.head(30)

df.shape
df.head()

for column in df:
  df = df[df[column].notnull()]

df.shape

df.boxplot(column=['ID'])

df.boxplot(column=['N_Days'])

df.boxplot(column=['Age'])

df.boxplot(column=['Bilirubin'])

df.boxplot(column=['Cholesterol'])

df.boxplot(column=['Albumin'])

df.boxplot(column=['Copper'])

df.boxplot(column=['Alk_Phos'])

df.boxplot(column=['SGOT'])

df.boxplot(column=['Tryglicerides'])

df.boxplot(column=['Platelets'])

df.boxplot(column=['Prothrombin'])

df.boxplot(column=['Stage'])

df.loc[df['Status'] == 'C', 'Status_class'] = 1
df.loc[df['Status'] == 'D', 'Status_class'] = 0
df.loc[df['Status'] == 'CL', 'Status_class'] = 1
df.head()

df.loc[df['Drug'] == 'D-penicillamine', 'Drug_class'] = 1
df.loc[df['Drug'] == 'Placebo', 'Drug_class'] = 0
df.head()

df.loc[df['Sex'] == 'M', 'Sex_class'] = 0
df.loc[df['Sex'] == 'F', 'Sex_class'] = 1
df.head()

df.loc[df['Ascites'] == 'Y', 'Ascites_class'] = 1
df.loc[df['Ascites'] == 'N', 'Ascites_class'] = 0
df.head()

df.loc[df['Hepatomegaly'] == 'Y', 'Hepatomegaly_class'] = 1
df.loc[df['Hepatomegaly'] == 'N', 'Hepatomegaly_class'] = 0
df.head()

df.loc[df['Spiders'] == 'Y', 'Spiders_class'] = 1
df.loc[df['Spiders'] == 'N', 'Spiders_class'] = 0
df.head()

df.loc[df['Edema'] == 'Y', 'Edema_class'] = 1
df.loc[df['Edema'] == 'N', 'Edema_class'] = 0
df.loc[df['Edema'] == 'S', 'Edema_class'] = 2
df.head()

import seaborn as sn

sn.heatmap(df[['N_Days', 'Age','Bilirubin', 'Cholesterol', 'Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets', 'Prothrombin', 'Stage', 'Status_class', 'Drug_class', 'Sex_class', 'Ascites_class', 'Hepatomegaly_class', 'Spiders_class', 'Edema_class' ]].corr(), annot=False)

df.plot(kind= 'scatter', x = 'Cholesterol', y = 'N_Days', use_index=True)

df.plot(kind= 'scatter', x = 'Tryglicerides', y = 'N_Days', use_index=True)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaled = scaler.fit_transform(df[['N_Days', 'Age','Bilirubin', 'Cholesterol', 'Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets', 'Prothrombin', 'Stage', 'Drug_class', 'Sex_class', 'Ascites_class', 'Hepatomegaly_class', 'Spiders_class', 'Edema_class']])

df_scaled = pd.DataFrame(data=scaled, columns=['N_Days_scaled', 'Age_scaled','Bilirubin_scaled', 'Cholesterol_scaled', 'Albumin_scaled','Copper_scaled','Alk_Phos_scaled','SGOT_scaled','Tryglicerides_scaled','Platelets_scaled', 'Prothrombin_scaled', 'Stage_scaled' , 'Drug_class_scaled', 'Sex_class_scaled', 'Ascites_class_scaled', 'Hepatomegaly_class_scaled', 'Spiders_class_scaled', 'Edema_class_scaled'])

df = df.join(df_scaled)
df

df.hist('Cholesterol')

"""feature_cols = ['Age','Bilirubin', 'Cholesterol', 'Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets', 'Prothrombin', 'Stage', 'Drug_class', 'Sex_class', 'Ascites_class', 'Hepatomegaly_class', 'Spiders_class', 'Edema_class' ]

"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
feature_cols = [ 'Age','Bilirubin', 'Cholesterol', 'Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets', 'Prothrombin', 'Stage', 'Sex_class', 'Ascites_class', 'Hepatomegaly_class', 'Spiders_class', 'Edema_class' ]
X = df[feature_cols] # Features
y = df.Status_class # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

clf = DecisionTreeClassifier(splitter="best")

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=13)

knn.fit(X_train, y_train)

# Calculate the accuracy of the model
print(knn.score(X_test, y_test))
d
neighbors = np.arange(1, 20)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over K values
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Compute training and test data accuracy
    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy')

plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())