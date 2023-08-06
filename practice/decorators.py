def show_menu(func):

    def inner(s):
        for i, j in enumerate(func(s), 1):
            print(f'{i}. {j}')

    return inner


@show_menu
def get_menu(s):
    return s.split()


def show_text(func):

    def wrapper(*args):
        print(f'Площадь прямоугольника: {func(*args)}')

    return wrapper


@show_text
def get_sq(width, height):
    return width * height


def sort_list(func):

    def wrapper(*args):
        return sorted(func(*args))

    return wrapper


@sort_list
def get_list(s):
    return list(map(int, s.split()))


