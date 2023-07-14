# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:55:24 2023

@author: Mohamed
"""

# Subset the players rated between 85 and 90 then create a histogram of 6 parts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fifa_players = pd.read_csv("fifa.csv")

players_above_85 = fifa_players[fifa_players[" rating"] > 85]

# Creating an array from the dataframe subset
ratings_above_85 = np.array(players_above_85.loc[:, [" rating"]])

# This line converts the array of arrays (containing a single int each) to an array of ints
ratings_above_85 = ratings_above_85.flatten()

# Preparing and drawing a histogram
plt.xlabel("Rating")
plt.ylabel("Number of players")
plt.title("Number of players for each rating above 85")
plt.hist(ratings_above_85, 10)
plt.draw()