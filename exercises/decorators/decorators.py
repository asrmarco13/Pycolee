def my_decorator(function):
    def print_hello_say_my_name(name):
        print('Hello')
        function(name)
        print('!')

    return print_hello_say_my_name


@my_decorator
def my_name(name):
    print(name)


my_name('Marco')
