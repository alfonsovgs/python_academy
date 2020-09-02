from machine import CoffeMachine
from machine_event import *
from machine_state import *

if __name__ == '__main__':
    machine = CoffeMachine(400, 540, 120, 9, 550)

    while not machine.is_exit:
        command = input('Write action (buy, fill, take, remaining, exit): \n')
        print('')

        state = machine.handle(MachineBaseEvent(command))

        if type(state) is MachineBuyingState:
            message = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n'
            value = input(message)

            if value == 'back':
                continue

            coffee = int(value)
            machine.handle(CoffeeSelectedEvent(coffee))
        elif type(state) is FillMachineState:
            water = int(
                input('Write how many ml of water do you want to add: \n'))
            milk = int(
                input('Write how many ml of milk do you want to add: \n'))
            coffee = int(
                input('Write how many grams of coffee beans do you want to add: \n'))
            cups = int(
                input('Write how many disposable cups of coffee do you want to add: \n'))
            machine.handle(MachineFilledEvent(water, milk, coffee, cups))
        elif type(state) is MachineExitState:
            machine.exit()

        print('')
