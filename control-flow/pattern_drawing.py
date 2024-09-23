# pattern_drawing.py

# Prompt for user input
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the pattern
while row < size:  # Loop for each row
    for col in range(size):  # Loop for each column
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line
    row += 1  # Increment the row counter