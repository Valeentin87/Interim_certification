import model
import view

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
