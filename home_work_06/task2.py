
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, road_length, wid):
        self._length = road_length
        self._width = wid

    def calc_mass(self):
        return (self._width * self._length * 25 * 5) / 1000


road = Road(5000, 20)
print('To build a road we need {} ton(s)'.format(road.calc_mass()))

