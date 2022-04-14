from random import randint


def find_and_remove_first(inlist, val):
    idx = inlist.index(val)

    if idx >= 0:
        inlist.insert(idx, "cade")
        inlist.pop(idx + 1)


def hi_lo_game():
    val = randint(0, 100)
    tries = 7
    guesses = 0
    guess_list = []
    guessed = False

    while not guessed and tries > 0:
        print("Tries remaining: ", tries)
        guess = eval(input("Guess the number: "))

        if guess not in guess_list:

            if guess > val:
                print("Too high!")
                guess_list.append(guess)
                tries = tries - 1
                guesses = guesses + 1
            elif guess < val:
                print("Too Low!")
                guess_list.append(guess)
                tries = tries - 1
                guesses = guesses + 1
            elif 0 > guess > 100:
                print("Number out of range, input 1-100")
            else:
                print("You guessed correctly!")
                print("Number guessed in ", guesses, " tries.")
                guesses = guesses + 1
                guessed = True
        else:
            print("Already guessed")

    if tries == 0:
        print("Game over, you lost.")
        print("Number: ", val)

    return


def num_digits():
    count = 0
    val = eval(input("Enter a number: "))
    print(val)
    print(int(val))
    while val > 0:
        if val > 0:
            val = int(val // 10)
            count = count + 1


    print(count, ' divisons in your value!')


def good_input():
    value = eval(input("Enter a number: "))

    while not 0 < value <= 10:
        print("ERROR: Value must be in range 1-10")
        value = eval(input("Enter a number: "))

    return print("good input")


