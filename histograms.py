#Python Exploratory Data Analysis Project
#Histograms
#
#This script displays histograms for all columns in the dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


df = pd.read_csv('/Users/Camille/Downloads/home_data.csv')          #reading in dataset to dataframe

df['date'] = pd.to_datetime(df['date'])                             #changing date to datetime object

pd.set_option("display.max_columns", 100)

df.set_index('date', inplace=True)                                  #setting date as index


df.hist(figsize=(15,15), bins=10)                                   #creating and displaying histograms
plt.tight_layout()                                                  #formatting to reduce overlap
plt.show()
