
def type_logger(func):
    def wrapper(*args):
        # calc = func(*args)
        func_args = [f"{el}: {type(el)}" for el in args]
        return func_args
    return wrapper

@type_logger
def calc_cube(*args):
   return x ** 3
a = calc_cube(1,23,3)
print(a)