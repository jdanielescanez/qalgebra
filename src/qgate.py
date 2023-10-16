
from src.qstate import QState
import copy

class QGate:
  def __init__(self, matrix: list, targets: list, controls: list=[]) -> None:
    self.matrix = matrix
    self.targets = targets
    self.controls = controls
    
    # TODO: Add symbol
    # chr(127215 + ord('A')) = chr(127280) = 🄰
    # self.symbol = chr(127215 + ord(self.get_name()))

  def __str__(self) -> str:
    controls_string = ('^{' + str(self.controls)[1:-1] + '}') if len(self.controls) > 0 else ''
    return self.get_name() + '_{' + str(self.targets)[1:-1] + '}' + controls_string

  @classmethod
  def get_name(cls):
    return cls.__name__

  def apply(self, qstate: QState):
    new_qstate = copy.copy(qstate)

    for j in self.targets:
      current_qstate = copy.copy(new_qstate)
      current_qstate.all_zero()
      for i, coefficient in enumerate(new_qstate.state):
        if coefficient != 0:
          if all([new_qstate.reversed_tags[i][x] == '1' for x in self.controls]):
            if new_qstate.reversed_tags[i][j] == '0':
              current_qstate.state[i] += self.matrix[0][0] * coefficient
              current_qstate.state[i + 2 ** j] += self.matrix[0][1] * coefficient
            else:
              current_qstate.state[i - 2 ** j] += self.matrix[1][0] * coefficient
              current_qstate.state[i] += self.matrix[1][1] * coefficient
          else:
            current_qstate.state[i] += coefficient
      new_qstate = copy.copy(current_qstate)
    return new_qstate
