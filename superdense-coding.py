from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt
import sys

c = QuantumCircuit(2,2)
c.h(0)
c.cx(0,1)

message = str(sys.argv[1])
print('Message {}'.format(message))

if message == '00':
    c.id(0)
elif message == '01':
    c.x(0)
elif message == '10':
    c.z(0)
elif message == '11':
    c.z(0)
    c.x(0)
else:
    print('Invalid message')
    sys.exit(1)

c.cx(0,1)
c.h(0)

#c.measure([0,1],[0,1])
c.measure_all()

# Use the local simulator
sim = Aer.get_backend('qasm_simulator')
result = execute(c,backend=sim).result()
counts = result.get_counts()

c.draw(output='mpl', style='iqp')
plt.show()

plot_histogram(counts)
plt.show()
