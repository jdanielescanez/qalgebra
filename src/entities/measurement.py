
from src.entities.qgate import QGate
from src.entities.qstate import QState
import copy
from random import random
from cmath import sqrt

class M(QGate):
  def __init__(self, targets: list, _: list) -> None:
    super().__init__([], targets)

  def apply(self, qstate: QState) -> QState:
    n = qstate.size
    norm_coef = 0
    new_qstate = copy.copy(qstate)

    for t in self.targets:
      prob_0 = 0
      for i in range(0, 2 ** n, 2 ** (t + 1)):
        for j in range(2 ** t):
          coef = new_qstate.state[i + j]
          prob_0 += abs(coef) ** 2
          norm_coef += coef ** 2

      norm_coef = sqrt(norm_coef)
      random_number = random()
      is_measured_zero = random_number < prob_0
      coef_index, zero_index = (0, 2 ** t) if is_measured_zero else (2 ** t, 0)

      for i in range(coef_index, 2 ** n, 2 ** (t + 1)):
        for j in range(2 ** t):
          new_qstate.state[i + j] /= norm_coef
      for i in range(zero_index, 2 ** n, 2 ** (t + 1)):
        for j in range(2 ** t):
          new_qstate.state[i + j] = 0
      
    return new_qstate
