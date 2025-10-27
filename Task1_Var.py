
#Create a variable named pi and check its data type

pi = 22 / 7
print("Value of pi =", pi)
print("Data type of pi =", type(pi))
print()


#Create a variable called 'for' and assign it value 4

print("We cannot assign a value to 'for' because it is a keyword in Python.")
print("Example of error:")
print("for = 4 --> it gives SyntaxError: invalid syntax")
print("Instead, we can use another variable name like 'for_' or 'for_var'.")

for_ = 4
print("Value of for_ =", for_)
print("This works fine because 'for_' is not a keyword.")
print()

# Simple Interest calculation

P = 10000   # Principal amount
R = 5       # Rate of interest (%)
T = 3       # Time in years

# Calculate simple interest
SI = (P * R * T) / 100

print("Principal (P) =", P)
print("Rate (R) =", R, "%")
print("Time (T) =", T, "years")
print("Simple Interest = (P * R * T) / 100")
print(f"= ({P} * {R} * {T}) / 100")
print(f"= {P * R * T} / 100")
print("Simple Interest =", SI)