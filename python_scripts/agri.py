import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

agri = pd.read_excel("agri.ods", engine="odf")

output_directory = "plots"
os.makedirs(output_directory, exist_ok=True)

def charto(label):
    uppercase_label = label.upper()
    if not all('A' <= char <= 'Z' for char in uppercase_label):
        return "Invalid input. Please provide a valid uppercase letter or letters."
    result = 0
    for char in uppercase_label:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

x = agri.iloc[:,0]

# growth % by allied sectors
y = agri.iloc[:,charto('H')-1]
correlation_coefficient = x.corr(y)
plt.scatter(x, y)
plt.text(x.max()-25, y.max(), f'Correlation Coefficient: {correlation_coefficient:.2f}', fontsize=10, color='red')
plt.xlabel('Years')
plt.ylabel('% Growth')
plt.title('Years v/s % Growth by allied sectors')
output_filename = os.path.join(output_directory, 'Allied_growth_%.png')
plt.savefig(output_filename)
plt.clf()
print('Allied_growth_%.png')

# arable land & gdp contri %
y1 = agri.iloc[:,charto('G')-1]
y2 = agri.iloc[:,charto('D')-1]
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('Years')
ax1.set_ylabel('Arable land in hectares', color=color)
ax1.plot(x, y1, color=color, label='Land (hectares)')
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('%GDP contribution of total GDP', color=color)
ax2.scatter(x, y2, color=color, label='%GDP contribution')
ax2.tick_params(axis='y', labelcolor=color)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right')
plt.title('Arable land and GDP% contribution over Years')
ax1.axvspan(2005, x.max(), alpha=0.3, color='yellow')
output_filename = os.path.join(output_directory, 'ArableLand&GDP_over_years.png')
plt.savefig(output_filename)
plt.clf()
print('Allied_growth_%.png')

# reducing x
x = agri.iloc[45:61,0]

# ys'
fertilizer = agri.iloc[45:61,charto('C')-1]
exports = agri.iloc[45:61,charto('B')-1]
employment = agri.iloc[45:61,charto('E')-1]
alliedValue = agri.iloc[45:61,charto('F')-1]

# fertilizer
correlation_coefficient = x.corr(fertilizer)
plt.plot(x, fertilizer)
plt.text(x.min(), fertilizer.max(), f'Correlation Coefficient: {correlation_coefficient:.2f}', fontsize=10, color='red')
plt.xlabel('Years')
plt.ylabel('Fertilizer consumption (kg per hectares)')
plt.title('Years v/s Fertilizer consumption')
output_filename = os.path.join(output_directory, 'Fertilizer.png')
plt.savefig(output_filename)
plt.clf()
print('Fertilizer.png')

# exports
correlation_coefficient = x.corr(exports)
plt.plot(x, exports)
plt.text(x.min(), exports.max(), f'Correlation Coefficient: {correlation_coefficient:.2f}', fontsize=10, color='red')
plt.xlabel('Years')
plt.ylabel('Exports % of merchandise exports')
plt.title('Years v/s Agricultural Raw Materials Exports')
output_filename = os.path.join(output_directory, 'Exports.png')
plt.savefig(output_filename)
plt.clf()
print('Exports.png')

# employment
correlation_coefficient = x.corr(employment)
plt.plot(x, employment)
plt.text(x.min(), employment.max(), f'Correlation Coefficient: {correlation_coefficient:.2f}', fontsize=10, color='red')
plt.xlabel('Years')
plt.ylabel('% of total Employment')
plt.title('Years v/s Agricultural Employment')
output_filename = os.path.join(output_directory, 'Employment.png')
plt.savefig(output_filename)
plt.clf()
print('Employment.png')

# alliedValue
correlation_coefficient = x.corr(alliedValue)
plt.plot(x, alliedValue)
plt.text(x.min(), alliedValue.max(), f'Correlation Coefficient: {correlation_coefficient:.2f}', fontsize=10, color='red')
plt.xlabel('Years')
plt.ylabel('Value added $US')
plt.title('Years v/s Value added by Agriculture, Forestry, Fishing')
output_filename = os.path.join(output_directory, 'alliedValue.png')
plt.savefig(output_filename)
plt.clf()
print('alliedValue.png')
