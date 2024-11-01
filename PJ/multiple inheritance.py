class Device:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"Device {self.name} is turned on.")

    def turn_off(self):
        print(f"Device {self.name} is turned off.")

class NetworkDevice(Device):
    def connect_to_network(self):
        print(f"Device {self.name} is connected to the network.")

class HasScreen:
    def show_on_screen(self, text):
        print(f"Displayed on screen: {text}")

class Computer(NetworkDevice, HasScreen):
    def __init__(self, name, processor):
        super().__init__(name)
        self.processor = processor

    def process_data(self):
        print(f"Computer {self.name} is processing data.")

class Smartphone(NetworkDevice, HasScreen):
    def __init__(self, name, processor):
        super().__init__(name)
        self.processor = processor

    def make_call(self, number):
        print(f"Calling number {number}.")

# Creating objects
computer = Computer("MacBook Pro", "M1")
smartphone = Smartphone("iPhone 16", "A16 Bionic")

computer.turn_on()
computer.connect_to_network()
computer.show_on_screen("Hello, world!")
computer.process_data()

smartphone.turn_on()
smartphone.connect_to_network()
smartphone.show_on_screen("Incoming call")
smartphone.make_call("+380671234567")
