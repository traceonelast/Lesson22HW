# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self, is_desc=False):
        return sorted(self.lst, reverse=is_desc)


if __name__ == "__main__":
    some = SomeClass()
    print(some.sorted_func(False    ))