STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

def stock_portfolio_tracker():
    print("=" * 45)
    print("      STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    total_value = 0

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found.")
            continue

        quantity = int(input("Enter quantity: "))

        investment = STOCK_PRICES[stock] * quantity
        total_value += investment

        print(f"Investment in {stock}: ${investment}")

    print("\nTotal Portfolio Value: $", total_value)

    with open("portfolio_summary.txt", "w") as file:
        file.write(f"Total Portfolio Value: ${total_value}")

    print("Portfolio summary saved to portfolio_summary.txt")

if __name__ == "__main__":
    stock_portfolio_tracker()
