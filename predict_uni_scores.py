# import modules to be used later
import numpy as np
import pandas as pd

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

data = pd.read_csv('uni_data.csv')

# set predicting variables
X = data.iloc[:-1,1:9]
# set variable to predict (score)
Y = data.iloc[:-1,9]

# define models with alpha of 0.01
model_lasso = Lasso(alpha=0.01)
model_ridge = Ridge(alpha=0.01)

# fit models 
model_lasso.fit(X,Y)
model_ridge.fit(X,Y)

# run predictions based on a a new university
# define the data to predict
new = data.iloc[2199,1:9]

# make predictions 
prediction_lasso = model_lasso.predict([new])
prediction_ridge = model_ridge.predict([new])

# print prediction
print('Predicted: %.3f' % prediction_lasso)
print('Predicted: %.3f' % prediction_ridge)
