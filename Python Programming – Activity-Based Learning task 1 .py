
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter your total travel budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))

expenses = {}

n = int(input("Enter number of expense categories: "))

for i in range(n):
    category = input("\nEnter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (INR, USD, EUR): ").upper()

    rate = float(input("Enter exchange rate in INR: "))

    converted_amount = amount * rate
    fee = converted_amount * fee_rate / 100
    total = converted_amount + fee

    expenses[category] = expenses.get(category, 0) + total

    print("Amount in INR:", round(converted_amount, 2))
    print("Conversion fee:", round(fee, 2))
    print("Total expense in INR:", round(total, 2))

total_spending = sum(expenses.values())

print("\n----- TRAVEL BUDGET REPORT -----")
print("Total Budget: Rs.", round(budget, 2))
print("Total Spending: Rs.", round(total_spending, 2))

for category, amount in expenses.items():
    print(category, ":", round(amount, 2))

largest_category = max(expenses, key=expenses.get)

print("Largest Expense Category:", largest_category)

if total_spending > budget:
    print("You are over budget by Rs.", round(total_spending - budget, 2))
else:
    print("Money left: Rs.", round(budget - total_spending, 2))
