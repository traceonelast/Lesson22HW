

class Unit:

    def move(self, field, unit_coord_x, unit_coord_y, move_direction, is_flying, is_creeping, move_speed = 1):


        if is_flying and is_creeping:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flying:
            move_speed *= 1.2
            if move_direction == 'UP':
                new_y = unit_coord_y + move_speed
                new_x = unit_coord_x
            elif move_direction == 'DOWN':
                new_y = unit_coord_y - move_speed
                new_x = unit_coord_x
            elif move_direction == 'LEFT':
                new_y = unit_coord_y
                new_x = unit_coord_x - move_speed
            elif move_direction == 'RIGHT':
                new_y = unit_coord_y
                new_x = unit_coord_x + move_speed
        if is_creeping:
            move_speed *= 0.5
            if move_direction == 'UP':
                new_y = unit_coord_y + move_speed
                new_x = unit_coord_x
            elif move_direction == 'DOWN':
                new_y = unit_coord_y - move_speed
                new_x = unit_coord_x
            elif move_direction == 'LEFT':
                new_y = unit_coord_y
                new_x = unit_coord_x - move_speed
            elif move_direction == 'RIGHT':
                new_y = unit_coord_y
                new_x = unit_coord_x + move_speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
