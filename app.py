import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# set title 

st.title('Machine Learning Web App')

# set subtitle

st.write("""
# A simple Data App with Streamlit
""")
st.write("""
### Let's explore different classifiers and datasets
""")

dataset_name = st.sidebar.selectbox('Select Dataset', ['Iris', 'Breast Cancer', 'Wine Dataset'],
                                    index=None,
                                    placeholder='Select a dataset...')

classifier_name = st.sidebar.selectbox('Select Classifier', ['KNN', 'SVM'],
                                      index=None,
                                      placeholder='Select a classifier...')

if dataset_name is None:
    st.info('Select a dataset to continue.')
    st.stop()

def get_dataset(name):
    data = None
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    return data.data, data.target, data.feature_names

st.write(""" 
##### Dataset: {dataset_name}
""".format(dataset_name=dataset_name))
x, y, feature_names = get_dataset(dataset_name)
st.dataframe(pd.DataFrame(x, columns=feature_names))
st.write('Shape of dataset:', x.shape)
st.write('Number of classes:', len(np.unique(y)))


fig = plt.figure()
sns.boxplot(data=x, orient='h')
st.pyplot(fig)
plt.close(fig)

fig = plt.figure()
plt.hist(x)
st.pyplot(fig)
plt.close(fig)

if classifier_name is None:
    st.info('Select a classifier to train the model.')
    st.stop()

# Building Our Algorithm
def add_parameter(name_of_clf):
    params = dict()
    if name_of_clf == 'SVM':
        C = st.sidebar.slider('C', 0.01, 15.0, step=0.01)
        params['C'] = C
    elif name_of_clf == 'KNN':
        K = st.sidebar.slider('K', 1, 15,step=1)
        params['K'] = K
    else:
        st.write('Please select a classifier')
    return params

params = add_parameter(classifier_name)

# Accessing the classifier
def get_classifier(name_of_clf, params):
    clf = None
    if name_of_clf == 'SVM':
        clf = SVC(C=params['C'])
    elif name_of_clf == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        st.write('Please select a classifier')
    return clf

clf = get_classifier(classifier_name, params)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
st.write("""
##### Predicted values for the test set:
""")
st.write(y_pred)

accuracy = accuracy_score(y_test, y_pred)
st.write('Classifier:', classifier_name)
st.write('Accuracy of your Model is:', accuracy)