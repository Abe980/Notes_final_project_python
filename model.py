import csv
import datetime
import os.path

path = 'notes.csv'

# Читаем файл с заметками
def read_file_notes():
    # прверяем существование файла, если его нет возвращаем пустой список
    if not os.path.exists(path): return []
    # читаем файл
    with open(path, 'r') as f_notes:
        list_notes = list(csv.reader(f_notes, delimiter=';'))

        # id переводим в инты, даты в объекты datetime
        for elem in list_notes:
            elem[0] = int(elem[0])
            elem[3] = datetime.datetime.strptime(elem[3], '%Y-%m-%d %H:%M:%S')

    # возвращаем список заметок
    return list_notes

# записываем заметки в файл
def write_file_notes(my_list):
    with open(path, 'w', newline='') as f_notes:
        writer = csv.writer(f_notes, delimiter = ';')
        writer.writerows(my_list)

# читаем файл с максимальным id
def read_max_id():
    # если файла не существует, возвращаем -1
    if not os.path.exists('max_id.txt'): return -1
    # читаем файл, возвращаем максимальный id
    with open('max_id.txt', 'r') as f:
        id = int(f.read())
    return id

# записываем максимальный id в файл
def write_max_id(id):
    with open('max_id.txt', 'w') as f:
        f.write(str(id))
        
