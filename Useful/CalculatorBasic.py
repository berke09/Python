

def calculator(num1,num2):
    print(f"number_1 = {num1}")
    print(f"number_2 = {num2}")
    process = input("please choose a figure +,-,/,* : ")
    if process == "+":
        return num1+num2
    elif process == "-":
        return num1-num2
    elif process == "/":
        return num1/num2
    elif process == "*":
        return num1*num2
    else :
        return "please only choose +,-,/,* "


while True : 
    num1 = int(input("please type a number as number 1 :"))
    num2 = int(input("please type a number as number 2 :"))

    print(calculator(num1,num2))