# Part 2 (v2): why the bra needs the complex conjugate, normalising by hand, eigenvectors of X
import numpy as np
psi = np.array([1, 1j]) / np.sqrt(2)          # (|0> + i|1>)/sqrt2
print("no conjugate :", np.round(psi @ psi, 3))          # plain dot: 1/2 + i^2/2 = 0  (a nonzero arrow with 'length' 0?!)
print("with bra     :", np.round(np.vdot(psi, psi), 3))  # <psi|psi> = 1
v = np.array([3, 4j])                          # 3|0> + 4i|1>
n = np.sqrt(np.vdot(v, v).real)
print("<v|v> =", np.vdot(v, v).real, " length =", n, " normalised:", v / n)
print("P(0), P(1) =", np.round(np.abs(v / n) ** 2, 2))
X = np.array([[0, 1], [1, 0]])
plus, minus = np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2)
print("X|+> = ", np.round(X @ plus, 3), "= +1 |+>")
print("X|-> = ", np.round(X @ minus, 3), "= -1 |->")
print("eigenvalues of X:", np.linalg.eigvalsh(X))
