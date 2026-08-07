n = int(input("Enter Number :"))

sum = 0 

while n > 0:
    digit = n % 10
    sum += digit
    n = n //10

print("Sum=",sum)
