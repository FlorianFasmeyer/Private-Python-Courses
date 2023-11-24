import time
import os
import keyboard
import random
import sys
from time import sleep
from threading import Timer
from inputimeout import inputimeout, TimeoutOccurred

# Introduction.
os.system('cls')
print("Welcome to Pan's labyrinth")
sleep(1.25)
print('You will be submitted to multiple tests')
sleep(1.25)
print('You may need to react in time to certain events')
sleep(1.25)
print('You may need to make difficult choices')
sleep(1.25)
print('You may just die ...')
sleep(1.25)
print('Good luck.')
sleep(1.25)

print('Enter your name, Adventurer:')
player_name = input()
os.system('cls')
print('Hello, ' + player_name)
print('How old are you ?')

player_age = input('>')
while not player_age.isnumeric():
    print('You must write your age in numbers only !')
    print('How old are you ?')
    player_age = input('>')

player_age = int(player_age)
if player_age <= 10:
    print("You're too young to enter the labyrinth, Go do your homework or something.")
    input()
    os.system('python helloplayer.py')
elif player_age >= 50:
    print("You're too old to enter the labyrinth, Go talk to your wife or something")
    input()
    os.system('python helloplayer.py')
else:
    print('You may enter the labyrinth, Be careful in there player')


# Intersection & Tests.
def intersection():
    os.system('cls')
    print('You enter a 3-way intersection')
    print('Where are you headed', player_name, '?')
    print('\t 1) Left')
    print('\t 2) Front')
    print('\t 3) Right')
    while True:
        inter_choice = input('>')
        if inter_choice in ['Left', 'Front', 'Right']:
            break

        print('Please enter one of the listed choices')

    if inter_choice == 'Left':
        os.system('cls')
        print('You enter the left path...')
        sleep(2)
        left_choice()
    elif inter_choice == 'Front':
        os.system('cls')
        print('You enter the front path...')
        sleep(2)
        front_choice()
    else:  # inter_choice == 'Right'.
        os.system('cls')
        print('You enter the right path...')
        sleep(2)
        right_choice()


def third_test():
    os.system('cls')
    print("Pago's mother has 3 sons, Pam, Pim, ...")
    print('\t 1) Pom')
    print('\t 2) Pem')
    print('\t 3) Pet')
    print('\t 4) Other')

    while True:
        choice_test3 = input('>')
        if choice_test3 in ['Pom','Pem','Pet','Other']:
            break

        print('Please enter one of the listed choices')

    if choice_test3 in ['Pom','Pem','Pet']:
        print('Wrong answer.')
        print("You are not ready yet.")
        sleep(2)
        print('Come back when you improved, Goodbye.')
        sleep(2)
        return False
    else:
        print('Well done', player_name, ', you may proceed...')
        sleep(3.5)
        return True


def left_choice():
    if not first_test(player_age):
        intersection()
        return

    if not second_test():
        intersection()
        return

    if not third_test():
        intersection()
        return


def front_choice():
    if not second_test():
        intersection()
        return

    if not first_test(player_age):
        intersection()
        return

    if not third_test():
        intersection()
        return


def right_choice():
    if not third_test():
        intersection()
        return

    if not second_test():
        intersection()
        return

    if not first_test(player_age):
        intersection()
        return


def first_test(player_age):
    os.system('cls')
    print('You enter a large circular room')
    sleep(1.5)
    print('There is a locked wooden chest in the middle')
    sleep(1.5)
    print('A dark liquid is leaking from it ...')
    sleep(2)
    print('Do you wish to break it open ?')
    print('\tPress [y] to open it')
    print('\tPress [n] to leave the room')
    is_error = True
    while True:
        letters = keyboard.read_key()
        if (letters != 'n') & (letters != 'y'):
            if is_error == True:
                print('Wrong key, press [y] or [n]!')
                is_error = False
            else:
                is_error = True
        else:
            break

    if letters == 'y':
        os.system('cls')
        print('You break the lock open...')
        sleep(2)
        print('A giant slime explodes out of the chest !')
        sleep(1.5)
        print('Fast ! You have to hit it so it can\'t form itself')
        print('')
        print('mash your [SPACE] key to kill it')

        monster_hits = 0
        hitcount = player_age / 2
        while True:
            keyboard.read_key()
            if keyboard.is_pressed('space'):
                monster_hits = monster_hits + 1
                print(random.randrange(1, 40) * ' ', 'Splusch !')

            if monster_hits >= hitcount:
                sleep(2)
                print('The slime dissolve itselfs into a goo puddle')
                sleep(2)
                print('You flee the room and continue your adventure...')
                sleep(5)
                break

        return True
    else:
        print('You take a step back and a trapdoor opens under your feet')
        sleep(2)
        print('Screaming in your fall, you get impaled by the metal pipes at the bottom')
        sleep(2)
        print('You bleed out and die, cold and alone ...')
        sleep(4)
        return False


def boulder_death():
    print('You got crushed by the boulder')
    sleep(2)
    print("Your children definitely won't recognize you...")
    sleep(2)
    print('Press [ENTER] to restart')


def second_test():
    os.system('cls')
    tilldeath = 5
    t = Timer(tilldeath, boulder_death)
    t.start()
    start_time = time.time()
    prompt = f"Careful ! a GIANT boulder comes rolling towards you, quick, DO SOMETHING !\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time < tilldeath:
        print("Well done,", player_name, "\nYou may continue ...")
        sleep(5)
        return True
    else:
        return False


intersection()

# Ending quizz
os.system('cls')
sleep(3)
print('You continue on your way and come to see an old lady blocking the path.')
sleep(3)
print("She's sat behind a desk with a wooden wall behind her limiting visibility")
sleep(3)
print('"I see somebody stumbled their way to the end of this structure..."')
print('"Unfortunately ..."')
sleep(3)
print('"I have one challenge for you, a simple one ..."')
sleep(2)
print('     "THE SUPER"')
sleep(1)
print('         "ULTRA TURBO"')
sleep(1)
print('                 "MEGA QUIZZ"')
sleep(1)
print('"It goes like this ..."')
os.system('cls')
sleep(2)
print('"Your wife and your mother are drowning."')
sleep(2)
print('"You can only save one of them ..."')
sleep(2)
print('Which one will it be',player_name,'?')
print('You have 10 seconds.')
print('\t 1) Wife')
print('\t 2) Mother')


def ending_quizz():
    while True:
        try:
            quizzchoice = inputimeout(prompt='>>', timeout=10)
            if quizzchoice == 'Mother':
                return False
                break
            elif quizzchoice == 'Wife':
                return False
                break
            else:
                print('You may only type [Wife] or [Mother]')
        except TimeoutOccurred:
            return True


if ending_quizz():
    os.system('cls')
    sleep(2)
    print('"Hm ..."')
    sleep(2)
    print('"Nothing to say uh ?"')
    sleep(2)
    print('"You may be wiser than i thought..."')
    sleep(2)
    print('"Some day you may find yourself in impossible situations"')
    sleep(3)
    print('"That\'s the whole point of this test, you need to be ready."')
    sleep(3)
    print('"If you go behind me you will die. But ! You can go this way."')
    print('She points to a covered hole in the ground')
    sleep(5)
    os.system('cls')
    sleep(2)
    print('You enter the hole to find yourself in front of the only thing you didn\'t expect ...')
    sleep(3)
    print('Redemption.')
    print('                 _..oo8\""\"Y8b.._')
    print('               .88888888o.    \"Yb.')
    print('             .d888P""Y8888b      \"b.')
    print('            o88888    88888)       \"b')
    print('           d888888b..d8888P         \'b')
    print('           88888888888888"           8')
    print('          (88DWB8888888P             8)')
    print('           8888888888P               8')
    print('           Y88888888P     ee        .P')
    print('            Y888888(     8888      oP')
    print('             \"Y88888b     ""     oP"')
    print('               "Y8888o._     _.oP"')
    print('                 `\""Y888boodP\""\'')
    print('You did very good,',player_name ,', good luck out there !')
    sys.exit("Thank you for playing !")
else:
    os.system('cls')
    sleep(2)
    print('Hmm ...')
    sleep(2)
    print('Who\'s to say whether you made the right choice or not,',player_name)
    sleep(2)
    print('You will eventually figure it out ...')
    sleep(2)
    print('"You can go through. Goodbye."')
    os.system('cls')
    print('You walk around the wall to find yourself in front of 10 hooded figures')
    sleep(3)
    print('Before you have time to question the situation you hear firecrackers pop off')
    sleep(3)
    print('You made it after all !')
    sleep(2)
    print('You feel an itch ...')
    sleep(2)
    print('You touch your chest, what is that ?')
    sleep(2)
    print('Blood ...?')
    sleep(5)
    os.system('cls')
    sleep(2)
    print('               .-.')
    print('             __| |__')
    print('            [__   __]')
    print('               | |')
    print('               | |')
    print('               | |')
    print("               '-'")
    print('You tried your best, good luck out there.')
    sys.exit("Thank you for playing !")
