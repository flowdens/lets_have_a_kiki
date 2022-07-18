
class Stationery:
    title = "Title"

    def draw(self):
        print("Запуск отрисовки")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашо")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


Pen().draw()
Pencil().draw()
Handle().draw()