from qiskit import *
from qiskit.providers import *
from qiskit_ibm_provider import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt

# https://quantum.ibm.com/account
#TOKEN = '6dcfae469161f20b96c050d468c957a6885396c65b2cd97618ce5de58a63cee28b0eb3f3f615444279dcbf3957f99cd91d677018876327891723f27bc0216ff0'

# Only need to do this once. See the saved token in ~/.qiskit/
#IBMProvider.save_account(token=TOKEN)

provider = IBMProvider()

def dump_backend_info():
    for b in provider.backends():
        print(b)
        print(b.status().to_dict())
        p = b.properties()
        if p is not None:
            print(len(p.qubits))

backend = provider.get_backend('ibm_osaka')
#backend = provider.get_backend('ibmq_qasm_simulator')

# 2 qubits, superposition with entanglement
circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1],[0,1])

job = execute(circuit,backend=backend)
print(job)

while (job.status() != JobStatus.DONE):
    print(job)
    print(job.status())
    time.sleep(5)

result = job.result()
plot_histogram(result.get_counts(circuit))
plt.show()
