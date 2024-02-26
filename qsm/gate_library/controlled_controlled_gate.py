import numpy as np

from qsm.gate_library.gate_matrix import *
from qsm.utils import *


class Toffolie:
    def __init__(self, instruction, methcontrol):
        self.inst = instruction
        self.controller = methcontrol

    def apply(self, state, control_qubit1, control_qubit2, target_qubit):
        mat = Toffoli(int(np.log2(len(state))), control_qubit1, control_qubit2, target_qubit)
        print(mat)
        return np.dot(mat, state)
