def greet(name):
    def add_greeting(func):
        def wrapper(*args, **kwargs):
            print(f"Hello {name}, this is your function:")
            return func(*args, **kwargs)

        return wrapper
    return add_greeting

@greet("Bogdan")
def add_three_numbers(a, b, c):
    print(f"the addition of {a}+{b}+{c}={a+b+c}")


@greet("Haj")
def add_two_numbers(a, b):
    print(f"the addition of {a}+{b}={a+b}")


add_three_numbers(4,5,6)
add_two_numbers(10, 7)
