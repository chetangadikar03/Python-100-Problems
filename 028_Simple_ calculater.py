a= float (input("Enter First Number :"))
b= float (input("Enter Second Number :"))

op= input("Enter operator(+,-,*,/):")

if op == "+":
    print("Answer=",a+b)
elif op == "-":
    print("Answer=",a-b)
elif op == "*":
    print("Answer=",a*b)
elif op == "/":
    print("Answer=",a/b)
else:
    print("Invalid Operator")