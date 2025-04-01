import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

def get_user_data():
    # Read numerical data from CSV file
    choice = input("Do you want to enter data manually? (yes/no): ").strip().lower()
    if choice == 'yes':
        while True:
            user_input = input("Enter numbers separated by spaces or commas: ").strip()
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue
            tokens = user_input.replace(',', ' ').split()
            try:
                data = [float(token) for token in tokens]
                df = pd.DataFrame({'Data': data})
                df.to_csv('raw_data.csv', mode='a', index=False, header=False)
                print("Raw data appended to raw_data.csv")
                return read_data()  # After appending, read data
            except ValueError:
                print("Invalid input. Please enter only numeric values.")
    else:
        data = [23, 45, 67, 45, 33, 89, 45, 56, 78, 98, 45, 67, 89, 12, 35]
        print("Using sample data:", data)
        return data

def read_data():
    try:
        df = pd.read_csv('raw_data.csv', names=['Data'])
        # Ensure that data is numeric
        return pd.to_numeric(df['Data'], errors='coerce').dropna().tolist()
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def group_data(data, class_width):
    if not data:
        print("No data provided.")
        return None, None, None
    # Ensure that data is numeric (if not already)
    data = [float(i) for i in data]

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

def compute_statistics(data, frequency, midpoints):
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

def draw_histogram(grouped_df, class_width):
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

def main():
    while True:
        print("\n=== Grouped Data Analysis ===")
        print("1. Enter Data")
        print("2. Load Data from CSV")
        print("3. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            data = get_user_data()
        elif choice == '2':
            data = read_data()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            continue
        if not data:
            print("No data available. Returning to menu.")
            continue
        class_width = float(input("Enter class width: "))
        grouped_df, freq, midpoints = group_data(data, class_width)
        if grouped_df is not None:
            print("\nFrequency Distribution Table:")
            print(grouped_df.to_string(index=False))
            grouped_df.to_csv('grouped_data.csv', index=False)
            print("Grouped data saved to grouped_data.csv")
        stats = compute_statistics(data, freq, midpoints)
        if stats:
            print("\nDescriptive Statistics:")
            for key, value in stats.items():
                print(f"{key}: {value}")
            stats_df = pd.DataFrame(list(stats.items()), columns=['Statistic', 'Value'])
            stats_df.to_csv('statistics.csv', index=False)
            print("Statistics saved to statistics.csv")
        draw_histogram(grouped_df, class_width)
        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    main()
