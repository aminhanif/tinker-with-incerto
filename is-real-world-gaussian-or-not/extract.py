import pandas as pd

# Load the CSV file
df = pd.read_csv('height.csv')

# Extract a specific column by column name
specific_column = df['Height(Inches)']

# Print the extracted column
print(specific_column)
