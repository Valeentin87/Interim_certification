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
