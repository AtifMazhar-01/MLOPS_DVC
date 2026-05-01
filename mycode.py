import pandas as pd
import os

# Create a sample DataFrame with columns names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

## Adding new row to the DataFrame for V2
# new_row_loc = {'Name': 'V2', 'Age': 40, 'City': 'Houston'}
# df.loc[len(df.index)] = new_row_loc

## Adding new row to the DataFrame for V3
#new_row_loc2 = {'Name': 'V3', 'Age': 45, 'City': 'Phoenix'}
# df.loc[len(df.index)] = new_row_loc2


# Ensure the output directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True) 

# Define the output file path
file_path = os.path.join(data_dir, 'sample_data.csv') # data/sample_data.csv

# Save the DataFrame to a CSV file,including columsn names
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")