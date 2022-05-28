def Calculator(): #simple program demostrating if statements
    num1 = float(input("Enter first number: ")) #user imputs what to calculate
    oper = input("Enter operator: ")
    num2 = float(input("Enter second number: ")) #float so only numbers can be inputted
    if oper == "+": #determines what calculation has to be done
        print("The answer is", num1 + num2) #prints out answer
    elif oper == "-":
        print("The answer is", num1 - num2)
    elif oper == "/":
        print("The answer is", num1 / num2)
    elif oper == "*":
        print("The answer is", num1 * num2)
    else:
        print("That is not possible, Try again") #if wrong operator is entered
        Calculator()
Calculator()
