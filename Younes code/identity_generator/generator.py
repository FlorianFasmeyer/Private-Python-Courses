import time


import keyboard
import random
import sys


def __main__():
    print('IDENTITY GENERATOR V.1')
    print('')
    delay_print('Hello user, do you wish to generate a new random identity ?\n')
    delay_print('\tPress [ENTER] to generate\n')
    delay_print('\tPress [ESC] to quit\n')

    is_error = True

    while True:
        letters = keyboard.read_key()
        if (letters != 'enter') & (letters != 'esc'):
            if is_error:
                print('Wrong key, press [y] or [n]!')
                is_error = False
            else:
                is_error = True
        else:
            break

    if letters == 'enter':
        generate_file()
    else:
        print('QUITTING . . .')
        leave_program()

    delay_print('Do you wish to generate another one ?\n')
    delay_print('\tKeep pressing [ENTER] to generate new identities\n')
    delay_print('\tpress [ESC] to quit\n')
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
            generate_file()
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            leave_program()
        else:
            pass


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


def read_random_line(filename):
    with open(f'./lists/{filename}.txt') as f:
        lines = f.read().splitlines()

    return random.choice(lines)


def create_write_file(arg1, arg2, arg3, arg4, arg5, arg6):
    text = f'Name: {arg1}\nLast name: {arg2}\nBirthday: {arg3}\nAddress: {arg4}\nJob: {arg5}\nPhone number: {arg6}\n'
    with open(f'{arg1}.txt', 'w') as file:
        file.write(text)


def generate_file():
    name = read_random_line('name')
    lastname = read_random_line('lastname')
    print('Generating :', name, lastname)
    birthday = read_random_line('birthday')
    address = read_random_line('address')
    job = read_random_line('job')
    phone_number = read_random_line('phonenumber')
    create_write_file(name, lastname, birthday, address, job, phone_number)


def leave_program():
    sys.exit('LEAVING IDENTITY GENERATOR V.1')


__main__()
