def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 2700,
        "AMZN": 140,
        "MSFT": 330
    }
    
    portfolio = {}   # Dictionary to store user’s stock holdings
    
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    
    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("⚠️ Stock not available in list.")
            continue
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("❗ Please enter a valid number.")
    
    # Calculate total investment
    total_value = 0
    print("\nYour Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_value += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    
    print(f"\n💰 Total Investment Value: ${total_value}")
    
    # Optionally save to file
    save_choice = input("Do you want to save your portfolio to a file? (y/n): ").lower()
    if save_choice == "y":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment: ${total_value}")
        print("✅ Portfolio saved to portfolio.txt")

# Run the tracker
stock_portfolio_tracker()
