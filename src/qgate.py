
from src.qstate import QState
import copy

class QGate:
  def __init__(self, matrix: list, indexes: list, controls: list=[]) -> None:
    self.matrix = matrix
    self.indexes = indexes
    self.controls = controls

  def apply(self, qstate: QState):
    new_qstate = copy.copy(qstate)
    new_qstate.all_zero()
    for i, coefficient in enumerate(qstate.state):
      if coefficient != 0:
        for j in self.indexes:
          if all([qstate.reversed_tags[i][x] == '1' for x in self.controls]):
            if qstate.reversed_tags[i][j] == '0':
              new_qstate.state[i] += self.matrix[0][0] * qstate.state[i]
              new_qstate.state[i + 2 ** j] += self.matrix[0][1] * qstate.state[i]
            else:
              new_qstate.state[i - 2 ** j] += self.matrix[1][0] * qstate.state[i]
              new_qstate.state[i] += self.matrix[1][1] * qstate.state[i]
          else:
            new_qstate.state[i] = qstate.state[i]
    return new_qstate
