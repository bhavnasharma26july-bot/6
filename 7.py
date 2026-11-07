# Q1

# Find numbers with exactly 3 factors

# Write a program to find all numbers between 1 and 100 that have exactly three factors, including 1 and the number itself.

# Example: 4 has three factors: 1, 2, 4.

# Constraint: Use nested loops to count the factors of each number


for number in range(1, 101):
    count = 0

    for factor in range(1, number + 1):
        if number % factor == 0:
            count = count + 1

    if count == 3:
        print(number)























