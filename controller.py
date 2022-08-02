import data_keeper 
import input_data
import output_data

def start():
    i=1
    while i==1:
        print('Вы находитесь в телефонном справочнике.\n\
    Введите номер команды:\n\
    1.Показать весь справочник (запись в файл)\n\
    2.Поиск номера телефона по фамилии\n\
    3.Добавить контакт\n\
    4.Удалить контакт')
        com=input_data.get_com()
        if com==1:
            stroka=''
            format=input_data.output_format()
            if format==1:                
                for key, value in data_keeper.dir.items():
                    stroka=stroka+str(key)+', '+str(value)+'\n'
                    print(key, value, sep=', ')
                    output_data.print(stroka)
            else:
                for key, value in data_keeper.dir.items():
                    print(key)
                    stroka=stroka+key+'\n'
                    for i in value:
                        if i==',':
                            print('')
                            stroka=stroka+'\n'
                        elif i==' ':
                            continue
                        else:
                            print(i,end='')
                            stroka=stroka+i
                    print('\n')
                    stroka=stroka+'\n'+'\n'
                output_data.print(stroka)
        if com==2:
            family=input_data.for_search()
            data_keeper.search(family)        
        if com==3:
            family, name, number, coment = input_data.new_data()
            data_keeper.directory_add(family, name, number, coment)
        if com==4:
            family=input_data.for_delete()
            data_keeper.delete(family)
        i=int(input('Желаете продолжить? (1-да, 2-нет)'))
