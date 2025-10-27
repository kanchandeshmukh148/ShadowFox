# Friends list
friends = ["Aditya", "Kanchan", "Riya", "Sagar", "Meena"]
friends_with_length = [(name, len(name)) for name in friends]
print("Friends with name lengths:", friends_with_length)

# Expenses
your_expenses = {"Hotel": 1200, "Food": 800, "Transport": 500, "Attractions": 300, "Misc": 200}
partner_expenses = {"Hotel": 1000, "Food": 900, "Transport": 600, "Attractions": 400, "Misc": 150}

# Totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())
print("Your total:", your_total)
print("Partner total:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more.")
elif your_total < partner_total:
    print("Your partner spent more.")
else:
    print("Both spent the same.")

# Biggest difference
max_diff = 0
category = ""
for item in your_expenses:
    diff = abs(your_expenses[item] - partner_expenses[item])
    if diff > max_diff:
        max_diff = diff
        category = item

print("Biggest difference in:", category)
print("Difference amount:", max_diff)