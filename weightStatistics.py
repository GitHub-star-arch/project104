import csv
import statistics as stats
import pandas as pd

info_df = pd.read_csv('SOCR-HeightWeight.csv')
print(info_df)

weight_list = info_df['Weight(Pounds)'].tolist() 
print(weight_list)

mean = round(stats.mean(weight_list), 3)
mode = round(stats.mode(weight_list), 3)
median = round(stats.median(weight_list), 3)

print(f"Yor mean is {mean}")
print(f"Yor median is {median}")
print(f"Yor mode is {mode}")

""" with open('SOCR-HeightWeight.csv', newline='') as f:
    data = csv.reader(f)
    weight_list = list(data)

print(weight_list)
weight_list.pop(0)
sum = 0
for i in weight_list:
    sum = sum + float(i[1])
weight_mean = round(sum/len(weight_list), 3)
print(f'The mean of weight is {weight_mean}') """