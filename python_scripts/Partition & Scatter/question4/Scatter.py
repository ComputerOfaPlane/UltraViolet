import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the data from the Excel file
data = pd.read_excel("health.ods", engine="odf")

# Create a directory to save scatter plots if it doesn't exist
output_directory = "scatter_plots"
os.makedirs(output_directory, exist_ok=True)

x = data.iloc[:,0]

# Iterate over each column (excluding the first one) to create scatter plots
for column in data.columns[1:]:
    y = data[column]

    # Create a scatter plot
    plt.scatter(x, y)

    # Add labels and title
    plt.xlabel(data.columns[0])
    plt.ylabel(column)
    plt.title(f'{data.columns[0]} vs {column}')

    # Save the scatter plot to the "scatter_plots" directory
    output_filename = os.path.join(output_directory, f'{column}.png')
    plt.savefig(output_filename)

    # Clear the current plot for the next iteration
    plt.clf()

print("Scatter plots saved in the 'scatter_plots' directory.")
