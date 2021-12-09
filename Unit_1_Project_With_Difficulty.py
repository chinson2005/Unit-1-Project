import random
title_1 = "The Number Guessing Game"
title_2 = "Easy"
title_3 = "Medium"
title_4 = "Hard"
quit_msg = "Thank you for playing!"
high_score = []


def start():
    print()
    print("-" * len(title_1))
    print(title_1)
    print("-" * len(title_1))
    while True:
        try:
            attempts = 1
            print("\nPlease select your difficulty:\n")
            level = int(input("1) Easy\n2) Medium\n3) Hard\n4) Quit\n\nSelect 1-4: "))
            if level == 1:
                print()
                print("*" * len(title_2))
                print(title_2)
                print("*" * len(title_2))
                ans = random.randint(1, 10)
                while True:
                    try:
                        guess = int(input("\nGuess a number 1-10: "))
                        if guess < 1 or guess > 10:
                            print("\nYour guess is out of range, try again.")
                            attempts += 1
                            continue
                        elif guess < ans:
                            print("\nHigher!")
                            attempts += 1
                            continue
                        elif guess > ans:
                            print("\nLower!")
                            attempts += 1
                            continue
                        else:
                            if attempts == 1:
                                tries = "try"
                            else:
                                tries = "tries"
                            print(f"\nCorrect! You got it in {attempts} {tries}!")
                            high_score.append(attempts)
                            while True:
                                play_again = input("\nWould you like to play again? (Y/N) ")
                                if play_again.lower() == "y":
                                    print(f"\n----High Score: {(min(high_score))}----")
                                    start()
                                elif play_again.lower() == "n":
                                    print("\n" + f"{quit_msg}")
                                    print("-" * len(quit_msg))
                                    break
                                else:
                                    print("Invalid Choice")
                                    continue
                        break
                    except ValueError:
                        attempts += 1
                        print("\nUse numbers only!")
                break                 
            elif level == 2:
                print()
                print("*" * len(title_3))
                print(title_2)
                print("*" * len(title_3))
                ans = random.randint(1, 30)
                while True:
                    try:
                        guess = int(input("\nGuess a number 1-30: "))
                        if guess < 1 or guess > 30:
                            print("\nYour guess is out of range, try again.")
                            attempts += 1
                            continue
                        elif guess < ans:
                            print("\nHigher!")
                            attempts += 1
                            continue
                        elif guess > ans:
                            print("\nLower!")
                            attempts += 1
                            continue
                        else:
                            if attempts == 1:
                                tries = "try"
                            else:
                                tries = "tries"
                            print(f"\nCorrect! You got it in {attempts} {tries}!")
                            high_score.append(attempts)
                            while True:
                                play_again = input("\nWould you like to play again? (Y/N) ")
                                if play_again.lower() == "y":
                                    print(f"\n----High Score: {(min(high_score))}----")
                                    start()
                                elif play_again.lower() == "n":
                                    print("\n" + f"{quit_msg}")
                                    print("-" * len(quit_msg))
                                    break
                                else:
                                    print("Invalid Choice")
                                    continue
                        break
                    except ValueError:
                        attempts += 1
                        print("\nUse numbers only!")
                break                 
            elif level == 3:
                print()
                print("*" * len(title_4))
                print(title_4)
                print("*" * len(title_4))
                ans = random.randint(1, 100)
                while True:
                    try:
                        guess = int(input("\nGuess a number 1-100: "))
                        if guess < 1 or guess > 100:
                            print("\nYour guess is out of range, try again.")
                            attempts += 1
                            continue
                        elif guess < ans:
                            print("\nHigher!")
                            attempts += 1
                            continue
                        elif guess > ans:
                            print("\nLower!")
                            attempts += 1
                            continue
                        else:
                            if attempts == 1:
                                tries = "try"
                            else:
                                tries = "tries"
                            print(f"\nCorrect! You got it in {attempts} {tries}!")
                            high_score.append(attempts)
                            while True:
                                play_again = input("\nWould you like to play again? (Y/N) ")
                                if play_again.lower() == "y":
                                    print(f"\n----High Score: {(min(high_score))}----")
                                    start()
                                elif play_again.lower() == "n":
                                    print("\n" + f"{quit_msg}")
                                    print("-" * len(quit_msg))
                                    break
                                else:
                                    print("Invalid Choice")
                                    continue
                        break
                    except ValueError:
                        attempts += 1
                        print("\nUse numbers only!")
                break
            elif level == 4:
                print("\n" + f"{quit_msg}")
                print("-" * len(quit_msg))
                quit()            
            else: 
                print("\nInvalid Choice!")
        except ValueError:
            print("\nInvalid Choice!")
        print(quit_msg)


start()
