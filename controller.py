import view
import model
import datetime

# выводит список заметок
def view_notes(my_list):
    print()
    if my_list:
        print('id' + '\t' + 'name')
        for row in my_list:
            for i in row:
                print(i, end='\t')
            print()
    else:
        print('Список пустой')

# добавляет заметку, сортирует по дате и времени
def add_note(my_list, id):
    name = input('Введите название: ')
    description = input('Введите описание: ')
    my_list.append([id+1, name, description, datetime.datetime.now().replace(microsecond=0)])
    my_list.sort(key=lambda x:x[3], reverse=True)

# редактирует заметку
def edit_note(my_list):
    correct_input = True
    # ввод id заметки для редактирования с проверкой на существование
    while True:
        id = input('Введите id заметки или "q" для отмены: ')
        if id in [str(e[0]) for e in my_list]:
            break
        elif id == 'q':
            correct_input = False
            break
        else:
            print('Указанного id не существует!')
    
    # меню выбора, что редактировать
    while correct_input:
        edit_field = input('''
        Что будете редактировать:
                1. Название
                2. Описание
                3. Оба поля
                4. Отмена
        ''')
        if correct_input in range(1, 5): correct_input = False
    
    for elem in my_list:
        if elem[0] == int(id):
            if edit_field == '1':
                new_name = input('Введите новое название: ')
                elem[1] = new_name
                elem[3] = datetime.datetime.now().replace(microsecond=0)
                my_list.sort(key=lambda x:x[3], reverse=True)
            elif edit_field == '2':
                new_description = input('Введите новое описание:')
                elem[2] = new_description
                elem[3] = datetime.datetime.now().replace(microsecond=0)
                my_list.sort(key=lambda x:x[3], reverse=True)
            elif edit_field == '3':
                new_name = input('Введите новое название:')
                elem[1] = new_name
                new_description = input('Введите новое описание:')
                elem[2] = new_description
                elem[3] = datetime.datetime.now().replace(microsecond=0)
                my_list.sort(key=lambda x:x[3], reverse=True)
            elif edit_field == '4':
                break
            else:
                print('Некорректный выбор')

    

# удаление заметки
def del_note(my_list):
    correct_input = True
    # ввод id заметки для удаления с проверкой на существование
    while True:
        id = input('Введите id заметки для удаления или "q" для отмены: ')
        if id in [str(e[0]) for e in my_list]:
            break
        elif id == 'q':
            correct_input = False
            break
        else:
            print('Указанного id не существует!')

    if correct_input:
        # в цикле доходим до нужной заметки, удаляем ее, завершаем цикл
        for i in range(len(my_list)):
            if id == str(my_list[i][0]):
                del_elem = my_list.pop(i)
                print(f'Заметка {del_elem[1]} с id {del_elem[0]} удалена')
                break

# вывод заметки по id
def find_id(my_list):
    correct_input = True
    # ввод id заметки с проверкой на существование
    while True:
        id = input('Введите id заметки для просмотра или "q" для отмены: ')
        if id in [str(e[0]) for e in my_list]:
            break
        elif id == 'q':
            correct_input = False
            break
        else:
            print('Указанного id не существует!')
        
    if correct_input:
        for elem in my_list:
            if str(elem[0]) == id:
                for i in elem:
                    print(i, end='\t')
                print() 

# возвращает список заметок с заданной датой
def find_date(my_list):
    # ввод даты с проверкой на корректность
    while True:
        date = input('Введите дату создания или последнего изменения в формате ГГГГ-ММ-ДД: ')
        try:
            datetime.date.fromisoformat(date)
            break
        except:
            print('Не корректная дата')

    return [x for x in my_list if date == str(x[3]).split(' ')[0]]
    

# старт программы
def start():

    # получаем список заметок
    list_notes = model.read_file_notes()
    # получаем максимальный id? bp rjulf kb,j ceotcndjdfdib[]
    max_id = model.read_max_id()
    correct_input = True

    if max_id == -1:
        print('Ошибка чтения ID, если продолжите, ID новых заметок могут совпасть с удаленными')
        cont_err = input('Продолжить? (y/n)')
        if cont_err == 'y':
            max_id = max([el[0] for el in list_notes])
        else:
            correct_input = False
            print('Работа программы завершена')

    while correct_input:
        user_input = view.get_main_menu()

        if user_input == '1':
            view_notes(list_notes)
        elif user_input == '2':
            add_note(list_notes, max_id)
            max_id += 1
        elif user_input == '3':
            edit_note(list_notes)
        elif user_input == '4':
            del_note(list_notes)
        elif user_input == '5':
            find_id(list_notes)
        elif user_input == '6':
            view_notes(find_date(list_notes))
        elif user_input == '0':
            model.write_file_notes(list_notes)
            model.write_max_id(max_id)
            break
        else:
            print('Не корректный ввод!')

    
