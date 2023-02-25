import model


def klick_menu(number):

    if number == 4:    # функционал добавления новой заметки при нажатии кнопки 4
        g = model.add_task()
        return g
