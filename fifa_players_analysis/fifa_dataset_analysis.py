# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:03:07 2023

@author: Mohamed
"""

import numpy as np
import csv

np.set_printoptions(precision=2)

def import_csv_as_list(file_path, encoding='utf-8'):
    data = []

    with open(file_path, 'r', encoding=encoding, errors='replace') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists
        
        for row in csv_reader:
            data.append(row[:])  # Append all values except the first column
    
    return data

def calculate_mean_rating(csv_data):
    ratings = []
    for row in csv_data:
        rating = int(row[2])
        ratings.append(rating)
    
    ratings_array = np.array(ratings)
    mean_rating = np.mean(ratings_array)
    return mean_rating

def calcualte_median_rating(csv_data):
    ratings = []
    for row in csv_data:
        rating = int(row[2])
        ratings.append(rating)
    
    ratings_array = np.array(ratings)
    mean_rating = np.median(ratings_array)
    return mean_rating

def highest_rated_gk_name(csv_data):
    names_and_ratings = []
    for row in csv_data:
        names_and_ratings.append(row[1:4])
    
    names_and_ratings_array = np.array(names_and_ratings)
    last_field = names_and_ratings_array[:, -1]  # Get the last column
    mask = last_field == ' GK'  # Create a boolean mask
    gk_ratings_array = names_and_ratings_array[mask]  # Apply the mask to extract rows
    highest_rating_index = np.argmax(gk_ratings_array[:, 1].astype(int))
    highest_rated_player_name = gk_ratings_array[highest_rating_index, 0]
    
    return highest_rated_player_name

csv_data = import_csv_as_list('fifa.csv')
average_player_rating = calculate_mean_rating(csv_data)
median_player_rating = calcualte_median_rating(csv_data)
highest_rated_gk = highest_rated_gk_name(csv_data)
print("Average rating:", np.round(average_player_rating, 2), "\nMedian of ratings:", median_player_rating,
      "\nHighest rated GK:", highest_rated_gk)
