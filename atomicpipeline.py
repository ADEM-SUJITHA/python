import pandas as pd
# Read data from CSV
def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Process data (e.g., filtering rows, adding new columns)
def process_data(data):
    processed_data = data[data['column_name'] > threshold_value]  # Example: Filter rows
    processed_data['new_column'] = processed_data['existing_column'] * 2  # Example: Add new column
    return processed_data

# Write processed data to CSV
def write_data(data, output_file_path):
    data.to_csv(output_file_path, index=False)

# Atomic pipeline
def atomic_pipeline(input_file_path, output_file_path, threshold_value):
    data = read_data(input_file_path)
    processed_data = process_data(data)
    write_data(processed_data, output_file_path)

# Example usage
input_file = 'input_data.csv'
output_file = 'processed_data.csv'
threshold = 10

atomic_pipeline(input_file, output_file, threshold)
