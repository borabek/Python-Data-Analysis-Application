import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample numerical data
data = [23, 45, 67, 45, 33, 89, 45, 56, 78, 98, 45, 67, 89, 12, 35]

def group_data(data, class_width):
    min_val, max_val = min(data), max(data)
    bins = np.arange(min_val, max_val + class_width, class_width)
    frequency, bin_edges = np.histogram(data, bins=bins)
    
    midpoints = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(len(bin_edges)-1)]
    freq_times_mid = [frequency[i] * midpoints[i] for i in range(len(frequency))]
    
    grouped_df = pd.DataFrame({
        'Classes': [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range(len(bin_edges)-1)],
        'Frequency': frequency,
        'Midpoint': midpoints,
        'Freq * Mid': freq_times_mid
    })
    
    return grouped_df, frequency, midpoints

#Draw Histogram
def draw_histogram(grouped_df, class_width):
    plt.bar(
        grouped_df['Midpoint'], 
        grouped_df['Frequency'], 
        width= class_width,  # Increase width to reduce gaps
        color='green',  # Change color to green
        edgecolor='black', 
        alpha=0.6
    )
    plt.xlabel("Midpoint")
    plt.ylabel("Frequency")
    plt.title("Histogram of Grouped Data")
    plt.show()
    
groupedDate, frequency, midpoint = group_data(data, 5)   
draw_histogram(groupedDate, 5)