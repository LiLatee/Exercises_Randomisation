from random import randrange
import time
import os

# TODO: 1. Czy zrobione czy już było ?
# TODO: 2. FileNotFoundError
# TODO: 2. Powrót

def get_range(range: list) -> int:
    try:
        number1, number2 = input('Podaj dwie liczby odzielone (TYLKO) spacją (zakres zadań): ').split(' ')
        randrange(int(number1), int(number2) + 1, 1) # Helps to check if numbers are int type. Otherwise ValueError occurs.
    except ValueError:
        return 1
    range.append(number1)
    range.append(number2)
    return 0
def open_write( action: str, filename: str=None) -> str:
    """Opens existing file and saves data."""

    #if filename is None:
    # err = FileNotFoundError
    #
    # while err is FileNotFoundError:
    #     try:
    #         err = None
    #         filename = input('Podaj nazwe pliku do otwarcia: ')
    #
    #         set_of_elements = set()
    #         with open(filename, 'r') as data:
    #             number1, number2 = data.readline().split(' ')
    #             # Removes square brackets
    #             for element in data:
    #                 # Creates set with elements from a file, converts strings to int.
    #                 set_of_elements = set(map(int, (element.strip('{}\n')).split(', ')))
    #     except FileNotFoundError:
    #         err = FileNotFoundError


    try:
        if filename is None:
            filename = input('Podaj nazwe pliku do otwarcia: ')

        set_of_elements = set()
        with open(filename, 'r') as data:
            number1, number2 = data.readline().split(' ')
            # Removes square brackets
            for element in data:
                # Creates set with elements from a file, converts strings to int.
                set_of_elements = set(map(int, (element.strip('{}\n')).split(', ')))
    except FileNotFoundError:
        print('Plik nie istnieje!')
        time.sleep(2)
        return FileNotFoundError

    draw_number = randrange(int(number1), int(number2) + 1, 1)

    done_exercises = 0
    list_of_elements = []
    while len(set_of_elements) != (int(number2) - int(number1) + 1):
        if draw_number not in set_of_elements:
            os.system('cls')
            print('Wylosowano: ', draw_number)
            set_of_elements.add(draw_number)
            list_of_elements.append(draw_number)
            print('Zadanie numer: ', len(set_of_elements), '/', (int(number2)-int(number1) + 1), '.')
            done_exercises += 1
            print('Aktualnie robione zadanie: ', done_exercises, '.')
            print(list_of_elements) # Shows currently performed exercises during this session.
            action = input('Wciśnij cokolwiek, aby wylosowac kolejną liczbę lub Q, aby zakończyć: ')
        draw_number = randrange(int(number1), int(number2) + 1, 1)
        if action.upper() == 'Q':
            break

    with open(filename, 'w') as data:
        print(number1, number2, file=data, end='')
        print(set_of_elements, file=data, end='')

    if action.upper() == 'Q':
        print('Do zobaczenia! :)')
        return action
    else:
        print('Wszystkie zadania zostały zrobione! GRATULACJE! :)')
        return action
def create_write_file() -> str:
    """Creates files if doesn't exist and uses open_write() function."""
    name = input('Podaj nazwę nowego pliku: ')

    range = []
    while get_range(range):
        pass
    number1 = range[0]
    number2 = range[1]



    # Checks if range starts with smaller number.
    if number1 > number2:
        temp_number1 = number1
        number1 = number2
        number2 = temp_number1



    # Saves range in a file.
    with open(name, 'w') as data:
        print(number1, number2, file=data, end='\n')

    return open_write(action, name)


# Creates a folder for saves if doesn't exist.
newpath = r'saves'
if not os.path.exists(newpath):
    os.makedirs(newpath)
os.chdir(newpath)

action = input('Stworzyć nowy zakres (N), czy wczytać ostatni (O)? ')

while action.upper() != 'Q':
    if action.upper() == 'N':
        action = create_write_file()
    elif action.upper() == 'O':
        action = open_write(action)
    os.system('cls')
    action = input('Stworzyć nowy zakres (N), czy wczytać ostatni (O) lub Q aby wyjść: ')
