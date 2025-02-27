import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

the_First_launch = [rock, paper, scissors]

while True:
    try:
        afnan = int(input("What do you choose? Type: 0 for Rock, 1 for Paper, 2 for Scissors (or -1 to quit): "))
        if afnan == -1:
            print("Thanks for playing!")
            break
        if afnan < 0 or afnan > 2:
            print("Invalid choice. Please choose 0, 1, or 2.")
            continue
        
        print("You chose:")
        print(the_First_launch[afnan])
        
        machine = random.randint(0, 2)
        print("Machine chose:")
        print(the_First_launch[machine])
        
        if afnan == machine:
            print("It's a draw!")
        elif (afnan == 0 and machine == 2) or (afnan == 1 and machine == 0) or (afnan == 2 and machine == 1):
            print("You win!")
        else:
            print("You lose!")
    except ValueError:
        print("Invalid input. Please enter a number.")


