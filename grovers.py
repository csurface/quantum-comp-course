from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt
import sys

# Grover's search algorithm

# Oracle circuit - winning state 11 (hence the cz)
oracle_circuit = QuantumCircuit(2, name="Oracle")
oracle_circuit.cz(0,1)
oracle_circuit.to_gate()

# Reflection circuit
reflection_circuit = QuantumCircuit(2,name="Reflection")
reflection_circuit.h([0,1])
reflection_circuit.z([0,1])
reflection_circuit.cz(0,1)
reflection_circuit.h([0,1])
reflection_circuit.to_gate()

# Main circuit
c = QuantumCircuit(2,2)
c.h([0,1])
c.append(oracle_circuit,[0,1])
c.append(reflection_circuit,[0,1])

c.measure([0,1],[0,1])

c.draw(output='mpl', style='iqp')
plt.show()

# Use the local simulator
sim = Aer.get_backend('qasm_simulator')
result = execute(c,backend=sim).result()
counts = result.get_counts()

#plot_histogram(counts)
print(counts)
plt.show()
