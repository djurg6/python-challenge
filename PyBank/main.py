import csv
# import pandas as pd

file = 'budget_data.csv'

total_months = 0
total_net = 0
month_change = []
net_change_list = []
greatest_increase = ['',0]
greatest_decrease = ['',9999999]

with open(file,'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_month_net = int(first_row[1])
    
    for i in reader:
        total_months = total_months + 1
        total_net = total_net + int(i[1])
        
        net_change = int(i[1]) - prev_month_net
        prev_month_net = int(i[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [i[0]]
        # average_change = sum(net_change_list) / len(net_change_list)
        # greatest_increase = max(net_change_list)
        # greatest_decrease = min(net_change_list)
        # increase_index = net_change_list.index(greatest_increase)
        # decrease_index = net_change_list.index(greatest_decrease)
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = i[0]
            greatest_increase[1] = net_change
            
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = i[0]
            greatest_decrease[1] = net_change
            
net_monthly_average = round(sum(net_change_list) / len(net_change_list),2)
        
with open(file, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    
#     for i in range (increase_index + 1):
#         next(reader)
#     increase_date = next(reader)[0]
    
#     for i in range(decrease_index + 1):
#         next(reader)
#     decrease_date = next(reader)[0]
    
print("Financial Analysis of PyBank")
print("----------------------------")
print(f"Total Months in Set: {total_months}")
print(f"Total P/L: ${total_net}")
print(f"Average Change in P/L: ${net_monthly_average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

