import csv
from datetime import datetime

with open('Menu.txt', 'w') as f:
    f.write('* Please Choose a Pizza Base:\n1: Classic\n2: Margherita\n3: TurkPizza\n4: PlainPizza\n')
    f.write('* and sauce of your choice:\n11: Olives\n12: Mushrooms\n13: GoatCheese\n14: Meat\n15: Onions\n16: Corn\n')
    f.write('* Thank you!\n')


# Creating superclass "Pizza"
class Pizza:
    def get_description(self):
        pass

    def get_cost(self):
        pass


# Creating subclasses "ClassicPizza", "MargheritaPizza", "TurkPizza", and "PlainPizza"
class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 10.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 12.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turk Pizza"
        self.cost = 15.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class PlainPizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizza"
        self.cost = 20.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Creating superclass "Decorator"
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_description(self)

    def get_description(self):
        return self.component.get_description() + " " + Pizza.get_description(self)


# Creating subclasses "Olives", "Mushrooms", "GoatCheese", "Meat", "Onions", and "Corn"
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Olives"
        self.cost = 2.0


class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushrooms"
        self.cost = 3.0


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Goat Cheese"
        self.cost = 4.0


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat"
        self.cost = 5.0


class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onions"
        self.cost = 1.0


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn"
        self.cost = 1.5


# Creating a function to print the menu on the screen
def print_menu():
    with open('Menu.txt', 'r') as FILE:
        menu = FILE.read()
        print(menu)


if __name__ == '__main__':
    # Print the menu on the screen
    print_menu()
    # Let the user choose a pizza and sauce from the menu
    while True:
        try:
            pizza_choice = int(input("Please enter the number of the pizza you would like to order: "))
            if pizza_choice < 1 or pizza_choice > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please try again.")

    pizza = None
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = PlainPizza()
    else:
        print("Invalid choice.")
        exit()

    print("Please select a sauce:")
    print("11: Olives")
    print("12: Mushrooms")
    print("13: Goat Cheese")
    print("14: Meat")
    print("15: Onions")
    print("16: Corn")

    sauce_choice = input("Enter sauce choice: ")
    if sauce_choice == "11":
        pizza = Olives(pizza)
        print("Olives selected.")
    elif sauce_choice == "12":
        pizza = Mushrooms(pizza)
        print("Mushrooms selected.")
    elif sauce_choice == "13":
        pizza = GoatCheese(pizza)
        print("Goat Cheese selected.")
    elif sauce_choice == "14":
        pizza = Meat(pizza)
        print("Meat selected.")
    elif sauce_choice == "15":
        pizza = Onions(pizza)
        print("Onions selected.")
    elif sauce_choice == "16":
        pizza = Corn(pizza)
        print("Corn selected.")
    else:
        print("Invalid choice.")
        exit()

    print("\nYour order is:")
    print(pizza.get_description())
    print("Total cost: $" + str(pizza.get_cost()))

    name = input("Please enter your name: ")
    id_number = input("Please enter your ID number: ")
    credit_card_number = input("Please enter your credit card number: ")
    credit_card_password = input("Please enter your credit card password: ")
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Orders_Database.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([name, id_number, credit_card_number, credit_card_password,
                         pizza.get_description(), str(pizza.get_cost()), order_time])
