def generate_financial_report(
    financial_summary,
    profit_summary
):
    report = f"""AI Financial Reporting Assistant Report

FINANCIAL SUMMARY
=================

Total Revenue:
${financial_summary['total_revenue']}

Total Expenses:
${financial_summary['total_expenses']}

Average Revenue:
${financial_summary['average_revenue']}

Average Expenses:
${financial_summary['average_expenses']}

PROFIT SUMMARY
==============

Net Profit:
${profit_summary['net_profit']}

Profit Margin:
{profit_summary['profit_margin']}%
"""

    return report