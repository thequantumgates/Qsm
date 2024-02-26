import numpy as np
from qsm.gate_library.gate_matrix import *

def cnot_num_qubit(num, qubit):
    if num == 0:
        return qubit
    else:
        return qubit @ paulix()

def cnot_controller(target, control):
    if target > control:
        return cnot(little_endian=True)
    else:
        return cnot(little_endian=False)