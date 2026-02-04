from Circuit import Circuit
from Solution import Solution

circuit_obj = Circuit("SimpleCircuit")

circuit_obj.add_bus("A")
circuit_obj.add_bus("B")

circuit_obj.add_vsource_element(name="Vsource", bus1_name="A", v=200.0)
circuit_obj.add_resistor_element(name="Rab", bus1_name="A", bus2_name="B", r=20.0)
circuit_obj.add_load_element(name="Lb", bus1_name="B", p=3000.0, q=0.0)

solution_obj = Solution(circuit_obj)
solution_obj.do_power_flow()

circuit_obj.print_nodal_voltage()
circuit_obj.print_circuit_current()