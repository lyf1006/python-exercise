class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increment):
        self.number_served += increment



restaurant = Restaurant("supo", 'sichuan cuisine')
print(restaurant.number_served)
restaurant.number_served = 12
print(restaurant.number_served)
restaurant.set_number_served(6)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)