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

class Computer(NetworkDevice):  
    def __init__(self, name, processor):
        super().__init__(name)  
        self.processor = processor  

    def process_data(self):
        print(f"Computer {self.name} is processing data.")

class HasScreen(Device):  
    def show_on_screen(self, text):
        print(f"Displayed on screen: {text}")

class Smartphone(NetworkDevice, HasScreen):  
    def __init__(self, name, processor):
        NetworkDevice.__init__(self, name)  
        HasScreen.__init__(self, name)  
        self.processor = processor

    def make_call(self, number):
        print(f"Calling number {number}.")


computer = Computer("MacBook Pro", "M1")
smartphone = Smartphone("iPhone 14", "A16 Bionic")

computer.turn_on()
computer.connect_to_network()
computer.process_data()

smartphone.turn_on()
smartphone.connect_to_network()
smartphone.show_on_screen("Incoming call")
smartphone.make_call("+380671234567")
