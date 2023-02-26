"""
{
01:{
      'id': 1, 
      'title': 'dada', 
      'discription': 'adsasda',       
      'data_r': '02.01.2020', 
      'execution': 'False'}

02:{
      'id': 1, 
      'title': 'dada', 
      'discription': 'adsasda',       
      'data_r': '02.01.2020', 
      'execution': 'False'}

}
"""
from colorama import Fore
import json
from datetime import datetime

dict_body = {}
cout_dict = 0

def add_note_json():
    with open('db.json', 'r') as json_data:
        my_data = json.load(json_data)
        cout_dict = len(my_data) + 1
        user_title = input('Ведите заголовок заметки: ')
        dict_body['title'] = user_title
        user_discription = input('Ведите описания заметки: ')
        dict_body['discription'] = user_discription
        user_data_note = input('Ведите дату для заметки в формате "дд.мм.гггг, ч.м"')
        dict_body['data_note'] = user_data_note
        dict_body['data_c'] = datetime.now().strftime('%d.%m.%y|%H:%M:%S')
        dict_body['data_r'] = datetime.now().strftime('%d.%m.%y|%H:%M:%S')
        dict_body['execution'] = False
        my_data[f'{cout_dict}'] = dict_body
    with open('db.json', 'w') as json_data_wried:
        json.dump(my_data, json_data_wried)


def read_all_note():
    with open('db.json', 'r') as r_json:
        data_json = json.load(r_json)
    for k, v in data_json.items():
       if v['execution']  == False:
           print(Fore.CYAN + f'Заметка: {k}\n'
                 f'Дата {v["data_note"]}\n'
                 f'Зоголовок {v["title"]}\n'
                 f'Описание {v["discription"]}')
           print('*'*40)
           print()

def change_note():
    chang_user = input(Fore.RED + 'Какую запись выхотите изменить:')
    with open('db.json', 'r') as json_data:
        my_data = json.load(json_data)
        user_title = input('Ведите заголовок заметки: ')
        dict_body['title'] = user_title
        user_discription = input('Ведите описания заметки: ')
        dict_body['discription'] = user_discription
        user_data_note = input('Ведите дату для заметки в формате "дд.мм.гггг, ч.м"')
        dict_body['data_note'] = user_data_note
        dict_body['data_c'] = my_data[f'{chang_user}']['data_c']
        dict_body['data_r'] = datetime.now().strftime('%d.%m.%y|%H:%M:%S')
        dict_body['execution'] = my_data[f'{chang_user}']['execution']
    my_data[f'{chang_user}'] = dict_body

    with open('db.json', 'w') as json_data_wried:
        json.dump(my_data, json_data_wried)
