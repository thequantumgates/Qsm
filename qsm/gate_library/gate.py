import numpy as np
from qsm.gate_library.gate_matrix import *

class Gate:
    def __init__(self, instruction):
        self.inst = instruction

    def apply(self, state, target_qubit):
        pass


class SingelletonGate(Gate):
    def __init__(self, instruction):
        super().__init__(instruction)

    def apply(self, state, target_qubit):
        size = int(np.log2(len(state)))
        mat = self.inst.matrix
        ket_zero = [identity()] * size
        ket_zero[target_qubit] = mat
        operator = ket_zero[0]
        for i in ket_zero[1:]:
            operator = np.kron(i, operator)
        return operator @ state