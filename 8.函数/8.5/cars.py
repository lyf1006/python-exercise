def car_info(manufacturer, type, **other_info):
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['type'] = type
    for key, value in other_info.items():
        cars[key] = value
    return cars

#关键字形参调用时等号两边不要有空格
my_car = car_info('Lamborghini', '350GT', made_year='1965', max_speed='240km/h', swept_volume='3464cc')
print(my_car)