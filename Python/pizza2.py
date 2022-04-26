from enum import Enum
import time

PizzaSauce = Enum('PizzaTopping', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'piña mortadela pepperoni pimenton lechuga totopos aguacate jalapeño')
STEP_DELAY = 3

class Pizza:
    def __init__(self, name):
        self.name = name
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

class HawaiiPizza:
    def __init__(self):
        self.pizza = Pizza('hawayana')
        self.baking_time = 5

    def add_sauce(self):
        print('Añadiendo la sala a su pizza...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)

    def add_topping(self):
        print('Añadiendo la piña y la mortadela...')
        self.pizza.topping.append([i for i in
                                   (PizzaTopping.piña, PizzaTopping.mortadela)])
        time.sleep(STEP_DELAY)
        print('Listo el topping (piña, mortadela)')

    def bake(self):
        print('Cocinando la pizza por {} segundos'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('La pizza esta lista')

class Pepperoni:
    def __init__(self):
        self.pizza = Pizza('pepperoni')
        self.baking_time = 7

    def add_sauce(self):
        print('Añadiendo la crema fraiche')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('Lista la salsa')

    def add_topping(self):
        print('Añadiendo los toppings (pepperoni, pimenton) a la pizza')
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.pepperoni, PizzaTopping.pimenton)])
        time.sleep(STEP_DELAY)
        print('Listo con el pepperoni')

    def bake(self):
        print('Cocinando la pizza por {} segundos'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('Su pizza esta lista')

class Vegetariana:
    def __init__(self):
        self.pizza = Pizza('vegetariana')
        self.baking_time = 2
    def add_sauce(self):
        print('Añadiendo la sala a su pizza...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
    def add_topping(self):
        print('Añadiendo los toppings (aguacate, lechuga, pimenton) a la pizza')
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.aguacate, PizzaTopping.lechuga, PizzaTopping.pimenton)])
        time.sleep(STEP_DELAY)
        print('Listo con los toppings')
    def bake(self):
        print('Cocinando la pizza por {} segundos'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('Su pizza esta lista')

class Mexicana:
    def __init__(self):
        self.pizza = Pizza('mexicana')
        self.baking_time = 2
    def add_sauce(self):
        print('Añadiendo la sala a su pizza...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
    def add_topping(self):
        print('Añadiendo los toppings (aguacate, jalapeños, pimenton, pepperoni, totopos) a la pizza')
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.aguacate, PizzaTopping.pepperoni, PizzaTopping.pimenton,
                                    PizzaTopping.jalapeño, PizzaTopping.totopos)])
        time.sleep(STEP_DELAY)
        print('Listo con los toppings')
    def bake(self):
        print('Cocinando la pizza por {} segundos'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('Su pizza esta lista')
        
class Waiter:
    def __init__(self):
        self.buider = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (
                             builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza

def validate_style(builders):
    try:
        pizza_style = input('¿Cual pizza quiere?, [h]Hawaii | [p]Pepperoni | [v]Vegetariana | [m]Mexicana =>  ')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Error , solo las pizzas mostradas son disponibles')
        return (False, None)
    return (True, builder)

def main():
    builders = dict(h=HawaiiPizza, p=Pepperoni, v=Vegetariana, m=Mexicana)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Disfrute su pizza {}!'.format(pizza))

if __name__ == '__main__':
    main()