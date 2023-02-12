# import random module
import random

# print rules for the winning the game...
print('\nWinning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user
    choice = int(input("Enter your choice : "))

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please!!\n'))

    # initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # print user choice
    print('User choice is: ', choice_name)
    print("\nNow its Computer's Turn....\n")

    # Computer chooses randomly any number from 1,2 or 3 using randint method of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: ", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    # condition for draw
    if choice == comp_choice:
        print("It's a draw...",end="")
        result = "DRAW"

    # conditions for winning
    if choice == 1 and comp_choice == 2:
        print('\nPaper wins ', end="")
        result = 'Paper'
    elif choice == 2 and comp_choice == 1:
        print('\nPaper wins ', end="")
        result = 'Paper'

    if choice == 1 and comp_choice == 3:
        print('\nRock wins ', end="")
        result = 'Rock'
    elif choice == 3 and comp_choice == 1:
        print('\nRock wins ', end="")
        result = 'RocK'

    if choice == 2 and comp_choice == 3:
        print('\nScissors wins ', end="")
        result = 'Scissor'
    elif choice == 3 and comp_choice == 2:
        print('\nScissors wins', end="")
        result = 'Scissor'

    # Printing either user or computer wins, or it is a draw
    if result == 'DRAW':
        print(" --> It's a tie!!!")
    if result == choice_name:
        print(" --> User wins!!!")
    else:
        print(" --> Computer wins!!!")

    print("\nDo you want to play again? (Y/N)")

    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break

# after coming out of the while loop
print("Thanks for playing....")
