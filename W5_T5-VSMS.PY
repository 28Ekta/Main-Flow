# W5_Task5-
# Mini project : - Virtual Stock Market Simulator

import random

class StockMarket:
    """A simple virtual stock market simulator."""

    def __init__(self):
        # Initial stock prices
        self.stocks = {
            "AAPL": 150.0,
            "GOOG": 2800.0,
            "TSLA": 700.0,
            "AMZN": 3400.0
        }
        self.portfolio = {}        # Stores owned stocks
        self.balance = 10000.0     # Starting cash balance

    # ---------------------------
    # Display current market prices
    # ---------------------------

    def show_market(self):
        print("\n📈 Current Stock Prices:")
        for stock, price in self.stocks.items():
            print(f"   {stock}: ${price:.2f}")

    # ---------------------------
    # Simulate price changes (-5% to +5%)
    # ---------------------------

    def update_prices(self):
        for stock in self.stocks:
            change_percent = random.uniform(-5, 5)
            self.stocks[stock] *= (1 + change_percent / 100)
            self.stocks[stock] = round(self.stocks[stock], 2)
        print("\n📊 Prices updated for the next day.")

    # ---------------------------
    # Buy stocks
    # ---------------------------

    def buy_stock(self, stock, quantity):
        if stock not in self.stocks:
            print("❌ Stock not found.")
            return

        total_cost = self.stocks[stock] * quantity
        if total_cost > self.balance:
            print("❌ Not enough balance.")
            return

        self.balance -= total_cost
        self.portfolio[stock] = self.portfolio.get(stock, 0) + quantity
        print(f"✅ Bought {quantity} shares of {stock} at ${self.stocks[stock]:.2f} each.")

    # ---------------------------
    # Sell stocks
    # ---------------------------

    def sell_stock(self, stock, quantity):
        if stock not in self.portfolio or self.portfolio[stock] < quantity:
            print("❌ You don't have enough shares.")
            return

        total_income = self.stocks[stock] * quantity
        self.balance += total_income
        self.portfolio[stock] -= quantity

        if self.portfolio[stock] == 0:
            del self.portfolio[stock]

        print(f"✅ Sold {quantity} shares of {stock} at ${self.stocks[stock]:.2f} each.")

    # ---------------------------
    # Display portfolio details
    # ---------------------------

    def show_portfolio(self):
        print("\n💼 Your Portfolio:")
        if not self.portfolio:
            print("   No stocks owned.")
        else:
            for stock, quantity in self.portfolio.items():
                value = self.stocks[stock] * quantity
                print(f"   {stock}: {quantity} shares (Value: ${value:.2f})")

        print(f"💰 Balance: ${self.balance:.2f}")


# ---------------------------
# Main Simulation Loop
# ---------------------------

def main():
    market = StockMarket()

    while True:
        print("\n--- Virtual Stock Market ---")
        print("1. Show Market Prices")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. View Portfolio")
        print("5. Next Day (Price Update)")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            market.show_market()

        elif choice == "2":
            stock = input("Enter stock symbol: ").upper()
            try:
                quantity = int(input("Enter quantity: "))
                market.buy_stock(stock, quantity)
            except ValueError:
                print("❌ Please enter a valid quantity.")

        elif choice == "3":
            stock = input("Enter stock symbol: ").upper()
            try:
                quantity = int(input("Enter quantity: "))
                market.sell_stock(stock, quantity)
            except ValueError:
                print("❌ Please enter a valid quantity.")

        elif choice == "4":
            market.show_portfolio()

        elif choice == "5":
            market.update_prices()

        elif choice == "6":
            print("👋 Exiting the simulator. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# Run the simulation

if __name__ == "__main__":
    main()
