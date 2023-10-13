
from src.qstate import QState
import copy

class QGate:
  def __init__(self, matrix: list, targets: list, controls: list=[]) -> None:
    self.matrix = matrix
    self.targets = targets
    self.controls = controls

  def __str__(self) -> str:
    controls_string = ('^{' + str(self.controls)[1:-1] + '}') if self.controls != [] else ''
    return self.get_name() + '_{' + str(self.targets)[1:-1] + '}' + controls_string

  @classmethod
  def get_name(cls):
    return cls.__name__

  def apply(self, qstate: QState):
    new_qstate = copy.copy(qstate)
    new_qstate.all_zero()
    for i, coefficient in enumerate(qstate.state):
      if coefficient != 0:
        for j in self.targets:
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
