from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt
import sys

c = QuantumCircuit(3,3)
c.x(0)
c.barrier()

c.h(1)
c.cx(1,2)
c.barrier()

c.cx(0,1)
c.h(0)
c.barrier()

c.measure([0,1],[0,1])
c.barrier()

c.cx(1,2)
c.cz(0,2)

c.measure([2],[2])

c.draw(output='mpl', style='iqp')
plt.show()

# Use the local simulator
sim = Aer.get_backend('qasm_simulator')
result = execute(c,backend=sim).result()
counts = result.get_counts()

# The first bit is actually qubit 2, and should be 1 for all results,
# meaning that the value of qubit 0 was teleported.
plot_histogram(counts)
plt.show()
