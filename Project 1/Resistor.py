
from bus import Bus
class Resistor:

    def __init__(self, name:str, bus1:Bus, bus2:Bus, r:float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.calc_g()

    def calc_g(self):
        self.g = 1/self.r