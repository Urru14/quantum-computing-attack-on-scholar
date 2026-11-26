# Part 5: the same Bell pair (H then CNOT, measure both) on a REAL IBM quantum computer, 1000 shots
from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
qc = QuantumCircuit(2, 2); qc.h(0); qc.cx(0, 1); qc.measure([0, 1], [0, 1])
service = QiskitRuntimeService()
backend = service.backend("ibm_fez")
isa = generate_preset_pass_manager(optimization_level=1, backend=backend).run(qc)
job = Sampler(mode=backend).run([isa], shots=1000)
print("backend:", backend.name, " job:", job.job_id(), flush=True)
counts = job.result()[0].data.c.get_counts()
bad = counts.get("01", 0) + counts.get("10", 0)
print("Bell pair on ibm_fez, 1000 shots:", dict(sorted(counts.items())), f"  01 or 10: {bad} ({bad / 10:.1f}%)")
