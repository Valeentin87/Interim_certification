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
