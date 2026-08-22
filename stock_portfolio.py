# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

print("===== Stock Portfolio Tracker =====")

stock_name = input("Enter stock symbol: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("\n----- Portfolio Summary -----")
    print("Stock:", stock_name)
    print("Quantity:", quantity)
    print("Price per share: $", price)
    print("Total Investment: $", total_investment)

    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price per share: ${price}\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("\nResult saved to portfolio.txt")

else:
    print("Stock not available.")