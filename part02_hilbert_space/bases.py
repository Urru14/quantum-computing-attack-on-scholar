import numpy as np

zero, one = np.array([1, 0]), np.array([0, 1])
plus, minus = (zero + one) / np.sqrt(2), (zero - one) / np.sqrt(2)
out = np.outer
print("Z: |0><0| + |1><1| =\n", out(zero, zero) + out(one, one))
print("X: |+><+| + |-><-| =\n", np.round(out(plus, plus) + out(minus, minus), 12))

X = out(zero, one) + out(one, zero)
H = (out(zero, zero) + out(zero, one) + out(one, zero) - out(one, one)) / np.sqrt(2)
print("X =\n", X)
print("H =\n", np.round(H, 4))

psi = 0.6 * zero + 0.8 * one
amp = np.vdot(one, psi)
print("<1|psi> =", amp, "  prob =", round(abs(amp) ** 2, 2))
