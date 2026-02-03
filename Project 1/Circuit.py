from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource


class Circuit:
    def __init__(self, name):
        self.name = name
        self.buses = {}
        self.resistors = {}
        self.loads = {}
        self.vsources = {}
        self.i = 0.0

    def add_bus(self, bus):
        self.buses[bus.name] = bus

    def add_resistor_element(self, name, bus1, bus2, r):
        resistor = Resistor(name, bus1, bus2, r)
        self.resistors[name] = resistor

    def add_load_element(self, name, bus1, p, q):
        load = Load(name, bus1, p, q)
        self.loads[name] = load

    def add_vsource_element(self, name, bus1, v):
        vsource = Vsource(name, bus1, v)
        self.vsources[name] = vsource
        if bus1 in self.buses:
            self.buses[bus1].set_bus_v(v)

    def set_i(self, i):
        self.i = i

    def print_nodal_voltage(self):
        print(f"\nNodal Voltages for Circuit: {self.name}")
        print("=" * 50)
        for bus_name, bus in self.buses.items():
            print(f"Bus {bus_name}: {bus.v:.2f} V")
        print("=" * 50)

    def print_circuit_current(self):
        print(f"\nCircuit Current for: {self.name}")
        print("=" * 50)
        print(f"Current: {self.i:.4f} A")
        print("=" * 50)


if __name__ == '__main__':
    circuit = Circuit("Simple DC Circuit")

    circuit.add_bus(Bus("A"))
    circuit.add_bus(Bus("B"))
    circuit.add_bus(Bus("Ground"))

    circuit.add_vsource_element("VS1", "A", 120.0)
    circuit.add_resistor_element("R_series", "A", "B", 5.0)
    circuit.add_resistor_element("R_load", "B", "Ground", 10.0)
    circuit.add_load_element("Load1", "B", 1000.0, 500.0)

    circuit.buses["B"].set_bus_v(80.0)
    circuit.buses["Ground"].set_bus_v(0.0)
    circuit.set_i(8.0)

    circuit.print_nodal_voltage()
    circuit.print_circuit_current()