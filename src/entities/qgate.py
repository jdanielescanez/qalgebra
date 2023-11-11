
from src.entities.qstate import QState
import copy

class QGate:
  def __init__(self, matrix: list, targets: list, controls: list=[]) -> None:
    self.matrix = matrix
    self.targets = targets
    self.controls = controls
    
    # TODO: Add symbol
    # chr(127215 + ord('A')) = chr(127280) = 🄰
    # self.symbol = chr(127215 + ord(self.get_name()))

  def format_indexes(self, indexes) -> str:
    string = ''
    i = 0
    j = i
    while i < len(indexes):
      while j + 1 < len(indexes) and indexes[j] + 1 == indexes[j + 1]:
        j += 1
      if i + 1 == j:
        string += f'{indexes[i]},{indexes[j]},'
        i = j
      elif i != j:
        string += f'{indexes[i]}-{indexes[j]},'
        i = j
      else:
        string += f'{indexes[i]},'
      i += 1
      j = i
    return string[:-1]

  def __str__(self) -> str:
    formated_targets = self.format_indexes(self.targets)
    if len(self.controls) > 0:
      formated_controls = self.format_indexes(self.controls)
      controls_string = '^{' + formated_controls + '}'
    else:
      controls_string = ''
    return self.get_name() + '_{' + formated_targets + '}' + controls_string

  @classmethod
  def get_name(cls):
    return cls.__name__

  def apply(self, qstate: QState) -> QState:
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
