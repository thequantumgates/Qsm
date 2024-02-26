import numpy as np


class Qubit:
    def __init__(self, size):
        self.state = np.array([1, 0])
        for i in range(size-1):
            self.state = np.kron(self.state, np.array([1, 0]))

    def apply_gate(self, gate, target_qubit):
        self.state = gate.apply(self.state, target_qubit)

    def apply_controlled_gate(self, gate, target_qubit, other_qubit):
        self.state = gate.apply(self.state, target_qubit, other_qubit)

    def apply_controlled_controlled_gate(self, gate, target_qubit, control_qubit1, control_qubit2):
        self.state = gate.apply(self.state, control_qubit1, control_qubit2, target_qubit)