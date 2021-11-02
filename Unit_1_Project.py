#  Reject if exceeds not met

import random
high_score = [10]

    
def game():
    attempts = 1
    ans = random.randint(1, 10)
    print("Welcome to the Number Guessing Game!\nThe high score is {}.\n".format(min(high_score)))
    while True:
        try:
            guess = int(input("Guess a number 1-10: "))
            if guess < 1 or guess > 10:
                attempts += 1
                print("Sorry, your guess is outside of the range, please try again: ")
                continue
            elif guess < ans:
                attempts += 1
                print("It's higher: ")
                continue
            elif guess > ans:
                attempts += 1
                print("It's lower: ")
                continue
            else:
                if attempts == 1:
                    tries = "try"
                else:
                    tries = "tries"
                print("\nThat is correct!!! You guessed it in {} {}!".format(attempts, tries))
                high_score.append(attempts)
                play_again = input("\nWould you like to play again?  Yes/No: ")
                if play_again.lower() == 'yes':
                    game()
                else:
                    print("\nThank you for playing!")
            break

        except ValueError:
            attempts += 1
            print("Please use integers (whole numbers)")


game()