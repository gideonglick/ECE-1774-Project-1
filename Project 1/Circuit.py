
from typing import Dict, List, Optional
from bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource


class Circuit:
    def __init__(self, name:str):
        self.name = name
        self.buses: Dict[str, Bus] = {}
        self.resistors: Dict[str, Resistor] = {}
        self.loads: Dict[str, Load] = {}
        self.vsource: Dict[str, Vsource] = {}
        self.i = float

    def add_bus(self, name:str):
        if name in self.buses:
            raise ValueError(f"Bus {name} already exists")
        self.buses[name] = Bus(name)


    def add_resistor_element(self, name:str, bus1_name:str, bus2_name:str, r:float):
        try:
            bus1 = self.buses[bus1_name]
            bus2 = self.buses[bus2_name]
        except KeyError as e:
            raise ValueError(f"Bus {e.args[0]} does not exist")
        self.resistors[name] = Resistor(name, bus1, bus2, r)

    def add_load_element(self, name, bus1, p, q):
        load = Load(name, bus1, p, q)
        self.loads[name] = load

    def add_vsource_element(self, name, bus1, v):
        vsource = Vsource(name, bus1, v)
        self.vsource = vsource
        if bus1 in self.buses:
            self.buses[bus1].set_bus_v(v)

    def set_i(self, i):
        self.i = i

    def print_nodal_voltage(self):
        print(f"\nNodal Voltages for Circuit: {self.name}")
        for bus_name, bus in self.buses.items():
            print(f"Bus {bus_name}: {bus.v:.2f} V")


    def print_circuit_current(self):
        print(f"\nCircuit Current for: {self.name}")
        print(f"Current: {self.i:.4f} A")