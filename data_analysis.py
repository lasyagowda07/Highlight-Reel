import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('provided_data.csv')

# Display the first 5 rows
print(df.head())

# Display basic information about the dataset
print(df.info())

# Calculate and print summary statistics
print(df.describe())

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df.iloc[:, 0], df.iloc[:, 1])
plt.xlabel('Frame Number')
plt.ylabel('Value')
plt.title('Second Column vs Frame Number')
plt.grid(True)
plt.savefig('plot.png')
plt.show()



# Creating Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Scatter Plot
axes[0, 0].scatter(df.iloc[:, 0], df.iloc[:, 1], alpha=0.5, color='blue')
axes[0, 0].set_xlabel('Frame Number')
axes[0, 0].set_ylabel('Value')
axes[0, 0].set_title('Scatter Plot: Second Column vs Frame Number')

# Multiple Columns Plot
axes[0, 1].plot(df.iloc[:, 0], df.iloc[:, 1], label='Column 2', alpha=0.7)
axes[0, 1].plot(df.iloc[:, 0], df.iloc[:, 2], label='Column 3', alpha=0.7)
axes[0, 1].set_xlabel('Frame Number')
axes[0, 1].set_ylabel('Values')
axes[0, 1].set_title('Multiple Columns on Same Graph')
axes[0, 1].legend()

# Histogram
axes[1, 0].hist(df.iloc[:, 1], bins=30, color='green', alpha=0.7, edgecolor='black')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Histogram of Second Column')

# Another Column Plot
axes[1, 1].plot(df.iloc[:, 0], df.iloc[:, 3], color='red', label='Column 4')
axes[1, 1].set_xlabel('Frame Number')
axes[1, 1].set_ylabel('Values')
axes[1, 1].set_title('Column 4 vs Frame Number')

# Adjust layout
plt.tight_layout()
plt.show()