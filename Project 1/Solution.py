class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):
        """
        Solves the circuit by calculating bus voltages and circuit current.
        Algorithm for simple DC circuit with voltage source, series resistor, and load.
        """
        # Get circuit elements
        buses = self.circuit.buses
        resistors = self.circuit.resistors
        loads = self.circuit.loads
        vsource = self.circuit.vsources

        # Find the voltage source and get voltage at bus A
        vsource = list(vsource.values())[0]
        V_a = vsource.v

        # Set bus A voltage from voltage source
        bus_a_name = vsource.bus1
        buses[bus_a_name].set_bus_v(V_a)

        # Get the series resistor (between A and B)
        series_resistor = None
        for resistor in resistors.values():
            if (resistor.bus1 == "A" and resistor.bus2 == "B") or \
                    (resistor.bus1 == "B" and resistor.bus2 == "A"):
                series_resistor = resistor
                break

        # Get the load at bus B
        load = list(loads.values())[0]

        # For constant impedance load: R_load = V_nominal^2 / P
        V_nominal = 100.0  # Nominal voltage for the load
        R_load = (V_nominal ** 2) / load.p
        G_load = 1.0 / R_load

        # Get series resistance
        R_series = series_resistor.r
        G_series = series_resistor.g

        # Total resistance in circuit
        R_total = R_series + R_load

        # Calculate current: I = V_a / R_total
        I = V_a / R_total

        # Calculate voltage at bus B: V_b = I * R_load
        V_b = I * R_load

        # Update bus B voltage
        buses["B"].set_bus_v(V_b)

        # Set circuit current
        self.circuit.set_i(I)


if __name__ == '__main__':
    from Circuit import Circuit
    from Bus import Bus
    from Resistor import Resistor
    from Load import Load
    from Vsource import Vsource

    # Create test circuit
    test_circuit = Circuit("Test Circuit")

    # Add buses
    test_circuit.add_bus(Bus("A"))
    test_circuit.add_bus(Bus("B"))

    # Add voltage source at bus A (100V)
    test_circuit.add_vsource_element("Va", "A", 100.0)

    # Add series resistor between A and B (5 Ohms)
    test_circuit.add_resistor_element("Rab", "A", "B", 5.0)

    # Add load at bus B (2000W, nominal voltage 100V)
    test_circuit.add_load_element("Lb", "B", 2000.0, 0.0)

    # Create solution and solve
    solution = Solution(test_circuit)
    solution.do_power_flow()

    # Display results
    print("\nCircuit Solution:")
    print("=" * 50)
    print(f"bus A voltage = {test_circuit.buses['A'].v} V")
    print(f"bus B voltage = {test_circuit.buses['B'].v} V")
    print(f"Circuit current = {test_circuit.i} A")
    print("=" * 50)