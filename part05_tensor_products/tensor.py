import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
np.set_printoptions(precision=4, suppress=True)
ket = lambda *v: np.array(v, dtype=complex).reshape(-1, 1)
zero, one = ket(1, 0), ket(0, 1)
plus = (zero + one) / np.sqrt(2)
show = lambda v: np.round(v.real.ravel(), 4)

# Postulate 4: two systems together = tensor (Kronecker) product
print("|0> (x) |0> = |00> =", show(np.kron(zero, zero)))
print("|0> (x) |1> = |01> =", show(np.kron(zero, one)))
print("|1> (x) |0> = |10> =", show(np.kron(one, zero)))
print("|1> (x) |1> = |11> =", show(np.kron(one, one)))
a = 0.6 * zero + 0.8 * one
print("(0.6|0> + 0.8|1>) (x) |+> =", show(np.kron(a, plus)))
print("order matters: |0>(x)|1> == |1>(x)|0> :", np.allclose(np.kron(zero, one), np.kron(one, zero)))

# product or entangled?  a|00> + b|01> + c|10> + d|11> is a product exactly when ad = bc
def test(name, v):
    a_, b_, c_, d_ = v.ravel()
    print(f"{name:22s} ad = {abs(a_*d_):.2f}  bc = {abs(b_*c_):.2f}  ->", "product" if np.isclose(a_*d_, b_*c_) else "ENTANGLED")
test("(|00> + |10>)/sqrt2", (np.kron(zero, zero) + np.kron(one, zero)) / np.sqrt(2))
test("(|00>+|01>+|10>+|11>)/2", (np.kron(zero, zero) + np.kron(zero, one) + np.kron(one, zero) + np.kron(one, one)) / 2)
test("(|00> + |11>)/sqrt2", (np.kron(zero, zero) + np.kron(one, one)) / np.sqrt(2))

# the four Bell states are orthonormal
B = {"B00": (np.kron(zero, zero) + np.kron(one, one)) / np.sqrt(2),
     "B10": (np.kron(zero, zero) - np.kron(one, one)) / np.sqrt(2),
     "B01": (np.kron(zero, one) + np.kron(one, zero)) / np.sqrt(2),
     "B11": (np.kron(zero, one) - np.kron(one, zero)) / np.sqrt(2)}
G = np.array([[(B[i].conj().T @ B[j]).real.item() for j in B] for i in B])
print("Bell states <Bi|Bj> = identity :", np.allclose(G, np.eye(4)))

# gates in parallel: (A (x) B)(|x> (x) |y>) = A|x> (x) B|y>
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
I = np.eye(2)
print("sqrt2 * (H (x) I) =\n", np.round(np.kron(H, I) * np.sqrt(2)) + 0)
print("sqrt2 * (I (x) H) =\n", np.round(np.kron(I, H) * np.sqrt(2)) + 0)
out = np.kron(H, I) @ np.kron(zero, one)
print("(H (x) I)|01> =", show(out), " = (|01> + |11>)/sqrt2 :", np.allclose(out, (np.kron(zero, one) + np.kron(one, one)) / np.sqrt(2)))
print("(H (x) I)(|0>(x)|1>) == H|0> (x) I|1> :", np.allclose(out, np.kron(H @ zero, I @ one)))
print("2 qubits: 4 numbers · 10 qubits:", 2**10, "· 50 qubits:", f"{2**50:.2e}", "· 300 qubits:", f"{2.0**300:.2e}")

# a real run: make B00 (H then CNOT) and measure both qubits, 1000 shots
qc = QuantumCircuit(2, 2); qc.h(0); qc.cx(0, 1); qc.measure([0, 1], [0, 1])
counts = AerSimulator(seed_simulator=2026).run(qc, shots=1000).result().get_counts()
print("Bell pair, 1000 shots:", dict(sorted(counts.items())), "  01 or 10 ever?", any(k in counts for k in ("01", "10")))
# Qiskit writes qubit 0 on the RIGHT (little-endian)
qc1 = QuantumCircuit(2); qc1.x(0)
print("Qiskit: X on qubit 0 gives", {str(k): float(v) for k, v in Statevector(qc1).probabilities_dict().items()}, "(qubit 0 is the rightmost digit)")
