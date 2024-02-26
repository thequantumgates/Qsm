import warnings

import numpy as np

from qsm.qubit import *
from qsm.gate_library import *
from qsm.instruction import *
from qsm.utils import *

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

pi = np.pi

class QuantumCircuit:
    def __init__(self, num_qubits):
        self.qubits = Qubit(num_qubits)

    def h(self, qubit):
        self.customgate(qubit, hadamard())

    def cx(self, qubit_control, qubit_target):
        self.custom_control(qubit_control, qubit_target, paulix())

    def cy(self, qubit_control, qubit_target):
        self.custom_control(qubit_control, qubit_target, pauliy())

    def cz(self, qubit_control, qubit_target):
        self.custom_control(qubit_control, qubit_target, pauliz())

    def custom_control(self, qubit_control, qubit_target, matrix):
        gate = Controlled2By2Gate(Instruction(matrix), None)
        self.qubits.apply_controlled_gate(gate, qubit_control, qubit_target)

    def x(self, qubit):
        self.customgate(qubit, paulix())

    def y(self, qubit):
        self.customgate(qubit, pauliy())

    def z(self, qubit):
        self.customgate(qubit, pauliz())

    def s(self, qubit):
        self.customgate(qubit, s())

    def rx(self, qubit, angle):
        self.customgate(qubit, rx(angle))

    def ry(self, qubit, angle):
        self.customgate(qubit, ry(angle))

    def rz(self, qubit, angle):
        self.customgate(qubit, rz(angle))

    def sdg(self, qubit):
        self.customgate(qubit, sdg())

    def t(self, qubit):
        self.customgate(qubit, t())

    def tdg(self, qubit):
        self.customgate(qubit, tdg())

    def u3(self, theta, phi, lamba, qubit):
        self.customgate(qubit, u(theta, phi, lamba))

    def u2(self, phi, lamba, qubit):
        self.customgate(qubit, u(pi/2, phi, lamba))

    def u1(self, lamba, qubit):
        self.customgate(qubit, u(0, 0, lamba))

    def p(self, lamba, qubit):
        self.customgate(qubit, phase(lamba))

    def toffolie(self, qubit_control1, qubit_control2, qubit_target):
        self.h(qubit_target)
        self.cx(qubit_control2, qubit_target)
        self.tdg(qubit_target)
        self.cx(qubit_control1, qubit_target)
        self.t(qubit_target)
        self.cx(qubit_control2, qubit_target)
        self.tdg(qubit_target)
        self.t(qubit_control2)
        self.cx(qubit_control1, qubit_target)
        self.t(qubit_target)
        self.cx(qubit_control1, qubit_control2)
        self.h(qubit_target)
        self.tdg(qubit_control2)
        self.t(qubit_control1)
        self.cx(qubit_control1, qubit_control2)

    def swap(self, qubit1, qubit2):
        gate_inst = Instruction(swap())
        gate = ControlledGate(gate_inst)
        self.qubits.apply_controlled_gate(gate, qubit1, qubit2)

    def customgate(self, qubit, matrix):
        gate_inst = Instruction(matrix)
        gate = SingelletonGate(gate_inst)
        self.qubits.apply_gate(gate, qubit)

    def state_vector(self):
        return np.round(self.qubits.state, decimals=3)

    def probabilities(self):
        self.qubits.state /= np.linalg.norm(self.qubits.state)
        return np.abs(self.qubits.state) ** 2

    def measure_all(self, shots=1024):
        args = initial_dict_state(self.qubits.state)
        states = possible_bits(self.qubits.state)
        for i in range(shots):
            prob = self.probabilities()
            ret = np.random.choice(states, p=prob)
            args[ret] += 1

        return args

    def measure(self, qubit_index):
        prob = self.probabilities()
        res = np.random.choice(possible_bits(self.qubits.state), p=prob)
        res = int(res[qubit_index])
        # Sample according to probability distribution
        self.qubits.state = project(qubit_index, res, self)
        return res


