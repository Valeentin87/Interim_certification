import datetime
import csv
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

    new_task = ';'.join(task)
    with open('note_book.txt', 'a', encoding='utf-8') as file:
        file.write(new_task + "\n")

    return new_task


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
        result = f'\t\t\t\033[31mзаметка под номером {task_id} в записной книжке не числится\033[31m'
        return result


# модуль для фильтрации списка заметок интересующей дате

def find_task_date(day, month, year):
    result_list = []

    with open('note_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            string_pars = line.split(sep=';')
            data_pars = string_pars[3].strip().split(sep=" ")
            if (data_pars[0].strip() == day) and (data_pars[1].strip() == month) and (data_pars[2].strip() == year):
                result_list.append(line)
                with open(f'{day}_{month}_{year}_.txt', 'a', encoding='utf-8') as data:
                    data.write(line + "\n")
        if len(result_list) == 0:
            return f'\t\t\t\033[31mзаметки, сделанные {day} {month} {year} года в записной книжке отсутствуют\033[0m'
        return result_list


def all_task_list():
    all_task = []
    with open('note_book.txt', 'r', encoding="utf-8") as file:
        for line in file:
            all_task.append(line.strip("\n"))
    return all_task


# модуль для удаления заметки по её номеру
def edit_task(task_id):
    edite_task = find_task_id(task_id)
    if edite_task == f'\t\t\tзаметка под номером {task_id} в записной книжке не числится':
        return edite_task
    new_task = edite_task
    new_task_pars = new_task.split(';')
    new_task_pars[1] = input(f'\t\t\tПредыдущее значение заголовка: {new_task_pars[1]}, введите новое значение: ')
    new_task_pars[2] = input(f'\t\t\tПредыдущее тело заметки: {new_task_pars[2]}, введите новое значение: ')
    new_task_pars[3] = input(f'\t\t\tПредыдущее значение даты: {new_task_pars[3]}, введите дату изменения: ')
    new_task = ';'.join(new_task_pars)
    result_task_list = list(set(all_task_list()) - {edite_task})
    result_task_list.append(new_task)
    with open('note_book.txt', 'w', encoding="utf-8") as file:
        for item in result_task_list:
            file.write(item + "\n")
    return f'\t\t\tЗаметка под номером {task_id} успешно отредактирована'

def delete_task(task_id):
    del_task = find_task_id(task_id)
    if del_task == f'\t\t\tзаметка под номером {task_id} в записной книжке не числится':
        return del_task

    result_task_list = list(set(all_task_list()) - {del_task})
    with open('note_book.txt', 'w', encoding="utf-8") as file:
        for item in result_task_list:
            file.write(item + "\n")
    return f'\t\t\tЗаметка под номером {task_id} успешно удалена'