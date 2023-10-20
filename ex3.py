'''
Exercise rock, paper, scissors
'''

import random

# 1. Create a list of rock, paper, scissors in a variable called rps.
# "rps" means rock, paper, scissors
rps = ['rock','paper','scissors']

# 2. Create a variable called user_choice that takes input from the user and stores it.
#   Make sure the user enters rock, paper, or scissors.
user_choice = "" # fix this, user input, hint: use input("...")

# 3. Create a variable called computer_choice that randomly chooses from rps.
computer_choice = "" # fix this, random choice from rps

# 4. Print out the user_choice and the computer_choice.
print("You chose: " + user_choice)
print("The computer chose: " + computer_choice)

# 5. Print out the winner of rock, paper, scissors.
# continue this if statement to print out the winner
if user_choice == computer_choice:
  print("It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
  print("You Win")
elif user_choice == 'paper' and computer_choice == 'rock' :  
 print ("You Win")
elif user_choice == 'scissors' and computer_choice == 'paper':
 print("You Win")
else: 
 print("You Lose")
