def sq(numb1):
    return numb1 ** 2


def is_simple(numb2):
    help_numb = int(numb2 ** 0.5) + 1
    for el in range(2, help_numb):
        if not numb2 % el:
            return False
    return True


answ = list(filter(is_simple, range(51)))
print(list(map(sq, answ)))


