"""Завдання 1.
Створити клас "Транспортний засіб" та його нащадків: класи Поїзд та Літак (можна більше за бажанням).
В батьківському класі має бути визначено мінімум 1 конструктор, 3 атрибути та 1 метод.
В класах-нащадках мають бути додані мінімум по 1му новому методу та мінімум по 1му новому атрибуту.
Оформлення програми має максимально враховувати усі кращі практики, що обговорювалися на попередніх лекціях."""


# умовне значення зменшення палива у транспортному засобі
FUEL_REDUCTION = 10
# умовне значенния збільшення швидкості
SPEED_INCREASE = 25
# мінімальне критичне значення висоти
HEIGHT_MIN = 1000


class Vehicle:
    def __init__(self, year, max_fuel, speed):
        self._year = year
        self.speed = speed
        self.max_fuel = max_fuel
        self.fuel = max_fuel
        self.position = 0

    def make_noise(self):
        raise NotImplemented

    def move(self):
        self.position += self.speed
        self.fuel -= FUEL_REDUCTION
        return f'{self.max_fuel, self.fuel}, Moving along the giving route'

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

    def get_station_stop_message(self):
        return f'City {self.station_name} Stop will be in a few minutes!'


class Airplane(Vehicle):
    def __init__(self, year, max_fuel, speed, height):
        super().__init__(year, max_fuel, speed)
        self.height = height

    def make_noise(self):
        return 'Viouuu'

    def get_catapult_massage(self):
        if self.height <= HEIGHT_MIN:
            return 'Pilot must catapult!!!'


class Car(Vehicle):
    def __init__(self, year, max_fuel, speed, model, color):
        super().__init__(year, max_fuel, speed)
        self.model = model
        self.color = color

    def make_noise(self):
        return 'Drrrrr'

    def increase_speed(self):
        self.speed += SPEED_INCREASE
        return self.speed

    def get_model_label(self):
        return f'Car model - {self.model}'


def vehicle_test():
    car = Car(2000, 100, 60, 'Nissan', 'blue')
    vehicle = Vehicle(2000, 600, 0)
    train = Train(2005, 400, 60, 'Odessa')
    airplane = Airplane(1997, 20, 400, 1000)

    print(car.make_noise())
    print(vehicle.move())
    print(car.move())
    print(car.get_model_label())
    print(car.increase_speed())
    print(train.get_station_stop_message())
    print(airplane.move())
    print(airplane.move())
    print(airplane.refueling())
    print(airplane.get_catapult_massage())
    print(train.make_noise())


if __name__ == '__main__':
    vehicle_test()
