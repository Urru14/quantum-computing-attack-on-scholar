from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

sim = AerSimulator(seed_simulator=2026)
counts = sim.run(qc, shots=1000).result().get_counts()
print(counts)
