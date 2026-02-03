
class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):

        # Get circuit elements
        buses = self.circuit.buses
        resistors = self.circuit.resistors
        loads = self.circuit.loads
        vsource = self.circuit.vsource

        # Find the voltage source to get the voltage at bus A
        V_a = vsource.v

        # Set bus A voltage from voltage source
        bus_a_name = vsource.bus1
        buses[bus_a_name].set_bus_v(V_a)

        #series resistor between A and B
        series_resistor = None
        for resistor in resistors.values():
            if (resistor.bus1 == "A" and resistor.bus2 == "B") or \
                    (resistor.bus1 == "B" and resistor.bus2 == "A"):
                series_resistor = resistor
                break

        # Get the load at bus B
        load = list(loads.values())[0]

        # For constant impedance load
        V_nominal = 100.0
        R_load = (V_nominal ** 2) / load.p
        G_load = 1.0 / R_load

        #series resistance
        R_series = series_resistor.r
        G_series = series_resistor.g

        # Total resistance in circuit
        R_total = R_series + R_load

        # Calculate current
        I = V_a / R_total

        # Calculate voltage at bus B
        V_b = I * R_load

        # Update bus B voltage
        buses["B"].set_bus_v(V_b)

        # Set circuit current
        self.circuit.set_i(I)


if __name__ == '__main__':
    from Circuit import Circuit

    test_circuit = Circuit("Test Circuit")

    # Add buses
    test_circuit.add_bus(bus_A="A", bus_B="B")

    test_circuit.add_vsource_element("Va", "A", 100.0)

    test_circuit.add_resistor_element("Rab", "A", "B", 5.0)

    test_circuit.add_load_element("Lb", "B", 2000.0, 0.0)

    solution = Solution(test_circuit)
    solution.do_power_flow()

    # Display results
    print("\nSolution:")
    print("=" * 50)
    print(f"bus A voltage = {test_circuit.buses['A'].v} V")
    print(f"bus B voltage = {test_circuit.buses['B'].v} V")
    print(f"Circuit current = {test_circuit.i} A")