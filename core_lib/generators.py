class CounterOne:

    def __init__(self, max_value):
        self.max_value = max_value
        self.cur_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_value >= self.max_value:
            raise StopIteration
        ret = self.cur_value
        self.cur_value += 1
        return ret


class CounterTwo:

    def __init__(self, max_value):
        self.max_value = max_value
        self.cur_value = 0

    def __iter__(self):
        for val in range(self.max_value):
            yield val


class CounterThree:

    def __init__(self, max_value):
        self.max_value = max_value
        self.cur_value = 0
        self.__gen = self.counter_generator()

    def counter_generator(self):
        for val in range(self.max_value):
            yield val

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__gen)


if __name__ == '__main__':
    c = CounterThree(10)
    for i in c:
        print(i)
