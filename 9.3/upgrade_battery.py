"""类实例作为另一个类的属性"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a '+ str(self.battery_size) + '-kmh battery.')

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range =240
        elif self.battery_size ==85:
            range =270
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    

electriccar = ElectricCar('Lbjn', 'G350T', '1987')
electriccar.battery.get_range()
electriccar.battery.upgrade_battery()
electriccar.battery.get_range()

