def sum_method(arg1: int, arg2: int):
    print(arg1 + arg2)

def sum_method_args(*args: int) -> int:
    return sum(args)


arg1 = 10
arg2 = 20
#sum_method(arg1, arg2)
sum_return = sum_method_args(arg1, arg2)
print(sum_return)