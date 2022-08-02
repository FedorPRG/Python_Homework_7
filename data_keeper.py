#dir = {}

dir = {'Фамилия_1':'Имя_1, Телефон_1, Описание_1',
    'Фамилия_2':'Имя_2, Телефон_2, Описание_2',
    'Фамилия_3':'Имя_3, Телефон_3, Описание_3',
    'Фамилия_4':'Имя_4, Телефон_4, Описание_4',
    'Фамилия_5':'Имя_5, Телефон_5, Описание_5'}

def directory_add(name,family,number,coment):
    dir[family]=f'{name}, {number}, {coment}'

def search(family):
    for key, value in dir.items():
        if key==family:
            return print(key, value, sep=', ')
    else: print(f'Записи с фамилией {family} нет')

def delete(family):
    for key, value in list(dir.items()):
        if key==family:
            del dir[family]
            print('Фамилия удалена')
            break
    print(f'Записи с фамилией {family} нет')    