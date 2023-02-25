import model


def klick_menu(number):
    if number == 4:  # функционал добавления новой заметки при нажатии кнопки 4
        g = model.add_task()
        return g
    elif number == 1:  # функционал распечатывания всей книжки при нажатии кнопки 1
        return model.print_all_task()
