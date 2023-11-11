
import re

from src.entities.qgates import gates

class Parser:
  def __init__(self):
    self.operations = []

  def run(self, text: str) -> list:
    # TODO: Add compatibility: comma and en dash notation, ranges :
    # new regex: (?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\d+(?::\d+)?(?:,\d+(?::\d+)?)*)\})|(?:\^\{(?P<controls>\d+(?::\d+)?(?:,\d+(?::\d+)?)*)\}))+
    regex = r'(?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\d+(?:,\d+)*|\d+-\d+)\})|(?:\^\{(?P<controls>\d+(?:,\d+)*|\d+-\d+)\}))+'
    results = re.findall(regex, text)
    split_string_by_char = lambda string, char: list(map(int, string.split(char)))

    self.operations = []
    for gate_name, targets, controls in results:
      if '-' in targets:
        first_target, last_target = split_string_by_char(targets, '-')
        targets = list(range(first_target, last_target + 1))
      else:
        targets = split_string_by_char(targets, ',')

      if len(controls) > 0:
        if '-' in controls:
          first_control, last_control = split_string_by_char(controls, '-')
          controls = list(range(first_control, last_control + 1))
        else:
          controls = split_string_by_char(controls, ',')
      else:
        controls = []

      gate = gates[gate_name](targets, controls)
      self.operations.append(gate)

    return self.operations
