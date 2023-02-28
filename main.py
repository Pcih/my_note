"""
Это основной модуль в котором реализованно меню интерфейса и связь с другими модулями.
"""

from colorama import Fore
from JSON_DATA import json_write

def menu():
    print(Fore.RED + 'Меню:')
    print(Fore.YELLOW +  ' 1. Добавить заметку.')
    print(Fore.YELLOW +  ' 2. Вывести весь список.')
    print(Fore.YELLOW +  ' 3. Редактировать заметку.')
    print(Fore.YELLOW +  ' 4. Удалить заметку.')
    print(Fore.YELLOW +  ' 5. Покозать историю.')
    print(Fore.YELLOW +  ' 6. Покозать событие на дату.')
    print(Fore.MAGENTA +  'Что бы выйти нажмите "Enter"')

def main():
    try:
        while True:
            menu()
            user_choice = int(input(Fore.BLUE + 'Выберете вариант: '))
            if user_choice == 1:
                json_write.add_note_json()
            elif user_choice == 2: 
                json_write.read_all_note()
            elif user_choice == 3:
                json_write.change_note()
            elif user_choice == 4:
                json_write.delete_note()
            elif user_choice == 5:
                json_write.history_all_note()
            elif user_choice == 6:
                json_write.view_data()
    except ValueError:
        print('Спасибо! Ждем Вас сново.')
    


if __name__ == "__main__":
    main()