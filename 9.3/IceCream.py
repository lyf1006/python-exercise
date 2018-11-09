class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    #其他方法定义应包含参数self
    def describe_restaurant(self):
        print("The restaurant's name is :" + self.restaurant_name)
        print("The cuisine of this restaurant is :" + self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is opening.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'hami melon']

    def display(self):
        print("The falvors of iceCream are: ")
        for falvor in self.flavors:
            print(falvor)


icecream = IceCreamStand('supo', 'sichuan cuisine')
icecream.display()