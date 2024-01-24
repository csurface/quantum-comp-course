from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt
import sys

# Guess the secret number using a BV circuit.
# Kinda misleading because the secret is known as input
# and the circuit is built based on the secret value.

secret = str(sys.argv[1])
secret_len = len(secret)
print('Secret {} length {}'.format(secret, secret_len))

c = QuantumCircuit(secret_len+1, secret_len)
last_qubit_index = secret_len

secret_qubits = [x for x in range(secret_len)]

c.h(secret_qubits)
c.x(secret_len)
c.h(secret_len)
c.barrier()

# Iterate from right to left to avoid endian-ness confusion about the result.
i = secret_len - 1
qi = 0
while i >= 0:
    secret_bit = secret[i]
    if secret_bit == '1':
        c.cx(qi, last_qubit_index)
    i -= 1
    qi += 1

c.barrier()
c.h(secret_qubits)

c.measure(secret_qubits, secret_qubits)

c.draw(output='mpl', style='iqp')
plt.show()

# Use the local simulator
sim = Aer.get_backend('qasm_simulator')
result = execute(c,backend=sim).result()
counts = result.get_counts()

#plot_histogram(counts)
print(counts)
plt.show()
