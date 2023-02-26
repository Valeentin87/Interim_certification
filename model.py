import datetime

import view


# модуль для записи новой заметки
def add_task():
    data = ['id', 'Заголовок', 'Тело заметки', 'дата создания']
    task = ['', '', '', '']
    for i in range(4):
        task[i] = str(input(f'введите {data[i]} '))
    new_task = ';'.join(task)
    with open('note_book.txt', 'a', encoding='utf-8') as file:
        file.write('\n ' + new_task)
    return new_task


# модуль для распечатывания всей записной книжки
def print_all_task():
    with open('note_book.txt', 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
        print('\n---------------------------------------------------------------------------------')


# модуль для поиска заметки в записной книжке по её номеру
def find_task_id(task_id):
    with open('note_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            string_pars = line.split(sep=';')
            if str(task_id) == string_pars[0].strip():
                return line
        result = f'заметка под номером {task_id} в записной книжке не числится'
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
            return f'заметки, сделанные {day} {month} {year} года в записной книжке отсутствуют'
        return result_list


def all_task_list():
    all_task = []
    with open('note_book.txt', 'r', encoding="utf-8") as file:
        for line in file:
            all_task.append(line)
    return all_task


def delete_task(task_id):
        del_task = find_task_id(task_id)
        if del_task == f'заметка под номером {task_id} в записной книжке не числится':
            return del_task
        result_task_list = all_task_list().remove(del_task)
        with open('note_book.txt', 'w', encoding="utf-8") as file:
            for item in result_task_list:
                file.write(item+"\n")
        return f'Заметка под номером {task_id} успешно удалена'



