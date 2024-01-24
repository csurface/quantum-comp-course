from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt

# 2 qubits, superposition with entanglement
c = QuantumCircuit(2,2)
c.h(0)
c.cx(0,1)
c.measure([0,1],[0,1])

# Optionally draw the circuit using matplotlib
#c.draw(output='mpl')
#plt.show()

# Use the local simulator
sim = Aer.get_backend('qasm_simulator')
result = execute(c,backend=sim).result()

plot_histogram(result.get_counts(c))
plt.show()

