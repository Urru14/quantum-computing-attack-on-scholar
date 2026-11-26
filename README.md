# Quantum Computing – Attack on Scholar

Code for the **Quantum Computing** lecture series on the *Attack on Scholar* YouTube channel.
Every number shown on screen in a lecture comes from a script in this repo – run it and you get the same output.

The series goes: **maths basics → concepts, step by step → by-hand calculations + code → a small project based on a published research paper.**

| Part | Topic | Folder |
|---|---|---|
| 1 | Bits, qubits, measurement, interference | [`part01_bits_and_qubits`](part01_bits_and_qubits) |
| 2 | Hilbert space, Dirac (bra-ket) notation, inner products | [`part02_hilbert_space`](part02_hilbert_space) |
| 3 | Outer products, projectors, the trace trick, completeness, spectral form | [`part03_projectors`](part03_projectors) |
| 4 | The postulates: states, unitary time evolution, measurement | [`part04_postulates`](part04_postulates) |
| 5 | Two qubits: tensor products, product vs entangled, Bell states, a real IBM run | [`part05_tensor_products`](part05_tensor_products) |
| … | density matrix, Bloch sphere, gates, circuits, algorithms | coming |
| Project | Simulating an atomic nucleus on a quantum computer (¹⁸O ground state with the variational quantum eigensolver, VQE), based on a published research paper | [`project_18O`](project_18O) |

Each folder has a README, the scripts (`*.py`) exactly as shown on screen, and their recorded output (`*_out.txt`).

## Setup
```bash
conda create -n qc python=3.11
conda activate qc
pip install numpy qiskit qiskit-aer
python part03_projectors/projectors.py
```
Tested with qiskit 2.6.2 and qiskit-aer 0.18.4.
For the real-hardware run in Part 5 also `pip install qiskit-ibm-runtime` (see that folder's README).
