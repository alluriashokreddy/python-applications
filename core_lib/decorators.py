def decorator_capitalize(target_func):
    def wrap_func(*args, **kwargs):
        print('Decorator function  capitalize')
        print(f'arg values are {args}')

        # Pre-processing
        args = list(args)
        for i, arg in enumerate(args):
            args[i] = arg.capitalize()
            a = 'hello'

        res = target_func(*args, **kwargs)

    return wrap_func

def decorator_sluggify(target_func):
    def wrap_func(*args, **kwargs):
        print('Decorator function  remove spaces')
        print(f'arg values are {args}')

        # Pre-processing
        args = list(args)
        for i, arg in enumerate(args):
            args[i] = arg.replace(" ", "-")

        res = target_func(*args, **kwargs)
    return wrap_func

@decorator_capitalize
@decorator_sluggify
def func(*args, **kwargs):
    print('Main function')
    print(f'args are {args}')


if __name__ == '__main__':
    func('new delhi', 'new york')