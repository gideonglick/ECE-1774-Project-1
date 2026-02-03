from Circuit import Circuit
from bus import Bus
from Solution import Solution

circuit_obj = Circuit("SimpleCircuit")

circuit_obj.add_bus(Bus("A"))
circuit_obj.add_bus(Bus("B"))

circuit_obj.add_vsource_element(name="Vsource", bus1="BusA", v=100.0)
circuit_obj.add_resistor_element(name="Rab", bus1="A", bus2="B", r=5)
circuit_obj.add_load_element(name="Lb", bus1="B", p=2000.0, q=0.0)

solution_obj = Solution(circuit_obj)
solution_obj.do_power_flow()
circuit_obj.print_nodal_voltage()
circuit_obj.print_circuit_current()