def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def first_element(a, b):
        return a
    return pair(first_element)


def cdr(pair):
    def last_element(a, b):
        return b
    return pair(last_element)


assert car(cons(3,4)) == 3
assert cdr(cons(3,4)) == 4
