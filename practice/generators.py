gen = (x ** 2 for x in range(1, 10) if x % 2 == 0)

a = set(gen) # {16, 64, 4, 36}
v = set(gen) # set()

# Генераторы позволяют использовать больше памяти.
# Пример: lst = [x for x in range(10**29)] -> MemoryError. lst = (x for x in range(10**29)) -> нет ошибки.

