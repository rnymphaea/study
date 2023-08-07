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


def del_useless_dashes(func):
    def wrapper(*args):
        s = func(*args)
        while s.count('--'):
            s = s.replace('--', '-')
        return s

    return wrapper


@del_useless_dashes
def get_string_latinic(s):
    s = s.lower()
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    res = ''
    for i in s:
        if i in t:
            res += t[i]
        elif i in '<>?,. ][{}"':
            res += '-'
        else:
            res += i
    return res

# передача аргументов декораторам
def outer_decorator(start):
    def decorator(func):
        def inner(*args):
            return sum(func(*args)) + start
        return inner
    return decorator


@outer_decorator(start=5)
def get_list_nums(s):
    return list(map(int, s.split()))


def outer_tag(tag='h1'):
    def decorator(func):
        def inner(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return inner
    return decorator


@outer_tag(tag='div')
def to_lower(s):
    return s.lower()


def outer_chars(chars="!?"):
    def decorator(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            for char in chars:
                res = res.replace(char, '-')
            while res.count('--'):
                res = res.replace('--', '-')
            return res
        return inner
    return decorator


@outer_chars(chars='?!:;,. ')
def to_latinic(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    s = s.lower()
    res = ""
    for char in s:
        if char in t:
            res += t[char]
        else:
            res += char
    return res


s = input()
print(to_latinic(s))
