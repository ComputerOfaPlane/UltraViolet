import pandas as pd
import numpy as np

health = pd.read_excel("health.ods", engine="odf")

def charto(label):
    uppercase_label = label.upper()
    if not all('A' <= char <= 'Z' for char in uppercase_label):
        return "Invalid input. Please provide a valid uppercase letter or letters."
    result = 0
    for char in uppercase_label:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

x = health.iloc[:,0]

current_health_expend_per_capita_in = health.iloc[:,charto('N')-1]
current_health_expend_per_capita_w = health.iloc[:,charto('AK')-1]

government_health_expend_per_capita_in = health.iloc[:,charto('Q')-1]
government_health_expend_per_capita_w = health.iloc[:,charto('AN')-1]

external_health_expenditure_current_in = health.iloc[:,charto('X')-1]

print('Did increasing Domestic government impact external health expenditure? (for india)')
correlation_coefficient_q2 = government_health_expend_per_capita_in.corr(external_health_expenditure_current_in)
print(f'Correlation Coefficient: {correlation_coefficient_q2:.2f}\n')

correlation_coefficient_years_cuurent_health_in = x.corr(current_health_expend_per_capita_in)
print(f'Correlation Coefficient (years, current health expend per capita india): {correlation_coefficient_years_cuurent_health_in:.2f}')

correlation_coefficient_years_cuurent_health_w = x.corr(current_health_expend_per_capita_w)
print(f'Correlation Coefficient (years, current health expend per capita world): {correlation_coefficient_years_cuurent_health_w:.2f}')

correlation_coefficient_years_government_health_expend_in = x.corr(government_health_expend_per_capita_in)
print(f'Correlation Coefficient (years, government health expenditure per capita india):{correlation_coefficient_years_government_health_expend_in:.2f}')

correlation_coefficient_years_government_health_expend_w = x.corr(government_health_expend_per_capita_w)
print(f'Correlation Coefficient (years, government health expenditure per capita world):{correlation_coefficient_years_government_health_expend_w:.2f}')

birth_by_skilled_in = health.iloc[:,charto('D')-1]
birth_by_skilled_w = health.iloc[:,charto('AD')-1]
correlation_coefficient_birth_in = x.corr(birth_by_skilled_in)
correlation_coefficient_birth_w = x.corr(birth_by_skilled_w)
print(f'Correlation Coefficient (years,% birth by skilled workers in world): {correlation_coefficient_birth_w:.2f}')
print(f'Correlation Coefficient (years,% birth by skilled workers in india): {correlation_coefficient_birth_in:.2f}')

out_of_pocket_expenditure_in = health.iloc[:,charto('E')-1]
out_of_pocket_expenditure_w = health.iloc[:,charto('AE')-1]
correlation_coefficient_out_in = x.corr(out_of_pocket_expenditure_in)
correlation_coefficient_out_w = x.corr(out_of_pocket_expenditure_w)
print(f'Correlation Coefficient (years,Out-of-pocket expenditure (% of current health expenditure) in world): {correlation_coefficient_out_w:.2f}')
print(f'Correlation Coefficient (years,Out-of-pocket expenditure (% of current health expenditure) in india): {correlation_coefficient_out_in:.2f}')
