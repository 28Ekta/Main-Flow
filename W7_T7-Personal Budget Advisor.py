# Mini Project :- Personal Budget Advisor

def budget_advisor():
    income = 0
    expenses = {}

    def show_summary():
        total_expense = sum(expenses.values())
        savings = income - total_expense

        print("\n========== 📊 Budget Summary ==========")
        print(f"💰 Total Income: {income:.2f}")
        print(f"🧾 Total Expenses: {total_expense:.2f}")
        print(f"💵 Savings: {savings:.2f}")
        print("=======================================")

        # Category-wise breakdown
        if expenses:
            print("\n--- Category-wise Breakdown ---")
            for category, amount in expenses.items():
                percentage = (amount / income) * 100 if income > 0 else 0
                print(f"➡️ {category}: {amount:.2f} ({percentage:.2f}%)")
        else:
            print("No expenses recorded.")

        # Suggestions
        print("\n========== 💡 Suggestions ==========")
        if income == 0:
            print("⚠️ Please set your income first to get suggestions.")
        else:
            if savings < 0:
                print("⚠️ You are overspending! Cut down unnecessary expenses immediately.")
            elif savings < 0.2 * income:
                print("💡 Try to increase your savings. Aim for at least 20% of income.")
            else:
                print("✅ Excellent! You are maintaining healthy savings.")
            
            if expenses:
                highest_category = max(expenses, key=expenses.get)
                print(f"🔎 Your highest spending is on '{highest_category}'. Consider reducing it if possible.")
        print("=======================================")

    # Main Menu Loop
    while True:
        print("\n========== 📌 Personal Budget Advisor ==========")
        print("1️⃣  Set / Update Income")
        print("2️⃣  Add Expense")
        print("3️⃣  View Budget Summary")
        print("4️⃣  Exit")
        print("===============================================")

        choice = input("👉 Choose an option (1-4): ")

        if choice == "1":
            while True:
                try:
                    new_income = float(input("Enter your monthly income: "))
                    if new_income <= 0:
                        print("⚠️ Income must be greater than 0. Try again.")
                        continue
                    income = new_income
                    print(f"✅ Income updated to {income:.2f}")
                    break
                except ValueError:
                    print("⚠️ Invalid input! Please enter a numeric value for income.")

        elif choice == "2":
            if income == 0:
                print("⚠️ Please set your income first before adding expenses.")
                continue
            category = input("Expense Category (e.g., Food, Rent, Travel): ").strip()
            if not category:
                print("⚠️ Category cannot be empty.")
                continue
            try:
                amount = float(input(f"Enter amount for {category}: "))
                if amount < 0:
                    print("⚠️ Expense cannot be negative.")
                    continue
                expenses[category] = expenses.get(category, 0) + amount
                print(f"✅ Added {amount:.2f} to {category}.")
            except ValueError:
                print("⚠️ Invalid amount! Please enter a number.")

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("\n👋 Thank you for using Personal Budget Advisor. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select between 1-4.")

# Run the program
if __name__ == "__main__":
    budget_advisor()

