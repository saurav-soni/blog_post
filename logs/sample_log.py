import logging

logging.basicConfig(filename='log_sample', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x // y
    except ZeroDivisionError:
        return 'division by 0 error'


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logging.debug(f"{num_1} + {num_2} = {add_result}")

sub_result = sub(num_1, num_2)
logging.debug(f"{num_1} - {num_2} = {sub_result}")

mul_result = mul(num_1, num_2)
logging.debug(f"{num_1} * {num_2} = {mul_result}")

div_result = div(num_1, num_2)
logging.debug(f"{num_1} / {num_2} = {div_result}")
