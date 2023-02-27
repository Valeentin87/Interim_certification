import datetime
import csv
import tabulate
import color_text
import view


# модуль для записи новой заметки
def add_task():
    data = ['id', 'Заголовок', 'Тело заметки', 'дата создания']
    task = ['', '', '', '']
    for i in range(4):
        task[i] = str(input(f'\t\t\t\033[34mвведите {data[i]} \033[0m'))
    with open('note_book.csv', 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=';', lineterminator="\r")
        file_writer.writerow(task)
    return f'\t\t\t\t\t\t\t\t\t\tУспешно добавлена заметка под номером {task[0]}'


# модуль для распечатывания всей записной книжки
def print_all_task():
    with open('note_book.csv', encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            print(row)
        print('\n---------------------------------------------------------------------------------')


# модуль для поиска заметки в записной книжке по её номеру
def find_task_id(task_id):
    with open('note_book.csv', encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            if str(task_id) == row[0].strip():
                return row
        result = f'\t\t\t\t\t\t\t\tзаметка под номером {task_id} в записной книжке не числится'
        return result


# модуль для фильтрации списка заметок интересующей дате

def find_task_date(day, month, year):
    result_list = []

    with open('note_book.csv', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:

            data_pars = row[3].strip().split(sep=" ")
            if (data_pars[0].strip() == day) and (data_pars[1].strip() == month) and (data_pars[2].strip() == year):
                result_list.append(row)
                with open(f'{day}_{month}_{year}_.txt', 'a', encoding='utf-8') as data:
                    data.write(';'.join(row)+"\n")
        if len(result_list) == 0:
            return f'\t\t\t\t\t\t\t\tзаметки, сделанные {day} {month} {year} года в записной книжке отсутствуют'
        return result_list


def all_task_list():
    all_task = []
    with open('note_book.csv', encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter=';')
        for row in file_reader:
            all_task.append(row)
    return all_task

def view_tasks_tabulate():
    tacks = all_task_list()
    tacks.insert(0,['Номер заметки','Заголовок','Содержание заметки','Дата создания(изменения)'])
    result = tabulate.tabulate(tacks)
    return result


# модуль для редактирования заметки по её номеру
def edit_task(task_id):
    edite_task = find_task_id(task_id)
    if edite_task == f'\t\t\t\t\t\t\t\tзаметка под номером {task_id} в записной книжке не числится':
        return edite_task
    all_tasks = all_task_list()

    for line in all_tasks:
        if line[0] == task_id:
            line[1] = input(f'\t\t\tПредыдущее значение заголовка: \033[31m{line[1]}\033[0m, введите новое значение: ')
            line[2] = input(f'\t\t\tПредыдущее тело заметки: \033[31m{line[2]}\033[0m, введите новое значение: ')
            line[3] = input(f'\t\t\tПредыдущее значение даты: \033[31m{line[3]}\033[0m, введите дату изменения: ')

    with open('note_book.csv', 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=';', lineterminator="\r")
        for task in all_tasks:
            file_writer.writerow(task)

    return f'\t\t\t\t\t\t\t\tЗаметка под номером {task_id} успешно отредактирована'

def delete_task(task_id):
    del_task = find_task_id(task_id)
    if del_task == f'\t\t\t\t\t\t\t\tзаметка под номером {task_id} в записной книжке не числится':
        return del_task
    all_tasks = all_task_list()
    tasks_result = []
    for line in all_tasks:
        if line[0] != task_id:
            tasks_result.append(line)
    with open('note_book.csv', 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=';', lineterminator="\r")
        for task in tasks_result:
            file_writer.writerow(task)
    return f'\t\t\t\t\t\t\t\tЗаметка под номером {task_id} успешно удалена'