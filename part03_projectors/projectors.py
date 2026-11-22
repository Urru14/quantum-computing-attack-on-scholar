# Part 3: outer products, projectors, trace trick, completeness, bra-ket table trick, spectral form
import numpy as np
np.set_printoptions(precision=4, suppress=True)
ket = lambda *v: np.array(v, dtype=complex).reshape(-1, 1)
bra = lambda k: k.conj().T

psi1, psi2 = ket(1, 2, 1), ket(1, 0, 1)                       # the notes' example (p4)
print("P1|psi2> = <psi1|psi2>|psi1> =", (psi1 @ bra(psi1) @ psi2).real.ravel())
u = psi1 / np.linalg.norm(psi1)                                # normalise first -> a true projector
P = u @ bra(u)
print("<psi1|psi1> =", (bra(psi1) @ psi1).real.item(), "-> unit u = psi1/sqrt(6)")
print("shadow of psi2 on psi1: P|psi2> =", (P @ psi2).real.ravel(), "= (1/3)|psi1>")
print("P^2 == P:", np.allclose(P @ P, P), "  P^dagger == P:", np.allclose(bra(P), P))

a, b = ket(1, 1j), ket(2, 1)                                    # trace trick with complex vectors
print("Tr(|a><b|) =", np.trace(a @ bra(b)), "  <b|a> =", (bra(b) @ a).item(), "  <a|b> =", (bra(a) @ b).item())

z0, z1 = ket(1, 0), ket(0, 1)
print("Z = |0><0| - |1><1| =\n", (z0 @ bra(z0) - z1 @ bra(z1)).real)
plus, minus = (z0 + z1) / np.sqrt(2), (z0 - z1) / np.sqrt(2)
print("X = (+1)|+><+| + (-1)|-><-| =\n", (plus @ bra(plus) - minus @ bra(minus)).real)
A = np.array([[2, 1], [1, 2]])
lam, V = np.linalg.eigh(A)
S = sum(l * np.outer(V[:, i], V[:, i].conj()) for i, l in enumerate(lam))
print("A = [[2,1],[1,2]]  eigenvalues", lam, " sum lam_i |v_i><v_i| =\n", S.real)
psi = 0.6 * z0 + 0.8 * z1                                       # shadow on |0> -> probability
sh = z0 @ bra(z0) @ psi
print("P0|psi> =", sh.real.ravel(), "  squared length =", round(np.linalg.norm(sh) ** 2, 4), "= P(0)")
print("|0><1| acting on |1> =", (z0 @ bra(z1) @ z1).real.ravel(), "  on |0> =", (z0 @ bra(z1) @ z0).real.ravel())
Hm = (z0 @ bra(z0) + z0 @ bra(z1) + z1 @ bra(z0) - z1 @ bra(z1)) / np.sqrt(2)
print("H|0> from the ket-bra form =", (Hm @ z0).real.ravel(), "= |+>")
print("A = 3|+><+| + 1|-><-| =\n", (3 * plus @ bra(plus) + minus @ bra(minus)).real)
print("A^2 = 9|+><+| + 1|-><-| =\n", (9 * plus @ bra(plus) + minus @ bra(minus)).real, "  check A@A =\n", A @ A)
