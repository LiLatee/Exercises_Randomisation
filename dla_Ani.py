from random import randrange
import os

#TODO: czy zrobione czy już było?

# Creates a folder for saves if doesn't exist.
newpath = r'saves'
if not os.path.exists(newpath):
    os.makedirs(newpath)
os.chdir(newpath)

action = input('Stworzyć nowy zakres (N), czy wczytać ostatni (O)? ')

while action.upper() != 'Q':
    if action.upper() == 'N':
        name = input('Podaj nazwe nowego pliku: ')
        number1, number2 = input('Podaj dwie liczby odzielone (TYLKO) przecinkiem (zakres zadań): ').split(',')

        # Check if range starts wity smaller number.
        if(int(number1)>int(number2)):
            tempNumber1 = number1
            number1 = number2
            number2 = tempNumber1

        set_of_elements = set()
        draw_number = randrange(int(number1), int(number2)+1, 1)
        
        while len(set_of_elements) != (int(number2)):
            if draw_number not in set_of_elements:
                os.system('cls')
                print('Wylosowano: ', draw_number)
                set_of_elements.add(draw_number)
                print('Aktualnie zrobiono ',len(set_of_elements),' zadań.')
                action = input('Wciśnij cokolwiek, aby wylosowac kolejną liczbę lub Q, aby zakończyć: ')
            draw_number = randrange(int(number1), int(number2)+1, 1)
            if action.upper() == 'Q':
                break

        # Saves data in a file (range and drawn numbers)
        with open(name,'w') as data:
            print(number1,number2, file=data)
            print(set_of_elements, file=data)

        if action.upper() == 'Q':
            print('Do zobaczenia! :)')
            break
        else:
            print('Wszystkie zadania zostały zrobione! GRATULACJE! :)')
            action = input('Stworzyć nowy zakres (N), czy wczytac ostatni (O)? ')

    elif action.upper() == 'O':
        name = input('Podaj nazwe pliku do otwarcia: ')
        set_of_elements = set()
        with open(name,'r') as data:
            number1, number2 = data.readline().split(' ')
            # Removes square brackets
            for element in data:
                # Creates set with elements from a file, converts strings to int.
                set_of_elements = set(map(int,(element.strip('{}\n')).split(', ')))

        draw_number = randrange(int(number1), int(number2)+1, 1)

        while len(set_of_elements) != (int(number2)):
                if draw_number not in set_of_elements:
                    os.system('cls')
                    print('Wylosowano: ', draw_number)
                    set_of_elements.add(draw_number)
                    print(set_of_elements)
                    print('Aktualnie zrobiono ',len(set_of_elements),' zadań.')
                    action = input('Wciśnij cokolwiek, aby wylosowac kolejną liczbę lub Q, aby zakończyć: ')
                draw_number = randrange(int(number1), int(number2)+1, 1)
                if action.upper() == 'Q':
                    break

        with open(name,'w') as data:
            print(number1,number2, file=data)
            print(set_of_elements, file=data)
        if action.upper() == 'Q':
            print('Do zobaczenia! :)')
        else:
            print('Wszystkie zadania zostały zrobione! GRATULACJE! :)')
            action = input('Stworzyć nowy zakres (N), czy wczytac ostatni (O)? ')
    else:
        action = input('Wciśnięto zły klawisz. Podaj N lub O (Q aby wyjść): ')

