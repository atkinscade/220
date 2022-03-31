from random import *


def get_words(file_name):
    with open(file_name, 'r') as f:
        lines = f.read()
        words = lines.split()
        return words


def get_random_word(words):
    count = randint(0, len(words))
    return words[count]


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guessed):
    if letter in guessed:
        return True
    else:
        return False


def make_hidden_secret(guessed, secret_word):
    word_collect = []
    for _ in secret_word:
        if _ not in guessed:
            word_collect.append('_')
        else:
            word_collect.append(_)
    guesser = ' '.join(word_collect)
    return guesser


def won(guesser):
    for letter in guesser:
        if '_' not in guesser:
            return True
        else:
            return False


def play_command_line(file):
    words = get_words(file)
    secret_word = get_random_word(words)
    correct_guess = False
    guessed_letters = []
    tries = 6
    print('_ ' * len(secret_word))
    while not correct_guess and tries > 0:
        print('Guesses: ', guessed_letters)
        print('Tries remaining: ', tries)
        guess = input("Guess a letter: ")
        if already_guessed(guess, guessed_letters):
            print('Letter already guessed.')
        else:
            if letter_in_secret_word(guess, secret_word):
                guessed_letters.append(guess)
                print(make_hidden_secret(guessed_letters, secret_word))
                if won(make_hidden_secret(guessed_letters, secret_word)):
                    print("You've Won!")
                    correct_guess = True
            else:
                guessed_letters.append(guess)
                print(make_hidden_secret(guessed_letters, secret_word))
                tries = tries - 1
    if tries == 0:
        print("L")
    else:
        pass
    return

play_command_line('words.txt')

def play_graphics(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
