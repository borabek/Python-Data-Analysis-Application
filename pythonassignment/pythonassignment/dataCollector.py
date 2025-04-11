import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics


def get_user_data():
    # Prompts the user to input data manually or use sample data.
    # Saves input to data.csv and returns the complete dataset.
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
                # Read existing data to avoid duplicates
                try:
                    existing = pd.read_csv('data.csv', names=['Data'])
                    existing_data = pd.to_numeric(existing['Data'], errors='coerce').dropna().tolist()
                except FileNotFoundError:
                    existing_data = []
                all_data = list(set(existing_data + data))  # remove duplicates
                df = pd.DataFrame({'Data': all_data})
                df.to_csv('data.csv', index=False, header=False)
                print("Data saved to data.csv (duplicates removed)")
                return all_data
            except ValueError:
                print("Invalid input. Please enter only numeric values.")
    else:
        data = [23, 45, 67, 45, 33, 89, 45, 56, 78, 98, 45, 67, 89, 12, 35]
        print("Using sample data:", data)
        return data


def read_data():
    # Reads numeric data from data.csv. Returns a list of floats.
    try:
        df = pd.read_csv('data.csv', names=['Data'])
        return pd.to_numeric(df['Data'], errors='coerce').dropna().tolist()
    except FileNotFoundError:
        print("Error: data.csv not found. Please enter data manually first.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []


def group_data(data, class_width):
    # Groups data into intervals of specified class width.
    # Returns grouped DataFrame, frequency list, and midpoint list.
    if not data:
        print("No data provided.")
        return None, None, None

    if class_width <= 0:
        print("Class width must be a positive number.")
        return None, None, None

    if class_width > (max(data) - min(data)):
        print("Class width is too large compared to the data range.")
        return None, None, None

    # Define histogram bins and compute frequencies
    data_min, data_max = min(data), max(data)
    bins = np.arange(data_min, data_max + class_width, class_width)
    frequency, bin_edges = np.histogram(data, bins=bins)

    # Compute class midpoints
    midpoints = [(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(bin_edges) - 1)]
    freq_times_mid = [frequency[i] * midpoints[i] for i in range(len(frequency))]
    intervals = [f"{bin_edges[i]} - {bin_edges[i + 1]}" for i in range(len(bin_edges) - 1)]

    grouped_df = pd.DataFrame({
        'Classes': intervals,
        'Frequency': frequency,
        'Midpoint': midpoints,
        'Freq * Mid': freq_times_mid
    })
    return grouped_df, frequency.tolist(), midpoints


def compute_statistics(data, frequency, midpoints):
    # Computes descriptive statistics from raw data.
    if not data:
        print("No data provided for statistics.")
        return {}

    stats = {
        "Mean": round(statistics.mean(data), 2),
        "Median": round(statistics.median(data), 2),
        "Variance": round(statistics.variance(data), 2) if len(data) > 1 else 0.0,
        "Standard Deviation": round(statistics.stdev(data), 2) if len(data) > 1 else 0.0,
    }

    # Handle multimodal values
    mode_list = statistics.multimode(data)
    stats["Mode"] = ", ".join(map(str, mode_list)) if mode_list else None

    # Determine modal class based on frequency and midpoints
    if frequency:
        max_freq = max(frequency)
        modal_index = frequency.index(max_freq)
        stats["Modal Class"] = f"Interval with midpoint {midpoints[modal_index]}"
    else:
        stats["Modal Class"] = None

    return stats


def draw_histogram(grouped_df, class_width):
    # Draws histogram based on grouped data.
    if grouped_df is None:
        print("No grouped data to plot.")
        return

    plt.bar(
        grouped_df['Midpoint'],
        grouped_df['Frequency'],
        width=class_width,
        color='green',
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

        try:
            class_width = float(input("Enter class width: "))
        except ValueError:
            print("Invalid class width input. Must be a number.")
            continue

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
        print("Returning to the main menu...")


if __name__ == "__main__":
    main()
