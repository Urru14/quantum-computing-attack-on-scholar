import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
np.set_printoptions(precision=4, suppress=True)
ket = lambda *v: np.array(v, dtype=complex).reshape(-1, 1)
bra = lambda k: k.conj().T
zero, one = ket(1, 0), ket(0, 1)
plus, minus = (zero + one) / np.sqrt(2), (zero - one) / np.sqrt(2)

# Postulate 1: one state, three bases
print("|0> = (|+> + |->)/sqrt2 :", np.allclose(zero, (plus + minus) / np.sqrt(2)))
print("|1> = (|+> - |->)/sqrt2 :", np.allclose(one, (plus - minus) / np.sqrt(2)))

# Postulate 2: U = exp(-iHt), built from the spectral form (hbar = 1), here H = X
lam, vec = np.linalg.eigh(np.array([[0, 1], [1, 0]], dtype=complex))
t = 0.5
U = sum(np.exp(-1j * l * t) * np.outer(v, v.conj()) for l, v in zip(lam, vec.T))
print("U(t=0.5) =\n", U)
print("U^dagger U = I :", np.allclose(bra(U) @ U, np.eye(2)))
X = np.array([[0, 1], [1, 0]], dtype=complex)
print("U = cos(t) I - i sin(t) X :", np.allclose(U, np.cos(t) * np.eye(2) - 1j * np.sin(t) * X))
psi_t = U @ zero
print("|psi(t)> = U|0> =", psi_t.ravel(), "  P(1) =", round(abs(psi_t[1, 0]) ** 2, 4))

# Postulate 3: measurement operators M0 = |0><0|, M1 = |1><1|
psi = 0.6 * zero + 0.8 * one
M0, M1 = zero @ bra(zero), one @ bra(one)
for m, M in (("0", M0), ("1", M1)):
    p = (bra(psi) @ M @ psi).real.item()
    print(f"P{m} = <psi|M{m}|psi> = {p:.2f}   after: {(M @ psi / np.sqrt(p)).real.ravel()}")
print("M0^dag M0 + M1^dag M1 = I :", np.allclose(bra(M0) @ M0 + bra(M1) @ M1, np.eye(2)))
psi_c = 0.6j * zero + 0.8 * one
after = M0 @ psi_c / np.sqrt((bra(psi_c) @ M0 @ psi_c).real.item())
print("alpha = 0.6i  ->  after measuring 0:", after.ravel(), " = i|0>  (a global phase)")

# measuring in the X basis
Mp, Mm = plus @ bra(plus), minus @ bra(minus)
print("P+ =", round((bra(psi) @ Mp @ psi).real.item(), 2), "  P- =", round((bra(psi) @ Mm @ psi).real.item(), 2))
pi_, mi_ = (zero + 1j * one) / np.sqrt(2), (zero - 1j * one) / np.sqrt(2)
print("Y basis: P(+i) =", round(abs((bra(pi_) @ psi).item()) ** 2, 2), "  P(-i) =", round(abs((bra(mi_) @ psi).item()) ** 2, 2))
qc = QuantumCircuit(1, 1)
qc.ry(2 * np.arctan2(0.8, 0.6), 0)      # prepare 0.6|0> + 0.8|1>
qc.h(0)                                  # rotate the X basis onto the Z basis
qc.measure(0, 0)
counts = AerSimulator(seed_simulator=2026).run(qc, shots=1000).result().get_counts()
print("X-basis measurement, 1000 shots ('0' = +, '1' = -):", dict(sorted(counts.items())))

# added for the 9-minute cut: (1) H = X for t = pi/2 is the X gate; (2) measuring twice; (3) a state certain in Y
t2 = np.pi / 2
U2 = sum(np.exp(-1j * l * t2) * np.outer(v, v.conj()) for l, v in zip(lam, vec.T))
print("t = pi/2:  U = -iX :", np.allclose(U2, -1j * X), "  U|0> =", np.round(U2 @ zero, 4).ravel(), "  P(1) =", round(abs((U2 @ zero)[1, 0]) ** 2, 4))
qc2 = QuantumCircuit(1, 2)
qc2.ry(2 * np.arctan2(0.8, 0.6), 0)
qc2.measure(0, 0)
qc2.measure(0, 1)                        # measure the same qubit again, straight away
c2 = AerSimulator(seed_simulator=2026).run(qc2, shots=1000).result().get_counts()
print("measure twice, 1000 shots:", dict(sorted(c2.items())), "  first and second always agree:", set(c2) <= {"00", "11"})
psi_y = (zero + 1j * one) / np.sqrt(2)
print("(|0> + i|1>)/sqrt2:  Z: P(0) =", round(abs((bra(zero) @ psi_y).item()) ** 2, 2), " P(1) =", round(abs((bra(one) @ psi_y).item()) ** 2, 2),
      "   Y: P(+i) =", round(abs((bra(pi_) @ psi_y).item()) ** 2, 2), " P(-i) =", round(abs((bra(mi_) @ psi_y).item()) ** 2, 2))
