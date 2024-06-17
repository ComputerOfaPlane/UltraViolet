import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

bank = pd.read_excel("bank.ods", engine="odf")

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

x = bank.iloc[:,0]

# broad money trend
y = bank.iloc[:,charto('E')-1]
plt.plot(x,y,color='black')
plt.xlabel('Years')
plt.ylabel('Broad money (current LCU)')
plt.title('Years vs Broad money')
output_filename = os.path.join(output_directory, 'Broad_Money.png')
plt.savefig(output_filename)
plt.clf()
print('Broad money')

# banking presence
y = bank.iloc[:,charto('B')-1]
plt.plot(x,y,color='black')
plt.xlabel('Years')
plt.ylabel('Commercial bank branches (per lakh adults)')
plt.title('Years vs Banking Presence')
output_filename = os.path.join(output_directory, 'Banking Presence.png')
plt.savefig(output_filename)
plt.clf()
print('Banking Presence')

# real interest rate
lrint = bank.iloc[18:61, charto('C')-1]
xrint = bank.iloc[18:61,0]
rint = bank.iloc[18:61,charto('F')-1]
coefficients = np.polyfit(xrint, rint, 1)
polynomial = np.poly1d(coefficients)
plt.plot(xrint, polynomial(xrint), color='black', label='Real Interest (best fit)')
plt.plot(xrint, rint, color='blue')
plt.scatter(xrint,rint,color='red',label='Real Interest (inflation adjusted) data points')
plt.plot(xrint, lrint, color='magenta', label='Lending Interest Rate')
plt.legend()
plt.xlabel('Years')
plt.ylabel('Interest Rate %')
plt.title('Years vs Interest Rate')
output_filename = os.path.join(output_directory, 'Interest.png')
plt.savefig(output_filename)
plt.clf()
print('Interest Rate')

x = bank.iloc[49:61,0]
y1 = bank.iloc[49:61, charto('G')-1]

# non performing & % interest as expense
y2 = bank.iloc[49:61,charto('D')-1] # expense %
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('Years')
ax1.set_ylabel('Bank nonperforming loans to total gross loans (%)', color=color)
ax1.plot(x, y1, color=color, label='Bank nonperforming loans')
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Interest payments (% of expense)', color=color)
ax2.plot(x, y2, color=color, label='interest amount % of expense')
ax2.tick_params(axis='y', labelcolor=color)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='lower right')
plt.title('Bank nonperforming loans and Interest payments over Years')
output_filename = os.path.join(output_directory, 'NPA_IntPayment.png')
plt.savefig(output_filename)
plt.clf()
print('Bank nonperforming loans and Interest payments over Years')

# non performing & interest rate
y2 = bank.iloc[49:61,charto('C')-1] # lending %
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('Years')
ax1.set_ylabel('Bank nonperforming loans to total gross loans (%)', color=color)
ax1.plot(x, y1, color=color, label='Bank nonperforming loans')
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Lending interest rate (%)', color=color)
ax2.plot(x, y2, color=color, label='Lending interest rate (%)')
ax2.tick_params(axis='y', labelcolor=color)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='lower right')
plt.title('Bank nonperforming loans and Lending interest rate (%)')
output_filename = os.path.join(output_directory, 'NPA_lending.png')
plt.savefig(output_filename)
plt.clf()
print('Bank nonperforming loans and lending %')
