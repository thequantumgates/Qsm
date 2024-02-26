import numpy as np

from qsm.gate_library.gate_matrix import *
from qsm.gate_library.gate import Gate
from qsm.utils import *


class Controlled2By2Gate:
    def __init__(self, instruction, methcontrol):
        self.inst = instruction
        self.controller = methcontrol

    def cnot_matrix(self, control_qubit, target_qubit, num_qubits):
        if control_qubit > target_qubit:
            bra_ket_zero = np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + 0j]], "F")

            bra_ket_one = np.array([[0 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], "F")

            bra_ket_zero_kron = [identity()] * num_qubits

            bra_ket_one_kron = [identity()] * num_qubits

            bra_ket_zero_kron[control_qubit] = bra_ket_zero
            bra_ket_one_kron[control_qubit] = bra_ket_one
            bra_ket_one_kron[target_qubit] = self.inst.matrix

            to_add_zero = bra_ket_zero_kron[0]

            to_add_one = bra_ket_one_kron[0]

            for i in range(1, len(bra_ket_zero_kron)):
                to_add_zero = np.kron(to_add_zero, bra_ket_zero_kron[i])

                to_add_one = np.kron(to_add_one, bra_ket_one_kron[i])

            to_add_zero += to_add_one
            return to_add_zero
        else:
            bra_ket_zero = np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0 + 0j]], "F")

            bra_ket_one = np.array([[0 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], "F")

            bra_ket_zero_kron = [identity()] * num_qubits

            bra_ket_one_kron = [identity()] * num_qubits

            bra_ket_zero_kron[control_qubit] = bra_ket_zero
            bra_ket_one_kron[control_qubit] = bra_ket_one
            bra_ket_one_kron[target_qubit] = self.inst.matrix

            bra_ket_zero_kron = bra_ket_zero_kron[::-1]
            bra_ket_one_kron = bra_ket_one_kron[::-1]

            to_add_zero = bra_ket_zero_kron[0]

            to_add_one = bra_ket_one_kron[0]

            for i in range(1, len(bra_ket_zero_kron)):
                to_add_zero = np.kron(to_add_zero, bra_ket_zero_kron[i])

                to_add_one = np.kron(to_add_one, bra_ket_one_kron[i])

            to_add_zero += to_add_one
            return to_add_zero

    def apply(self, state, control_qubit, target_qubit):
        mat = self.cnot_matrix(control_qubit, target_qubit, int(np.log2(len(state))))
        return mat @ state


class ControlledGate(Gate):
    def __init__(self, instruction):
        super().__init__(instruction)

    def apply(self, state, qubit1, qubit2):
        matrix = self.inst.matrix
        iden = [identity()] * int(np.log2(len(state))-1)
        i = min([qubit1, qubit2])
        iden[i] = matrix
        operator = iden[0]
        for i in iden[1:]:
            operator = np.kron(operator, i)

        return operator @ state