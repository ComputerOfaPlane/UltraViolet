import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Read the data from the Excel file
rural = pd.read_excel("ruralclean.ods", engine="odf")
urban = pd.read_excel("urbanpart.ods", engine="odf")

# Create a directory to save scatter plots if it doesn't exist
output_directory = "lineplots"
os.makedirs(output_directory, exist_ok=True)

# function
def charto(label):
    uppercase_label = label.upper()
    if not all('A' <= char <= 'Z' for char in uppercase_label):
        return "Invalid input. Please provide a valid uppercase letter or letters."
    result = 0
    for char in uppercase_label:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

# x axis
x = rural.iloc[:,0]

# rural population plot
ruralpopin = rural.iloc[:,charto('L')-1]
ruralpopw = rural.iloc[:,charto('V')-1]
plt.plot(x,ruralpopw, label='World', color='black')
plt.plot(x,ruralpopin, label='India', color='blue')
plt.xlabel('Years')
plt.ylabel('Rural Population')
plt.title('Years vs Rural Population')
plt.legend()
output_filename = os.path.join(output_directory, 'Rural_Population.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted Rural population')

# rural population growth plot
ruralpopin = rural.iloc[:,charto('M')-1]
ruralpopw = rural.iloc[:,charto('W')-1]
plt.plot(x,ruralpopw, label='World', color='black')
plt.plot(x,ruralpopin, label='India', color='blue')
plt.xlabel('Years')
plt.ylabel('Growth (% annual)')
plt.title('Years vs Rural Population Growth (% annual)')
plt.legend()
output_filename = os.path.join(output_directory, 'Rural_Population_Growth%.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted Rural population growth %')

# rural population % of total population
ruralpopin = rural.iloc[:,charto('J')-1]
ruralpopw = rural.iloc[:,charto('T')-1]
plt.plot(x,ruralpopw, label='World', color='black')
plt.plot(x,ruralpopin, label='India', color='blue')
plt.xlabel('Years')
plt.ylabel('% of total')
plt.title('Years vs Rural Population (% of total Population)')
plt.legend()
output_filename = os.path.join(output_directory, 'Rural_Population_%_of_total.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted % Rural population')

# rural population practicing open defecation (% rural population)
ruralpopin = rural.iloc[:,charto('G')-1]
ruralpopw = rural.iloc[:,charto('R')-1]
plt.plot(x,ruralpopw, label='World', color='black')
plt.plot(x,ruralpopin, label='India', color='blue')
plt.xlabel('Years')
plt.ylabel('% of rural')
plt.title('Years vs Rural Population practicing open defecation')
plt.legend()
output_filename = os.path.join(output_directory, 'Rural_Population_practicing_open_defecation.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted Rural population open defecation line graph')

# people with basic hand washing facilities india
labels = ['% people true', '']
sizes1 = [60.0113582, 100-60.0113582]
sizes2 = [82.28006598, 100-82.28006598]
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].pie(sizes1, labels=labels, autopct='%1.1f%%', startangle=90, colors=['magenta', 'cyan'])
axs[0].axis('equal')
axs[0].set_title('Rural')
axs[1].pie(sizes2, labels=['',''], autopct='%1.1f%%', startangle=90, colors=['magenta', 'cyan'])
axs[1].axis('equal')
axs[1].set_title('Urban')
output_filename = os.path.join(output_directory, '%Rural_Urban_India_Handwash.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted Rural Handwash usage')

# --------------------------------------------------------------------------------------
# SANITATION
# setting up data frames
# usage sanitation services by % population rural
ruralpopin = rural.iloc[:,charto('E')-1] # safely managed
ruralpopw = rural.iloc[:,charto('P')-1]
ruralpopin1 = rural.iloc[:,charto('H')-1] # bare minimum
ruralpopw1 = rural.iloc[:,charto('S')-1]
# usage sanitation services by % population urban
urbanpopin = urban.iloc[:,charto('D')-1] # safely managed
urbanpopw = urban.iloc[:,charto('V')-1]
urbanpopin1 = urban.iloc[:,charto('O')-1] # bare minimum
urbanpopw1 = urban.iloc[:,charto('AF')-1]

#plotting
# plot safely managed urban vs rural
plt.plot(x,urbanpopw, label='Urban World', color='black')
plt.plot(x,urbanpopin, label='Urban India', color='red')
plt.fill_between(x, ruralpopw, alpha=0.3, label='Rural World', color='blue')
plt.fill_between(x, ruralpopin, alpha=0.3, label='Rural India', color='orange')
plt.xlabel('Years')
plt.ylabel('% of people')
plt.title('Years vs %Population using Safely Managed Sanitation Services')
plt.legend()
output_filename = os.path.join(output_directory, 'RuralvUrban_Safe_Sanitation.png')
plt.savefig(output_filename)
plt.clf()

# bare minimum urban vs rural
plt.plot(x,urbanpopw1, label='Urban World', color='black')
plt.plot(x,urbanpopin1, label='Urban India', color='red')
plt.fill_between(x, ruralpopw1, alpha=0.3, label='Rural World', color='blue')
plt.fill_between(x, ruralpopin1, alpha=0.3, label='Rural India', color='orange')
plt.xlabel('Years')
plt.ylabel('% of people')
plt.title('Years vs %Population using atleast Basic Sanitation Services')
plt.legend()
output_filename = os.path.join(output_directory, 'RuralvUrban_Basic_Sanitation.png')
plt.savefig(output_filename)
plt.clf()
# --------------------------------------------------------------------------------------
print('Plotted Sanitation')

# --------------------------------------------------------------------------------------
# DRINKING WATER
# setting up data frames
# usage drinking water services by % population rural
ruralpopin = rural.iloc[:,charto('F')-1] # safely managed
ruralpopw = rural.iloc[:,charto('Q')-1]
ruralpopin1 = rural.iloc[:,charto('B')-1] # bare minimum
ruralpopw1 = rural.iloc[:,charto('N')-1]
# usage drinking water services by % population urban
urbanpopw = urban.iloc[:,charto('AC')-1] # safely managed
urbanpopin1 = urban.iloc[:,charto('J')-1] # bare minimum
urbanpopw1 = urban.iloc[:,charto('AA')-1]

#plotting
# plot safely managed urban vs rural
plt.plot(x,urbanpopw, label='Urban World', color='black')
plt.fill_between(x, ruralpopw, alpha=0.3, label='Rural World', color='blue')
plt.fill_between(x, ruralpopin, alpha=0.3, label='Rural India', color='orange')
plt.xlabel('Years')
plt.ylabel('% of people')
plt.title('Years vs %Population using Safely Managed Drinking Water Services')
plt.legend()
output_filename = os.path.join(output_directory, 'RuralvUrban_Safe_Water.png')
plt.savefig(output_filename)
plt.clf()

# bare minimum urban vs rural
plt.plot(x,urbanpopw1, label='Urban World', color='black')
plt.plot(x,urbanpopin1, label='Urban India', color='red')
plt.fill_between(x, ruralpopw1, alpha=0.3, label='Rural World', color='blue')
plt.fill_between(x, ruralpopin1, alpha=0.3, label='Rural India', color='orange')
plt.xlabel('Years')
plt.ylabel('% of people')
plt.title('Years vs %Population using atleast Drinking Water Services')
plt.legend()
output_filename = os.path.join(output_directory, 'RuralvUrban_Basic_Water.png')
plt.savefig(output_filename)
plt.clf()
# --------------------------------------------------------------------------------------
print('Plotted Water')

# access to electricity
ruralpopin = rural.iloc[:,charto('K')-1]
ruralpopw = rural.iloc[:,charto('U')-1]
urbanpopin = urban.iloc[:,charto('S')-1]
urbanpopw = urban.iloc[:,charto('AI')-1]
plt.plot(x,urbanpopin, label='Urban India', color='black')
plt.plot(x,ruralpopin, label='Rural India', color='red')
plt.fill_between(x, urbanpopw, alpha=0.3, label='Urban World', color='blue')
plt.fill_between(x, ruralpopw, alpha=0.3, label='Rural World', color='orange')
plt.xlabel('Years')
plt.ylabel('% of people')
plt.title('Years vs %Population with Access to Electricity')
plt.legend()
output_filename = os.path.join(output_directory, 'RuralvUrban_Electricity.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted access to electricity')

# ------------composite score calculation and plotting------------

years = rural.iloc[51:61,0]

rural_handwash = rural.iloc[51:61, charto('I')-1]
urban_handwash = urban.iloc[51:61, charto('F')-1]

rural_water = rural.iloc[51:61, charto('Q')-1]
urban_water = urban.iloc[51:61, charto('AC')-1]

rural_electricityw = rural.iloc[51:61, charto('U')-1]
urban_electricityw = urban.iloc[51:61, charto('AI')-1]

rural_sanitationw = rural.iloc[51:61, charto('P')-1]
urban_sanitationw = urban.iloc[51:61, charto('V')-1]

composite_score_rural = ( rural_handwash * 0.24 ) + ( rural_water * 0.27 ) + ( rural_electricityw * 0.23) + ( rural_sanitationw * 0.26)
composite_score_urban = ( urban_handwash * 0.24 ) + ( urban_water * 0.27 ) + ( urban_electricityw * 0.23) + ( urban_sanitationw * 0.26)

plt.plot(years,composite_score_urban, label='Urban QoL', color='black')
plt.plot(years,composite_score_rural, label='Rural Qol', color='red')
plt.xlabel('Years')
plt.ylabel('Quality of Life (QoL)')
plt.title('Years v/s Quality of Life in Rural and Urban')
plt.legend()
output_filename = os.path.join(output_directory, 'RuralvUrban_Qol.png')
plt.savefig(output_filename)
plt.clf()
print('Plotted composite line graph')
print('Done all')
