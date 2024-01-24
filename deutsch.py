from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt
import sys

# Determine if a function is constant or balanced.
# f:{0,1} -> {0,1}
# f(0) =  f(1) : constant
# f(0) != f(1) : balanced or f(0) = f(1) xor 1

c = QuantumCircuit(2,2)

c.x(1)
c.h([0,1])

c.barrier()

# This is the black box portion, using cx as an example.
c.cx(0,1)

c.barrier()
c.h(0)

c.measure([0],[0])

c.draw(output='mpl', style='iqp')
plt.show()

# Use the local simulator
sim = Aer.get_backend('qasm_simulator')
result = execute(c,backend=sim).result()
counts = result.get_counts()

#plot_histogram(counts)
print(counts)
plt.show()
