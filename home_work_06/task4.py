class Car:
    speed = 50
    color = 'blue'
    name = 'Volkswagen'
    is_police = False

    def go(self):
        print("Car rides")

    def stop(self):
        print("Car stops")

    def turn(self, direction):
        print("Car turn in {}".format(direction))

    def show_speed(self):
        print("Current speed is {}".format(self.speed))


class WorkCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Speed is too fast for riding in town")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Speed is too fast for riding while work")


police = PoliceCar()
print(police.is_police)

town = TownCar()
town.show_speed()
town.speed = 70
town.show_speed()

work = WorkCar()
work.show_speed()
work.speed = 50
work.show_speed()
