from qiskit import *
from qiskit.providers import *
from qiskit_ibm_provider import *
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import plot_bloch_multivector
import time
from matplotlib import pyplot as plt
import math

#print(Aer.backends())

qasm_sim = Aer.get_backend('qasm_simulator')
sv_sim = Aer.get_backend('statevector_simulator')

def run(circuit):
    sv_job = execute(circuit, backend=sv_sim)
    result = sv_job.result()
    sv = result.get_statevector()

    num_qubits = circuit.num_qubits
    circuit.measure([i for i in range(num_qubits)], [i for i in range(num_qubits)])

    qasm_job = execute(circuit, backend=qasm_sim, shots=1024)
    qasm_result = qasm_job.result()
    counts = qasm_result.get_counts()

    return sv, counts

def run_and_plot(circuit):
    sv, counts = run(circuit)
    circuit.draw(output='mpl')
    plt.show()

    plot_bloch_multivector(sv)
    plt.show()

    plot_histogram([counts])
    plt.show()

#circuit = QuantumCircuit(2,2)
#circuit.h(0)
#circuit.cx(0,1)
#run_and_plot(circuit)

#circuit = QuantumCircuit(2,2)
#circuit.rx(math.pi/4,0)
#circuit.rx(math.pi/2,1)
#run_and_plot(circuit)

# Demonstrating that Hadamard does a rotation similar to the rx() example above (geometrically).
#circuit = QuantumCircuit(1,1)
#circuit.h(0)
#circuit.z(0)
#run_and_plot(circuit)

circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)
circuit.z(0)
circuit.cx(0,1)
circuit.h(0)
run_and_plot(circuit)
