import random


def writhing_word_on_screen(correct_letters_, chosen_word_, number_of_letters_):
    for i in range(number_of_letters_):
        if chosen_word_[i] in correct_letters_:
            print(chosen_word_[i], end='')
        else:
            print('-', end='')


def copy_of_secret_word(correct_letters_, chosen_word_, number_of_letters_):
    word = ''
    for i in range(number_of_letters_):
        if chosen_word_[i] in correct_letters_:
            word += chosen_word_[i]
        else:
            word += '-'
    return word


def check_winner(word_, chosen_word_):
    if word_ == chosen_word_:
        return True


def checking_letters(correct_letters_, chosen_word_, number_of_letters_):
    english_lowercase_letter = 'abcdefghijlmnopqrstuvxzywk'
    check = True
    while check:
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter\n')
            writhing_word_on_screen(correct_letters_, chosen_word_, number_of_letters_)
            print()
        elif letter not in english_lowercase_letter:
            print('Please enter a lowercase English letter\n')
            writhing_word_on_screen(correct_letters_, chosen_word_, number_of_letters_)
            print()
        if letter in english_lowercase_letter and len(letter) == 1:
            check = False
    return letter


def initial():
    words = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(words)
    number_of_letters = len(chosen_word)
    correct_letters = []
    wrong_letters = []
    lives = 8
    while lives > 0:
        word = copy_of_secret_word(correct_letters, chosen_word, number_of_letters)
        if check_winner(word, chosen_word):
            print(f'You guessed the word {word}!\nYou survived!')
            exit()
        writhing_word_on_screen(correct_letters, chosen_word, number_of_letters)
        print()
        letter = checking_letters(correct_letters, chosen_word, number_of_letters)
        if letter in correct_letters or letter in wrong_letters:
            print("You've already guessed this letter")
        elif letter in chosen_word:
            correct_letters.append(letter)
        else:
            lives -= 1
            wrong_letters.append(letter)
            print("That letter doesn't appear in the word")
    else:
        print('You lost!')


def main():
    print('H A N G M A N')
    while True:
        restart = input('Type "play" to play the game, "exit" to quit: ')
        if restart == 'play':
            initial()
        elif restart == 'exit':
            break
        else:
            continue


main()
