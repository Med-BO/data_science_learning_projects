# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:28:38 2023

@author: Mohamed
"""

import pandas as pd

fifa_players = pd.read_csv("fifa.csv")

players_above_90 = fifa_players[fifa_players[' rating'] > 90]

# Goalkeepers in this dataset do not have pace defined
players_not_goalkeepers = fifa_players[fifa_players[' pace'] != ' ']

# Subsetting a dataframe containing names and pace ratings
players_names_and_pace = players_not_goalkeepers.loc[:, [" name", " pace"]]

# Converting the pace values to int
players_names_and_pace[' pace'] = players_names_and_pace[' pace'].astype(int)

# Sorting the pace values in descending order
players_names_and_pace = players_names_and_pace.sort_values(by=' pace', ascending = False)

# Top 10 fastest players in FIFA 22
players_names_and_pace.iloc[0:10]

# Adding a column that contains the average value of "defending" + "pace" + "height"
# This will serve as in indicator for how good a defender is 

defenders = fifa_players[fifa_players[' position'] == ' D']

for index, row in defenders.iterrows():
    average_defence = (int(row[' defending']) + int(row[' pace']) + int(row[' height'])) / 3
    
    defenders.loc[index, ['average_defence']] = average_defence