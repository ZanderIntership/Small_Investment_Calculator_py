initial_investment = float(input("Enter Initial Investment: R"))
investment_period = int(input("Enter Investment Period (months): "))
investment_per_month = float(input("Enter Investment per Month: R"))
investment_rate_percent = float(input("Enter Investment Rate (% per month): "))

rate = investment_rate_percent / 100.0
multiplier = 1.0 + rate

balance = initial_investment

for month in range(1, investment_period + 1):
    start_balance = balance
    balance = (balance + investment_per_month) * multiplier

    print(
        f"Month {month}: "
        f"Start R{start_balance:,.2f} + R{investment_per_month:,.2f} "
        f"@ {investment_rate_percent:.2f}% -> R{balance:,.2f}"
    )
