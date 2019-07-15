def sum_method(arg1: int, arg2: int):
    return arg1 + arg2


def sum_method_args(*args: int) -> int:
    return sum(args)


arg1 = 10
arg2 = 20
result = sum_method(arg1, arg2)
print('Result by sum arg1 + arg2:')
print(result)
result_from_args = sum_method_args(arg1, arg2)
print('Result by invocation of sum method:')
print(result_from_args)
