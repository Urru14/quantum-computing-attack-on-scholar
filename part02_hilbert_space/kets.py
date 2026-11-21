import numpy as np

psi1 = np.array([1, 2, 1])
psi2 = np.array([1, 0, 1])
print("<psi1|psi2> =", np.vdot(psi1, psi2))

P1 = np.outer(psi1, psi1.conj())
print("|psi1><psi1| =\n", P1)
O12 = np.outer(psi1, psi2.conj())
print("|psi1><psi2| =\n", O12)
print("trace =", np.trace(O12))

print("P1 @ P1 == 6 * P1 :", np.allclose(P1 @ P1, 6 * P1))   # not normalised: P^2 = 6P
u = psi1 / np.linalg.norm(psi1)          # a projector needs a UNIT vector
P = np.outer(u, u.conj())
print("P @ P == P :", np.allclose(P @ P, P))
