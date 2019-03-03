import os
import csv
file = os.path.join('budget_data.csv')


with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)



    #creating empty lists for variables values  
    month_count = []
    profit = []
    change_profit = []
    
                      
    # loop through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])


        
                      
# calculate  the max and min 
increase = max(change_profit)
decrease = min(change_profit)
 

month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


# results 

print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"the Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"the Greatest Decrease in losses: {month_count[month_decrease]} (${(str(decrease))})")      


output = os.path.join("pypanktest.txt")

with open(output,"w") as new:
    new.write("Financial Analysis")
    

    new.write(f"Total Months:{len(month_count)}")
    new.write(f"Total: ${sum(profit)}")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")

    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")