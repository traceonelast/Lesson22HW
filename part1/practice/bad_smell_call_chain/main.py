# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, room_number, city_pop):
        self.room_number = room_number
        self.ciy_pop = city_pop

    def get_person_room(self):
        return self.room_number

    def get_city_population(self):
        return self.ciy_pop


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

if __name__ == '__main__':
    person = Person(17, 999999)
    print(f"Room - {person.get_person_room()}")
    print(f"Person's City Population - {person.get_city_population()}")