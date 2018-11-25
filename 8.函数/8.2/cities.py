# describe a city...
#函数形参指定默认值等号两边不要有空格
def describe_city(name='Beijing', country='China'):
    print(name + " is in " + country)

describe_city()
#函数调用参数赋值等号两边不要有空格
describe_city(name='Paris', country='France')
describe_city(name='Reykjavik', country='Iceland')