def show_menu(func):
    def inner(s):
        for i, j in enumerate(func(s), 1):
            print(f'{i}. {j}')
    return inner


@show_menu
def get_menu(s):
    return s.split()


get_menu('Главная Добавить Удалить Выйти')
