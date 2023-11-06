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
choices = [rock, paper, scissors]
user_choice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))]
cpu_choice = choices[random.randint(0, 2)]

print(user_choice, "\n")
print("Computer chose:")
print(cpu_choice, "\n")

if user_choice == cpu_choice:
    print("It's a draw")
else:
    if user_choice == rock:
        if cpu_choice == paper:
            print("You lose.")
        else:
            print("You win!")
    elif user_choice == paper:
        if cpu_choice == rock:
            print("You lose.")
        else:
            print("You win!")
    elif user_choice == scissors:
        if cpu_choice == rock:
            print("You lose.")
        else:
            print("You win!")
