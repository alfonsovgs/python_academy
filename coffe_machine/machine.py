from machine_event import *
from machine_state import *


class CoffeMachine:
    def __init__(self, water_ml, milk_ml, coffee_grams, disposable_coups, money):
        self.water_ml = water_ml
        self.milk_ml = milk_ml
        self.coffee_grams = coffee_grams
        self.disposable_coups = disposable_coups
        self.money = money
        self.is_exit = False

    def handle(self, event):
        if event.command == 'buy':
            return MachineBuyingState()
        elif event.command == 'fill':
            return FillMachineState()
        elif event.command == 'take':
            self.take_money()
            return MachineBaseState()
        elif event.command == 'remaining':
            self.show_information()
            return MachineBaseState()
        elif event.command == 'exit':
            return MachineExitState()
        elif type(event) == CoffeeSelectedEvent:
            self.buy(event)
            return MachineBaseState()
        elif type(event) is MachineFilledEvent:
            self.fill(event)
            return MachineBaseState()
        else:
            return MachineBaseState()

    def show_information(self):
        print('The coofe machine has:')
        print('{} of water'.format(self.water_ml))
        print('{} of milk'.format(self.milk_ml))
        print('{} of coffe beans'.format(self.coffee_grams))
        print('{} of disposable cups'.format(self.disposable_coups))
        print('{} of money'.format(self.money))

    def buy(self, event: CoffeeSelectedEvent):
        print(f'selected: {event.coffee_selected}')
        if event.coffee_selected == 1:
            self.dispatch_coffee(250, 0, 16, 4)
        elif event.coffee_selected == 2:
            print('entró')
            self.dispatch_coffee(350, 75, 20, 7)
        elif event.coffee_selected == 3:
            self.dispatch_coffee(200, 100, 12, 6)

    def fill(self, event: MachineFilledEvent):
        self.water_ml = self.water_ml + event.water
        self.milk_ml = self.milk_ml + event.milk
        self.coffee_grams = self.coffee_grams + event.coffee
        self.disposable_coups = self.disposable_coups + event.cups

    def take_money(self):
        print('I gave you: ${}'.format(self.money))
        self.money = 0

    def dispatch_coffee(self, water_of_cup, milk_of_cup, coffe_beans_of_cup, coffee_price):
        water_ml_tmp = self.water_ml - water_of_cup
        milk_ml_tmp = self.milk_ml - milk_of_cup
        coffee_grams_tmp = self.coffee_grams - coffe_beans_of_cup
        disposable_coups_tmp = self.disposable_coups - 1
        money_tmp = self.money + coffee_price

        print(f'warer_tmp: {water_ml_tmp}')
        if water_ml_tmp <= 0:
            print('Sorry, not enough water!')
        else:
            self.water_ml = water_ml_tmp
            self.milk_ml = milk_ml_tmp
            self.coffee_grams = coffee_grams_tmp
            self.disposable_coups = disposable_coups_tmp
            self.money = money_tmp
            print('I have enough resources, making you a coffee!')

    def exit(self):
        self.is_exit = True
