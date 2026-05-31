# Stock Portfolio Tracker

portfolio = {}

while True:
    print("\n--- Stock Portfolio Tracker ---")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Save Portfolio")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock = input("Enter stock name: ").upper()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter purchase price: "))

        portfolio[stock] = {
            "quantity": quantity,
            "price": price
        }

        print("Stock added successfully!")

    elif choice == "2":
        total_investment = 0

        print("\nPortfolio Details:")
        for stock, details in portfolio.items():
            investment = details["quantity"] * details["price"]
            total_investment += investment

            print(
                f"{stock} - Quantity: {details['quantity']}, "
                f"Price: {details['price']}, "
                f"Investment: {investment}"
            )

        print("Total Investment:", total_investment)

    elif choice == "3":
        file = open("portfolio.txt", "w")

        for stock, details in portfolio.items():
            file.write(
                f"{stock},{details['quantity']},{details['price']}\n"
            )

        file.close()
        print("Portfolio saved to file!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
