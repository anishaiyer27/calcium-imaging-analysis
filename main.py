"""
    main.py

    prototype code to build analysis pipeline for log file
    written to analyze all cells in 1 well

    #TODO: adapt to modularized code (prototype -> deployment grade)
    #TODO: build automated integration for multiple wells (iterate over files in directory)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from scipy.stats import linregress
from matplotlib import cm

plt.rcParams['font.sans-serif'] = "Helvetica"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 16
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.width'] = 1
plt.rcParams['ytick.major.width'] = 2


# try pipeline for 1 well log file
file_prename = 'W1'
output_filename = file_prename

# import log file from local data dir as csv
log = pd.read_csv("data/" + file_prename + '.LOG', sep='\s\s+', engine='python')
# save local copy as csv
log.to_csv(output_filename + '.csv', index=None)
print("*** converted log file to csv file for " + file_prename + " ***\n")

print("\n\nexploratory data analysis: qualitative examination of what this dataframe looks like \n")

print("first five lines of dataframe: ")
print(log.head())

print("\nconcise summary of dataframe: ")
print(log.info())

print("\nshape and dimensions of dataframe: ")
print(log.shape)

print("\nrow labels for dataframe: ")
print(log.index)

print(log)

# rename singular dataframe column for easy access
log.columns.values[0] = "data"

# retrieve sections of df corresponding to different kinds of rows
f = log.loc[log["data"].str.contains("File")]
d = log.loc[log["data"].str.contains("Date")]
regions = log.loc[log["data"].str.contains("Region")]
time = log.loc[log["data"].str.contains("Time")]
data = log.loc[~log["data"].str[1].isin(['D', 'R', 'F', 'T'])]

print("\nnumber of cells in this well: ", len(regions))

cell_scores = data.values

# TODO: issue with len(data.values) and len(regions) mismatch. values should intrinsically be the same, but they are not

