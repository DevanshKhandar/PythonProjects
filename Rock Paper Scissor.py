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

n = int(input("Press 0 for rock, 1 for paper, 2 for scissors: "))
c = random.randint(0, 2)

if n == 0:
    print(rock)
    print("Rock")

elif n == 1:
    print(paper)
    print("Paper")

elif n == 2:
    print(scissors)
    print("Scissor")
    
print("Computer chose:")

if c == 0:
    print(rock)
    print("Rock")

elif c == 1:
    print(paper)
    print("Paper")

elif c == 2:
    print(scissors)
    print("Scissor")

if n == 0 and c == 1:
    print("You win!")

elif n == 0 and c == 0:
    print("It's a draw")

elif n == 0 and c == 2:
    print("You lose!")

elif n == 1 and c == 2:
    print("You win!")

elif n == 1 and c == 1:
    print("It's a draw")

elif n == 1 and c == 0:
    print("You lose!")

elif n == 2 and c == 1:
    print("You win!")

elif n == 2 and c == 2:
    print("It's a draw")

elif n == 2 and c == 0:
    print("You lose!")
