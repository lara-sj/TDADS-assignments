import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv('car_data.csv')

# select the 2nd and 3rd columns and convert them to a numpy array 
X = data.iloc[:, 2].values.reshape(-1,1)
Y = data.iloc[:, 3].values.reshape(-1,1)

# create linear regression object
linear_regressor = LinearRegression()
# perform linear regression 
linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)

#plot the data and predicted varibale
plt.scatter(X,Y)
plt.plot(X,Y_pred, color = 'red')
plt.xlabel('selling price')
plt.ylabel('km driven')
plt.show()