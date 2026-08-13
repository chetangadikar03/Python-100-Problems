n = int(input("Enter Number of values: "))

positive = 0
negative = 0

for i in range(n):
    num = int(input("Enter number: "))

    if num >= 0:
        positive += 1
    else:
        negative += 1

print("Positive numbers =", positive)
print("Negative numbers =", negative)