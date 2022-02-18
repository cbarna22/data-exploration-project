#Python Exploratory Data Analysis Project
#Summary Statistics
#
#This script prints out summary statistics for the housing data
#including count, mean, standard deviation (std), min, max, and the 25%,
#50% and 75% quartiles.

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calmap
from pandas_profiling import ProfileReport


#reading in dataset to dataframe
df = pd.read_csv('/Users/Camille/Downloads/home_data.csv') 

df['date'] = pd.to_datetime(df['date']) #changing date to datetime object

pd.set_option("display.max_columns", 100)

df.set_index('date', inplace=True) #setting date as index

print(df.describe()) #printing out summary statistics




