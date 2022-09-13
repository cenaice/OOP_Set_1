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
        choice = input(f"\nYou have ${cash}. Would you like to play (y/n)? ")
        if choice.lower() == 'y':
            cash += spin_wheel()
        else:
            game_on = False


    # Decrease our cash for every play and checks for no money
        cash -= 1
        if cash == 0:
            print("You ran out of money.")
            game_on = False
    
    print("Thanks for playing.")g

def spin_wheel():
    print("Wheel is spinning. . .  \n")

    wheel_one = spin_choices[random.randint(0,5)]
    wheel_two = spin_choices[random.randint(0,5)]
    wheel_three = spin_choices[random.randint(0,5)]
    # Should return payoff amount

    results = f"{wheel_one} {wheel_two} {wheel_three}"

    if "CHERRY" in results:
        # Use a dictionary to give out the amount of cash depending on the amount of cherries in results
        cherry_cash = {
            1:2,
            2:5,
            3:7,
        }
        cherry_count = results.count('CHERRY')
        print(f"{results} -- You win ${cherry_cash[cherry_count]}")
        return cherry_cash[cherry_count]
    
    
    else:
        fruit_cash = {
            "ORANGE":10,
            "PLUM":14,
            "BELL":20,
            "BAR":250,
        }
        # Check for other possibilities
        for fruit in spin_choices:
            if results.count(fruit) == 3 or results.count(fruit) == 2 and "BAR" in results:
                print(f"{results} -- You win ${fruit_cash[fruit]}")
                return fruit_cash[fruit]
        
        # If function reaches this point, no combination was found.
        print(f"{results} -- You lose")



    return 0

spin_choices = ['CHERRY', 'LEMON', 'ORANGE', 'PLUM', 'BELL', 'BAR']
  

one_armed_bandit()
