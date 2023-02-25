import model
import view
import datetime

def klick_menu(number):
    if number == 4:  # функционал добавления новой заметки при нажатии кнопки 4
        g = model.add_task()
        return g
    elif number == 1:  # функционал распечатывания всей книжки при нажатии кнопки 1
        return model.print_all_task()
    elif number == 2:  # функционал поиска заметки по её номеру
        number_id = input("Введите номер заметки, которую необходимо найти в записной книжке")
        answer = model.find_task_id(number_id)
        return view.output(answer)
    elif number == 3:  # функционал фильтрации записной книжки по дате
        find_day = input("Введите число месяца: ")
        find_month = input("Введите месяц: ")
        find_year = input("Введите год: ")
        result = model.find_task_date(find_day, find_month, find_year)
        dtn = str(datetime.datetime.now())
        with open(f'{find_day}_{find_month}_{find_year}_.txt', 'a', encoding='utf-8') as data:
            data.write("\n" + " список заметок на указанную дату отображен " + f'{dtn}' + "\n")
        return view.output(result)
