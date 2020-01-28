import random

playing = True

while playing == True:
    number = random.randint(1, 2)
    guess = input("Heads or Tails: ")

    # Heads is thrown and guessed
    if number == 1 and (guess == 'heads' or guess == 'Heads'):
        print("You flipped a Head and guessed a Head. Well done! ")
        throw = input("\nDo you wish to flip again? ")
    
    # Tails is thrown and guessed
    elif number == 2 and (guess == 'tails' or guess == 'Tails'):
        print("You flipped a Tail and guessed a Tail. Well done! ")
        throw = input("\nDo you wish to flip again? ")

    # Heads is thrown and Tails is guessed
    elif number == 1 and (guess == 'tails' or guess == 'Tails'):
        print("You flipped a Head but guessed a Tail. Unlucky!")
        throw = input("\nDo you wish to flip again? ")

    # Tails is thown and Heads is guessed
    elif number == 2 and (guess == 'heads' or guess == 'Heads'):
        print("You flipped a Tail but guessed a Head. Unlucky!")
        throw = input("\nDo you wish to flip again? ")

    # If neither Heads or Tails is guessed
    else:
        print("You entered incorrect value.")
        throw = input("\nDo you wish to flip again? ")

    if throw == 'yes' or throw == 'Yes' or throw == 'y' or throw == 'Y':
        playing = True
    elif throw == 'no' or throw == 'No' or throw == 'n' or throw == 'N':
        playing = False
