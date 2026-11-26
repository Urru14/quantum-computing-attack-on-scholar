# Part 5 · Two qubits: tensor products and entanglement

| Script | What it shows | Output |
|---|---|---|
| `tensor.py` | Postulate 4: tensor (Kronecker) products of columns, \|00⟩…\|11⟩, order matters · how fast 2ⁿ grows · product vs entangled (the ad = bc test) · the four Bell states are orthonormal · gates in parallel, H⊗I and I⊗H · a Bell pair on the Qiskit Aer simulator (1000 shots, seed 2026) · Qiskit's qubit order | [`tensor_out.txt`](tensor_out.txt) |
| `bell_ibm.py` | The same Bell pair on a **real IBM quantum computer** (ibm_fez, 156 qubits, 1000 shots) | [`bell_ibm_out.txt`](bell_ibm_out.txt) |

Run: `python tensor.py`

`bell_ibm.py` needs a free IBM Quantum account (Open Plan) and `pip install qiskit-ibm-runtime`. Save your own API key once with
`QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token="<your key>", instance="<your CRN>")` – never put a key in the script.
A real machine is noisy, so your counts will differ a little from ours (we got 46 of 1000 shots with the qubits disagreeing).
