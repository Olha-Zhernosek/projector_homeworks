

'''Create a class Restaurant with properties name, cuisine, and
menu. The menu property should be a dictionary with keys being
the dish name and values being the price. Create a child class
FastFood that inherits from Restaurant and adds a property
drive_thru (a boolean indicating whether the restaurant has a
drive-thru or not) and a method called order which takes in the
dish name and quantity and returns the total cost of the order.
The method should also update the menu dictionary to subtract
the ordered quantity from the available quantity. If the dish
is not available or if the requested quantity is greater than
the available quantity, the method should return a message
indicating that the order cannot be fulfilled. Example of usage:
class Restaurant:

    # your code here
    pass

class FastFood(Restaurant):
    # your code here
    pass

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available'''


class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        self.drive_thru = drive_thru
        super().__init__(name, cuisine, menu)

    def order(self, dish_name, quantity):
        if dish_name in self.menu and quantity <= self.menu[dish_name]['quantity']:
            total_cost = self.menu[dish_name]['price'] * quantity
            self.menu[dish_name]['quantity'] -= quantity
            return total_cost
        elif dish_name not in self.menu:
            return "Dish not available"
        else:
            return "Requested quantity not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
