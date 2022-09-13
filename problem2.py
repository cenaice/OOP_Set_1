# Victer Phiathep
# RUID : 179005525

import random

def one_armed_bandit():
    welcome  = """\tThe One-Armed Bandit Welcomes You
\t---------------------------------"""
    print(welcome)
    cash = 50

    
    # Using a while loop to continously run our slot machine
    game_on = True
    while game_on:
        choice = input(f"You have ${cash}. Would you like to play (y/n)? ")
        if choice.lower() == 'y':
            spin_wheel()
        else:
            game_on = False


    # Decrease our cash for every play and checks for no money
    cash -= 1
    if cash == 0:
        print("You ran out of money.")
        game_on = False
    
    print("Thanks for playing.")

    # Start with $50
    # Use a while loop to take away $1 every round

def spin_wheel():
    print("Wheel is spinning!")
    wheel_one = spin_choices[random.randint(0,6)]
    wheel_two = spin_choices[random.randint(0,6)]
    wheel_three = spin_choices[random.randint(0,6)]
    # Should return payoff amount


spin_choices = ['CHERRY', 'LEMON', 'ORANGE', 'PLUM', 'BELL', 'BAR']
  

one_armed_bandit()
