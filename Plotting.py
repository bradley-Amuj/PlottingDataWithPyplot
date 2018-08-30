#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:23:55 2018

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt

#This line is used to open the file and read it 
data_source = pd.read_excel("/Users/user/Desktop/dataSource.xlsx")
print(data_source)

x_values = data_source["X(AGE)"]
y_values = data_source["Y(SALARY)"]

plt.title("Data Source")
plt.plot(x_values,y_values,"ro")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid()
plt.show()

