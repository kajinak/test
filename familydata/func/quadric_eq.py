from django.shortcuts import render

def get_dis(a, b, c):
    discr = (b**2) - 4*(a*c)
    return discr


def get_eq_root(a, b, d, order = 1):
    if order == 1:
        x = ((b * (-1)) + d ** (1 / 2)) / 2 * a
    else:
        x = ((b * (-1)) - d ** (1 / 2)) / 2 * a
    return x


class Coefficient(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.error_message = None

    def is_valid(self):
        if not self.value:
            self.error_message = "коэффициент не определен"
            return False
        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_message = "коэффициент не целое число"
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_message = "коэффициент при а не может быть равен нулю"
            return False

        return  True

