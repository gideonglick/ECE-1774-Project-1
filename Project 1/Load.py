import pandas as pd

class Load:
    def __init__(self, name, bus1, p, v):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v

        self.r = v ** 2 / p

    def calc_g(self):
        self.g = 1/self.r

if __name__ == '__main__':
    load1 = Load("Load1", "B", 2000.0, 100.0)
    load1.calc_g()
    print(f"Load1 Resistance = {load1.r} Ohms")
    print(f"Load1 Conductance = {load1.g} Siemens")