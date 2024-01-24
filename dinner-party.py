from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import PhaseOracle
from qiskit.primitives import Sampler
from qiskit_algorithms import AmplificationProblem
from qiskit_algorithms import Grover
import time
from matplotlib import pyplot as plt
import sys

# Dinner Party
# Host a dinner party with as many guests as possible given constraints.
# James and Lars
# OR
# Kirk and Rob
# AND NOT
# Lars and Rob

# https://qiskit.org/ecosystem/algorithms/tutorials/07_grover_examples.html

expression = '((James & Lars) | (Kirk & Rob)) & ~(Lars & Rob)'
oracle = PhaseOracle(expression)
problem = AmplificationProblem(oracle, is_good_state=oracle.evaluate_bitstring)
grover = Grover(sampler=Sampler())
result = grover.amplify(problem)
#counts = result.get_counts()
plot_histogram(result.circuit_results[0])
plt.show()

