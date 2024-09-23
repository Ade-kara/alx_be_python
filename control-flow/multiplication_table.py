# multiplication_table.py

# Prompt for user input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):  # Loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")