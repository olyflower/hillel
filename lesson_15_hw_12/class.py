"""Завдання 1.
Створити клас "Транспортний засіб" та його нащадків: класи Поїзд та Літак (можна більше за бажанням).
В батьківському класі має бути визначено мінімум 1 конструктор, 3 атрибути та 1 метод.
В класах-нащадках мають бути додані мінімум по 1му новому методу та мінімум по 1му новому атрибуту.
Оформлення програми має максимально враховувати усі кращі практики, що обговорювалися на попередніх лекціях."""


class Vehicle:
    def __init__(self, year, max_fuel, speed):
        self.year = year
        self.speed = speed
        self.max_fuel = max_fuel
        self.fuel = max_fuel
        self.position = 0

    def move(self):
        self.position += self.speed
        self.fuel -= 10
        return f'{self.max_fuel, self.fuel}, Moving along the giving route'

    def get_year(self):
        return self.year

    def refueling(self):
        if self.fuel <= 0.1 * self.max_fuel:
            self.fuel = self.max_fuel
            return 'Fueled!'


class Train(Vehicle):
    def __init__(self, year, max_fuel, speed, station_name):
        super().__init__(year, max_fuel, speed)
        self.station_name = station_name

    def make_noise(self):
        return 'To-tooooo.....'

    def station_stop(self):
        return f'City {self.station_name} Stop will be in a few minutes!'


class Airplane(Vehicle):
    def __init__(self, year, max_fuel, speed, height):
        super().__init__(year, max_fuel, speed)
        self.height = height

    def make_noise(self):
        return 'Viouuu'

    def catapult(self):
        if self.height <= 1000:
            return 'Pilot must catapult!!!'


class Car(Vehicle):
    def __init__(self, year, max_fuel, speed, model, color):
        super().__init__(year, max_fuel, speed)
        self.model = model
        self.color = color

    def make_noise(self):
        return 'Drrrrr'

    def increase_speed(self):
        self.speed += 25
        return f'Speed - {self.speed}'

    def get_model_car(self):
        return f'Car model - {self.model}'


car = Car(2000, 100, 60, 'Nissan', 'blue')
vehicle = Vehicle(2000, 600, 0)
train = Train(2005, 400, 60, 'Odessa')
airplane = Airplane(1997, 20, 400, 1000)

print(car.make_noise())
print(vehicle.move())
print(car.move())
print(car.get_model_car())
print(car.increase_speed())
print(train.station_stop())
print(airplane.move())
print(airplane.move())
print(airplane.refueling())
print(vehicle.get_year())
print(airplane.catapult())
print(train.make_noise())
