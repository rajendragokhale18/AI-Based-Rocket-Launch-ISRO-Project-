import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('rocket_launch_data.csv')

# Display the first few rows of the dataset
print(data.head())

# Handle missing values
# Option 1: Drop rows with missing values
data_cleaned = data.dropna()

# Option 2: Fill missing values with the mean or median
data_cleaned = data.fillna(data.mean())

# Option 3: Forward-fill or backward-fill
data_cleaned = data.fillna(method='ffill')

# Handle outliers using z-score
from scipy import stats

z_scores = np.abs(stats.zscore(data_cleaned.select_dtypes(include=np.number)))
data_cleaned = data_cleaned[(z_scores < 3).all(axis=1)]

# Save cleaned data
data_cleaned.to_csv('cleaned_rocket_launch_data.csv', index=False)
