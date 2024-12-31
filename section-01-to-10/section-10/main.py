def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2 == 0 :
        print("Error! Can not divide for 0!")
        return
    return n1/n2

from art import logo
print(logo)

cal_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
memory = "X"
while True :
    first_number = memory
    if memory == "X" :
        first_number = float(input("What's your first number?: "))
    while True:
        math_op = input("What's your math operator (+ or - or * or /)?: ")
        if math_op in cal_dict :
            break
        else:
            print("You can only input + or - or * or /")
    second_number = float(input("What's your second number?: "))

    memory = cal_dict[math_op](first_number, second_number)
    if memory != None :
        print(f"Result: {first_number}{math_op}{second_number}={memory}")

    confirm = input("Do you want to stop the program(yes/no)?: ")
    if confirm == "yes":
        break

    if memory != None:
        confirm = input("Do you want to continue working with the previous result(yes/no)?: ")
    if confirm == "no":
        memory = "X"
