numbers = [10, 25, 7, 40, 18]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum =", minimum)