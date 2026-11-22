# Quantum Computing – Attack on Scholar

Code for the **Quantum Computing** lecture series on the *Attack on Scholar* YouTube channel.
Every number shown on screen in a lecture comes from a script in this repo – run it and you get the same output.

The series goes: **maths basics → concepts, step by step → by-hand calculations + code → a small project built on a published paper.**

| Part | Topic | Folder |
|---|---|---|
| 1 | Bits, qubits, measurement, interference | [`part01_bits_and_qubits`](part01_bits_and_qubits) |
| 2 | Hilbert space, Dirac (bra-ket) notation, inner products | [`part02_hilbert_space`](part02_hilbert_space) |
| 3 | Outer products, projectors, the trace trick, completeness, spectral form | [`part03_projectors`](part03_projectors) |
| … | postulates, tensor products, density matrix, Bloch sphere, gates, entanglement, algorithms | coming |
| Project | Simulating an atomic nucleus on a quantum computer (¹⁸O ground state with the variational quantum eigensolver, VQE), based on a published research paper | [`project_18O`](project_18O) |

Each folder has the scripts (`*.py`) and their recorded output (`*_out.txt`).

## Setup
```bash
conda create -n qc python=3.11
conda activate qc
pip install numpy qiskit qiskit-aer
python part03_projectors/projectors.py
```
Tested with qiskit 2.6.2 and qiskit-aer 0.18.4.
