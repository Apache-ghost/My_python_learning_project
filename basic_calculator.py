def add(a, b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result) + "\n")

def sub(a, b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result) + "\n")

def mul(a, b):
    result = a * b
    print(str(a) + " * " + str(b) + " = " + str(result) + "\n")

def div(a, b):
    result = a / b
    print(str(a) + " / " + str(b) + " = " + str(result) + "\n")

while True:
    print('A. addition')
    print('B. subtraction')
    print('C. multiplication')
    print('D. division')
    print("E. exit")

    choice = input("Enter your choice: ")
    if choice == 'a' or choice == 'A':
        print("Addition")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        add(num1, num2)
    elif choice == 'b' or choice == 'B':
        print("Subtraction")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        sub(num1, num2)
    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        mul(num1, num2)
    elif choice == 'd' or choice == 'D':
        print("Division")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        div(num1, num2)
    elif choice == 'e' or choice == 'E':
        print("Program ended")
        break
    else:
        print("Invalid choice. Please try again.\n")