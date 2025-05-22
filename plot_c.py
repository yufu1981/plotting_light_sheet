#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:33:04 2023

@author: fuyu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Read the CSV file
mousenumber = '1'
csv_file = '/Users/'+'Mouse'+mousenumber+'_session_example.csv'
df = pd.read_csv(csv_file)




# Calculate the downsampling factor
downsample_factor = int(df.shape[0] / target_size)

# Downsample the DataFrame
df_downsampled = df.groupby(df.index // downsample_factor).mean()

# Trim or extend the downsampled DataFrame to the target size
if df_downsampled.shape[0] > target_size:
    df_downsampled = df_downsampled.iloc[:target_size, :]
elif df_downsampled.shape[0] < target_size:
    df_downsampled = df_downsampled.reindex(range(target_size), fill_value=None)

snout_x = df_downsampled['snout_x']
snout_y = df_downsampled['snout_y']
chow_x = 250
chow_y = 450

distance_to_food = np.sqrt((snout_x - chow_x)**2 + (snout_y - chow_y)**2)



# Calculate the change in x and y positions
delta_x = snout_x.diff()
delta_y = snout_y.diff()

# Calculate the Euclidean distance between consecutive points
distance = np.sqrt(delta_x**2 + delta_y**2)
total_distance = distance.sum()
print('total_distance is', total_distance)



# Plot the distance against the time stamp
time_stamp = df_downsampled.iloc[:, 0]

# plt.plot(time_stamp, distance)
plt.plot(time_stamp, distance)
plt.xlabel('Time Stamp')
plt.ylabel('Distance (units)')
plt.title('speed across time')
plt.ylim(-1, 600)  # Set the y-axis limits
plt.show()


# Plot the distance to food
fig, ax = plt.subplots(figsize=(6, 6))
plt.plot(time_stamp, distance_to_food)
plt.xlabel('Time Stamp')
plt.ylabel('Distance (units)')
plt.title('distance to food across time')
plt.ylim(-1, 500)  # Set the y-axis limits

plt.savefig('distance_2.png', dpi=600)
plt.show()


# Create a trajectory plot
# Create a trajectory plot with colored lines based on distances
fig, ax = plt.subplots(figsize=(7, 6))
for i in range(1, len(snout_x)):
    color = plt.cm.viridis(norm_distances[i])  # You can choose a different colormap if you prefer
    ax.plot(snout_x[i-1:i+1], snout_y[i-1:i+1], marker='', linestyle='-', color=color)

# Create a colorbar for reference
sm = ScalarMappable(cmap=plt.cm.viridis, norm=norm)
sm.set_array([])  # Dummy array for the colorbar
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Distance', rotation=270, labelpad=15)

plt.title('Object Trajectory with Color-coded Distance')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.xlim(80, 500)
plt.ylim(80, 500)

plt.savefig('trajectory_2.png', dpi=600)
plt.show()

