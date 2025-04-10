import time
print("Hello, This is my final project")
name = input("What is your name? ")
print("This is a special calculator, I would need two numbers from you ")
number1 = int(input("First number "))
number2 = int(input("Second number "))
print("Thank you for putting in your numbers, " + str(number1) + " and " + str(number2))
flag1 = "even"
if number1 % 2 != 0:
    flag1 = "odd"
print("I can see that the first number is "+ flag1)
flag2 = "even"
if number2 % 2 != 0:
    flag2 = "odd"
print("And the second is " + flag2)
if flag1 == flag2 :
    if flag1 == "even" :
        print("So both of them are even")
    else:
        print("So both of them are odd")
else:
    print("So one of them is even, and one is odd")
operator = input("Operator (+, -, *, /): ")
if operator == "+" :
    result = number1 + number2
    print(str(number1) + "+" + str(number2) + "=" + str(result))
elif operator == "-":
    result = number1 - number2
    print(str(number1) + "-" + str(number2) + "=" + str(result))
elif operator == "*":
    result = number1 * number2
    print(str(number1) + "*" + str(number2) + "=" + str(result))
elif operator == "/":
    answer = input("You chose division, should the result be integer? (y/n) ").strip().lower()
    if answer == "y" and number2 != 0:
        result = number1 // number2
        print(str(number1) + "/" + str(number2) + "=" + str(result))
    elif answer == "n" and number2 != 0:
        result = number1 / number2
        print(str(number1) + "/" + str(number2) + "=" + str(result))
    else:
         if number2 == 0:
                print("Error: num_2 is zero") 
                print("An error had occured , please try again")
else:
    print("Error : Operator " + operator +" is not supported")
    print("An error had occured , please try again")
print("Thank you "+name +" for using the calculator on " + time.ctime())





