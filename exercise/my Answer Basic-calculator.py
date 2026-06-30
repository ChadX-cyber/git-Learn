
num1 = int(input("Enter the first number: " ))
num2 = int(input("Enter the second number: " ))
op = input("enter operator + or - or * or /: ")

def add ():
    if op == "+":
        print("You choose add and the answer is:", num1+num2)
    else:
        print("error")

def subtract():
    if op == "-":
        print("You choose subtract and the answer is:", num1-num2)

    else:
        print("error subtract")
def multiply():
    if op == "*":
        print("You choose Multiply and the answer is: ", num1*num2)
    else:
        print("error multiply")
def division():
    if op == "/":
        print("You choose division and the answer is: ", num1/num2)
    else:
        print("error division")

def operation():
    if op =="+":
        add()
    elif op == "-":
        subtract()
    elif op == "*":
        multiply()
    elif op == "/":
        division()
    else:
        print("Error on operator")
    
operation()

    

