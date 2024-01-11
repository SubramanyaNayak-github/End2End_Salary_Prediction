# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Salary Data.csv')

df = df.dropna()

df.drop('Job Title',axis=1, inplace=True)

#Converting words to integer values
def convert_to_int(word):
    word_dict = {"Bachelor's":1, "Master's":2, "PhD":3}
    return word_dict[word]

df['Education Level'] = df['Education Level'].apply(lambda x : convert_to_int(x))


df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})


X = df.drop(columns = 'Salary')

y = df["Salary"]


"""
### Splitting Training and Test Set

Since we have a very small dataset, we will train our model with all availabe data.

"""

regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)


# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))