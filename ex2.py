'''
Exercises for random
'''

import random

# 1. Write some code that prints the numbers from 1 to 10 and stores them in a list called numbers.
numbers = list(range(1,11))
print(numbers)

# 2. Shuffle the list and print it out.
random.shuffle(numbers)
print(numbers)

# 3. Choose a random number from the list and print it out.
random_number = random.choice(numbers)
print(f"Random number from the list: {random_number}")

# 4. Choose a random number from 1 to 100 and print it out.
random_number=random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# 5. Sample 5 numbers uniques from numbers list and print them out.
random_samples = random.sample(numbers,5) 
print("Random samples:", random_samples)

# 6. Create a list of days of the week in a variable days and print a random day of the week.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random_day = random.choice(days)
print("Random day of the week:", random_day)


# 7. Dice roll simulator: print a random number from 1 to 6.
dice_roll = random.randint(1, 6)
print("Dice roll:", dice_roll)

# 8. Coin flip: randomly chooses "heads" or "tails".
coins = ['heads','tails']
coin = random.choice(coins)
print("Coin flip:", coin)

# 9. Ask the user for a number and print out a random number from 1 to the number the user chooses.
# hint: use int(input("..."))
user_number = int(input("Choose a number"))
random_number = random.randint(1,user_number)
print(f"Random number from 1 to {user_number}: {random_number}")


# 10. Ask the user to guess a number from 1 to 10 and tell them whether they guessed correctly or not.
random_number = random.randint(1, 10)
while True: #Se que no hacia falta el while, pero para que quedase mas bonito
    user_guess = int(input("Guess a Number from 1 to 10:"))
    if user_guess == random_number:
        print("You guessed correctly!")
        break  
    else:
        print("Try again.")

