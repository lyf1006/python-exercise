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


# restaurant = Restaurant('supo', 'sichuan cuisine')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

restone = Restaurant('baoshifu', 'dessert')
resttwo = Restaurant('seven-eleven','all kinds')
restthree = Restaurant('xiapu', 'hotpot')
restone.describe_restaurant()
resttwo.describe_restaurant()
restthree.describe_restaurant()