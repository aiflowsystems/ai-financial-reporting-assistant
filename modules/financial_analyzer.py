def analyze_financial_data(financial_data):
    total_revenue = 0
    total_expenses = 0

    for record in financial_data:
        revenue = int(record["revenue"])
        expenses = int(record["expenses"])

        total_revenue += revenue
        total_expenses += expenses

    record_count = len(financial_data)

    average_revenue = round(total_revenue / record_count, 2)
    average_expenses = round(total_expenses / record_count, 2)

    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "average_revenue": average_revenue,
        "average_expenses": average_expenses
    }