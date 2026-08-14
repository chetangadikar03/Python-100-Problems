start = int(input("Enter Start: "))
end = int(input("Enter End: "))

sum = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers =", sum)