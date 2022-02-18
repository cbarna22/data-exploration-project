#Python Exploratory Data Analysis Project
#Univariate Analysis
#
#This script displays a distribution plot for home prices.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#reading in dataset to dataframe
df = pd.read_csv('/Users/Camille/Downloads/home_data.csv') 

df['date'] = pd.to_datetime(df['date']) #changing date to datetime object

pd.set_option("display.max_columns", 100)

df.set_index('date', inplace=True) #setting date as index


sns.displot(df['price']) #creating and displaying distribution plot
plt.show()
