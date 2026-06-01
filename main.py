import csv
import json
from pathlib import Path
from modules.financial_analyzer import analyze_financial_data
from modules.profit_calculator import calculate_profit
from modules.report_generator import generate_financial_report

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]
Path(output_folder).mkdir(exist_ok=True)

financial_data = []

with open("financial_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        financial_data.append(row)

financial_summary = analyze_financial_data(financial_data)
profit_summary = calculate_profit(financial_summary)
financial_report = generate_financial_report(
    financial_summary,
    profit_summary
)

print("AI Financial Reporting Assistant")
print("================================")
print()

print(f"Financial records loaded: {len(financial_data)}")

for record in financial_data:
    print(record["month"], "-", record["revenue"], "-", record["expenses"])

print()
print("FINANCIAL SUMMARY")
print("-----------------")
print(f"Total Revenue: ${financial_summary['total_revenue']}")
print(f"Total Expenses: ${financial_summary['total_expenses']}")
print(f"Average Revenue: ${financial_summary['average_revenue']}")
print(f"Average Expenses: ${financial_summary['average_expenses']}")

print()
print("PROFIT SUMMARY")
print("--------------")
print(f"Net Profit: ${profit_summary['net_profit']}")
print(f"Profit Margin: {profit_summary['profit_margin']}%")

report_file = (
    Path(output_folder)
    / config["financial_report_file"]
)

with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:
    file.write(financial_report)

print()
print(
    f"Financial report generated: "
    f"{report_file}"
)
