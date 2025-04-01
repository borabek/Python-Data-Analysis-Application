import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math

def input_data():
    #Let user to input numerical data (or use sample data).
    choice = input("Do you want to enter data manually? (y/n): ").strip().lower()
    if choice == 'y':
        while True:
            user_input = input("Enter numbers separated by spaces or commas: ").strip()
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue
            tokens = user_input.replace(',', ' ').split()
            try:
                data = [float(token) for token in tokens]
                return data
            except ValueError:
                print("Invalid input. Please enter only numeric values.")
    else:
        # Use sample data as provided in the references
        data = [23, 45, 67, 45, 33, 89, 45, 56, 78, 98, 45, 67, 89, 12, 35]
        print("Using sample data:", data)
        return data

def save_dataframe_to_csv(df, filename):
    #Save a DataFrame to a CSV file
    try:
        df.to_csv(filename, index=False)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def load_data_from_csv(filename):
    #get th number then turn it as a list
    try:
        df = pd.read_csv(filename)
        # Assuming the first column contains the data
        data = df.iloc[:, 0].tolist()
        print(f"Loaded {len(data)} data points from {filename}.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def group_data(data, class_width):
    if not data:
        print("No data provided.")
        return None, None, None
    # Determine bin edges using numpy's arange
    data_min, data_max = min(data), max(data)
    bins = np.arange(data_min, data_max + class_width, class_width)
    # Compute frequency distribution
    frequency, bin_edges = np.histogram(data, bins=bins)
    # Calculate midpoints for each bin
    midpoints = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(len(bin_edges)-1)]
    # Compute frequency times midpoint
    freq_times_mid = [frequency[i] * midpoints[i] for i in range(len(frequency))]
    # Create interval labels as strings
    intervals = [f"{bin_edges[i]} - {bin_edges[i+1]}" for i in range(len(bin_edges)-1)]
    # Create a DataFrame to display the grouped data
    grouped_df = pd.DataFrame({
        'Classes': intervals,
        'Frequency': frequency,
        'Midpoint': midpoints,
        'Freq * Mid': freq_times_mid
    })
    return grouped_df, frequency.tolist(), midpoints

def draw_histogram(grouped_df, class_width):
    #Plot a histogram using the grouped data.
    if grouped_df is None:
        print("No grouped data to plot.")
        return
    plt.bar(
        grouped_df['Midpoint'],
        grouped_df['Frequency'],
        width=class_width,  # Increase width to reduce gaps
        color='green',      # Use green bars
        edgecolor='black', 
        alpha=0.6
    )
    plt.xlabel("Midpoint")
    plt.ylabel("Frequency")
    plt.title("Histogram of Grouped Data")
    plt.show()

def compute_statistics(data, frequency, midpoints):
    #Compute basic statistics on the raw data and return them in a dictionary.
    if not data:
        print("No data provided for statistics.")
        return {}
    stats = {}
    stats["Mean"] = round(statistics.mean(data), 2)
    stats["Median"] = round(statistics.median(data), 2)
    mode_list = statistics.multimode(data)
    if len(mode_list) == 1:
        stats["Mode"] = mode_list[0]
    elif len(mode_list) > 1:
        stats["Mode"] = ", ".join(map(str, mode_list))
    else:
        stats["Mode"] = None
    # Identify modal class (first class with the maximum frequency)
    if frequency:
        max_freq = max(frequency)
        modal_index = frequency.index(max_freq)
        stats["Modal Class"] = f"Interval with midpoint {midpoints[modal_index]}"
    else:
        stats["Modal Class"] = None
    # Use sample variance and standard deviation (if possible)
    if len(data) > 1:
        stats["Variance"] = round(statistics.variance(data), 2)
        stats["Standard Deviation"] = round(statistics.stdev(data), 2)
    else:
        stats["Variance"] = 0.0
        stats["Standard Deviation"] = 0.0
    return stats

def main():
    print("=== Grouped Data Analysis ===")
    # Option to load data from CSV or input manually
    choice = input("Load data from CSV file? (yes/no): ").strip().lower()
    if choice == 'yes':
        filename = input("Enter CSV filename (default: data.csv): ").strip()
        if filename == "":
            filename = "data.csv"
        data = load_data_from_csv(filename)
    else:
        data = input_data()
    
    # Ask user for class width
    while True:
        cw_input = input("Enter class width (positive number): ").strip()
        try:
            class_width = float(cw_input)
            if class_width <= 0:
                print("Class width must be positive.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Group the data and display results
    grouped_df, freq, midpoints = group_data(data, class_width)
    if grouped_df is not None:
        print("\nFrequency Distribution Table:")
        print(grouped_df.to_string(index=False))
    
    # Compute and display statistics
    stats = compute_statistics(data, freq, midpoints)
    if stats:
        print("\nDescriptive Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    
    # Ask user if they want to save the results
    save_choice = input("Save grouped data and statistics to CSV? (yes/no): ").strip().lower()
    if save_choice == 'yes':
        dist_file = input("Enter filename for grouped data (default: grouped_data.csv): ").strip()
        if dist_file == "":
            dist_file = "grouped_data.csv"
        stats_file = input("Enter filename for statistics (default: statistics.csv): ").strip()
        if stats_file == "":
            stats_file = "statistics.csv"
        save_dataframe_to_csv(grouped_df, dist_file)
        # Save statistics as a one-row DataFrame
        stats_df = pd.DataFrame({key: [value] for key, value in stats.items()})
        save_dataframe_to_csv(stats_df, stats_file)
    
    # Plot the histogram
    plot_choice = input("Plot histogram? (y/n): ").strip().lower()
    if plot_choice == 'y':
        draw_histogram(grouped_df, class_width)
    
    print("Analysis complete.")

if __name__ == "__main__":
    main()
