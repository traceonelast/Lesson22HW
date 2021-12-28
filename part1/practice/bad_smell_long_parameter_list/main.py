# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self):
        pass
    def move(self,  direction):
        if direction == 'UP':
            self.field.set_unit(x=self.x_coord, y=self.y_coord + self.speed, unit=self)

        elif direction == 'DOWN':
            self.field.set_unit(x=self.x_coord, y=self.y_coord - self.speed, unit=self)

        elif direction == 'LEFT':
            self.field.set_unit(x=self.x_coord - self.speed, y=self.y_coord, unit=self)

        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x_coord + self.speed, y=self.y_coord, unit=self)

    def _calc_speed(self):
        if self.fly:
            self.speed *=1.5
        elif self.crawl:
            self.speed *=0.5
        else:
            raise ValueError('Быть такого не может')


