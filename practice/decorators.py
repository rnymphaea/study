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


def get_dict_words(func):

    def wrapper(*args):
        return dict(func(*args))

    return wrapper



@get_dict_words
def get_list_words(s1, s2):
    return zip(s1.split(), s2.split())




