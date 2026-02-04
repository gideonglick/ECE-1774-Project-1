from Circuit import Circuit


class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):

        buses = self.circuit.buses
        resistors = self.circuit.resistors
        loads = self.circuit.loads
        vsource = list(self.circuit.vsource.values())[0]

        V_a = vsource.v
        bus_a_name = vsource.bus1.name
        buses[bus_a_name].set_bus_v(V_a)

        series_resistor = None
        for resistor in resistors.values():
            if (resistor.bus1.name == "A" and resistor.bus2.name == "B") or \
                    (resistor.bus1.name == "B" and resistor.bus2.name == "A"):
                series_resistor = resistor
                break

        # Get the load at bus B
        load = list(loads.values())[0]

        V_nominal = 100.0
        R_load = (V_nominal ** 2) / load.p
        G_load = 1.0 / R_load

        R_series = series_resistor.r
        G_series = series_resistor.g

        R_total = R_series + R_load

        I = V_a / R_total

        V_b = I * R_load

        buses["B"].set_bus_v(V_b)

        self.circuit.set_i(I)


if __name__ == '__main__':
    from Circuit import Circuit

    test_circuit = Circuit("Test Circuit")

    test_circuit.add_bus("A")
    test_circuit.add_bus("B")

    test_circuit.add_vsource_element("Va", "A", 100.0)
    test_circuit.add_resistor_element("Rab", "A", "B", 5.0)
    test_circuit.add_load_element("Lb", "B", 2000.0, 0.0)

    solution = Solution(test_circuit)
    solution.do_power_flow()

    print("\nSolution:")
    print("=" * 50)
    print(f"bus A voltage = {test_circuit.buses['A'].v} V")
    print(f"bus B voltage = {test_circuit.buses['B'].v} V")
    print(f"Circuit current = {test_circuit.i} A")