# в классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные,
# проверить значения атрибутов,
# вызвать методы экземпляров.


class Worker:
    income = {"wage": 250000, "bonus": 70000}
    name = 'Lisa'
    surname = "Grey"
    __position = 'CEO'


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


position = Position()
print(position.get_full_name())
print(position.get_total_income())
