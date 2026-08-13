n = int(input("Enter Number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum += factorial
    n = n // 10

if sum == original:
    print("Strong Number")
else:
    print("Not Strong Number")