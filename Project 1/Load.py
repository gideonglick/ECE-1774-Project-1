from bus import Bus
class Load:
    def __init__(self, name:str, bus1:Bus, p:float, v:float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v

        self.r = v ** 2 / p

    def calc_g(self):
        self.g = 1/self.r

