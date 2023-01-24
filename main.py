##### hang man #####
import random

tries = 10
history = []
correct = []
my_word = []


# ////////////////////////////////////////////////////////////////////
def importaword():
    with open("words.txt") as words:
        words = words.read()
    words = words.split("\n")
    word = random.choice(words)
    new_word = list(word.lower())
    new_word = sorted(new_word)
    return word, new_word


# ////////////////////////////////////////////////////////////////////
def checker(new_litter, my_word, correct, tries, new_word):
    if new_litter in list(new_word):  #
        correct.append(new_litter)
        my_word.append(new_litter)
        my_word = sorted(my_word)
        if new_word.count(new_litter) >= 2:
            my_word.append(new_litter)
            my_word = sorted(my_word)
    hd(word, correct)
    sorted(my_word)
    return correct, my_word, tries


# ////////////////////////////////////////////////////////////////////
def hd(word, correct):
    s = ''
    for i in word:
        if i in correct:
            s += i
        else:
            s += '_'
    print(s)


# ////////////////////////////////////////////////////////////////////
def input_litter(tries, history, my_word, new_word):
    while (tries != 0 and my_word != new_word):
        new_ = input("Enter a litter : ").lower()
        try:
            new_litter = new_[0]
        except TypeError:
            new_litter = [" "]
        if new_litter in history:
            print("repeted litter dear ")
        elif new_litter in new_word:
            history.append(new_litter)
        else:
            history.append(new_litter)
            tries = tries - 1
            print(' wrong litter your tries = ', tries)
        return new_litter, history, tries


# ////////////////////////////////////////////////////////////////////

def printer(tries, new_word, my_word):
    if my_word == new_word:
        print("you did it \nyou are amazing \nYOU ARE A WINNER ^_^")
    if tries == 0:
        print("I'm sorry you are out of tries \nGAME OVER !!")


# ////////////////////////////////////////////////////////////////////
word, new_word = importaword()
while tries != 0 and my_word != new_word:
    hd(word, correct)
    new_litter, history, tries = input_litter(tries, history, my_word, new_word)
    correct, my_word, tries = checker(new_litter, my_word, correct, tries, new_word)
    printer(tries, new_word, my_word)
    print("\n")
    print(new_word)
    print(correct)
    print(history)
    print(my_word)
