# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hc975cUl6OLsxUgFFeHFWZ8w7MteAAXX
"""

import pandas as pd
import numpy as nm
import matplotlib.pyplot as mtp
p=pd.read_csv('/content/Employee_monthly_salary (1).csv')
p.head()

x = p.iloc[:,[2,6]].values
y = p.iloc[:,[3,5]].values
print(x,y)

import numpy as np
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
x,y,test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)

from sklearn.tree import DecisionTreeclassifier
classifier= DecisionTreeclassifier(criterion='entropy',random_state=0)
classifier.fit(x_train, y_train)