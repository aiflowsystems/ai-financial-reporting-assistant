def calculate_profit(financial_summary):
    total_revenue = financial_summary["total_revenue"]
    total_expenses = financial_summary["total_expenses"]

    net_profit = total_revenue - total_expenses

    if total_revenue == 0:
        profit_margin = 0
    else:
        profit_margin = round((net_profit / total_revenue) * 100, 2)

    return {
        "net_profit": net_profit,
        "profit_margin": profit_margin
    }