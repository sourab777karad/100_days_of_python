print("WELCOME TO HIGH PASSWORD GENERATOR!!")

letters = int(input("enter the total number of letters you want to input in your password :"))
if letters <= 4 or letters > 20:
    print("password to weak! please enter again")
    exit()
else:
    print(letters)
name = input("input the name for password :")

numbers = int(input("enter the total number of numbers you want to input in your password :"))
if numbers < 2 or numbers > 5:
    print("need atmost 2 numbers for high end password!!")
    exit()
else:
    print(letters, numbers)
in_numbers = int(input("enter the numbers you want to input"))
if in_numbers <= numbers:
    print("error")
    exit()
else:
    print("next!")

symbols = input("enter the symbols you want (@, $, %, &, *, +,) :")

password = print(name,symbols,in_numbers)