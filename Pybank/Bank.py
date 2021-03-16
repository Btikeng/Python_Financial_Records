import os, csv
from pathlib import Path
file = Path("budget_data.csv")
profit = []
profitDifference = []
months = []
with open(file, newline="", encoding="utf-8") as budget:
    reader = csv.reader(budget, delimiter=",")
    head = next(reader)
    for row in reader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit) - 1):
        profitDifference.append(profit[i + 1] - profit[i])
MaxIncValue = max(profitDifference)
MaxDecValue = min(profitDifference)
MaxIncMonth = profitDifference.index(max(profitDifference)) + 1
MaxDecMonth = profitDifference.index(min(profitDifference)) + 1
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profitDifference) / len(profitDifference), 2)}")
print(f"Greatest Increase in Profits: {months[MaxIncMonth]} (${(str(MaxIncValue))})")
print(f"Greatest Decrease in Profits: {months[MaxDecMonth]} (${(str(MaxDecValue))})")

output_file = Path("FinancialAnalysisSummary.txt")

with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profitDifference) / len(profitDifference), 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[MaxIncMonth]} (${(str(MaxIncValue))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[MaxDecMonth]} (${(str(MaxDecValue))})")