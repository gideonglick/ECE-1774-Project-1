from bus import Bus

class Vsource:
    def __init__(self, name:str, bus1:Bus, v:float):
        self.name = name
        self.bus1 = bus1
        self.v = v
