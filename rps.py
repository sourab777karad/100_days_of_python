import random



rock = print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
images = (rock, paper, scissors)
user_input = int(input("enter what do you want to choose? type 0 for rock, 1 for paper and 2 for scissors :\n"))
if user_input >= 3 or user_input < 0:
    print("choose a number from 0-2 bro!!! you lose")
else:
    print(images[user_input])

computer_choice = random.randint(0, 2)
print(images[computer_choice])
print(f"computer choose : {computer_choice}")


if user_input == 0 and computer_choice == 2:
    print("****YOU WIN****")
    
elif computer_choice == 0 and user_input == 2:
    print("****you lose****")
    
elif computer_choice > user_input:
    print("****YOU LOSE****")
    
elif user_input > computer_choice:
    print("****you win****")
    
elif user_input == computer_choice:
    print("it's a draw. try again")
    
    

