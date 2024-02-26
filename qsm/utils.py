import numpy as np
from qsm.gate_library.gate_matrix import *


def possible_bits(state):
    num_bits = int(np.log2(len(state)))
    num_states = 2 ** num_bits

    binary_states = [bin(i)[2:].zfill(num_bits) for i in range(num_states)]

    return binary_states


def initial_dict_state(state):
    num_bits = int(np.log2(len(state)))
    num_states = 2 ** num_bits

    binary_states = [bin(i)[2:].zfill(num_bits) for i in range(num_states)]

    dict_state = {state: 0 for state in binary_states}

    return dict_state


def initial_dict_list(state):
    num_bits = len(state)
    num_states = 2 ** num_bits

    binary_states = [bin(i)[2:].zfill(num_bits) for i in range(num_states)]

    dict_state = {state: 0 for state in binary_states}

    return dict_state


def dict_list(state):
    num_bits = len(state)
    num_states = 2 ** num_bits

    binary_states = [bin(i)[2:].zfill(num_bits) for i in range(num_states)]
    return binary_states


def cnot_gate(c, t):
    if c > t:
        return cnot(little_endian=True)
    else:
        return cnot()


projectors = [np.array([[1, 0], [0, 0]]), np.array([[0, 0], [0, 1]])]


def project(i, j, reg):
    reg.customgate(i, projectors[j])
    reg.qubits.state /= np.linalg.norm(reg.qubits.state)
    return reg.qubits.state
