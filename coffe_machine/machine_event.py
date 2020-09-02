class MachineBaseEvent:
    def __init__(self, command):
        self.command = command

    def __str__(self):
        return self.command


class CoffeeSelectedEvent(MachineBaseEvent):
    def __init__(self, coffe_selected):
        super().__init__('')
        self.coffee_selected = coffe_selected


class MachineFilledEvent(MachineBaseEvent):
    def __init__(self, water, milk, coffee, cups):
        super().__init__('')
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
