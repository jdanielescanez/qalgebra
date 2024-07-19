
import re

from src.entities.qgates import gates

RANGE_SEPARATOR = ':'

class Parser:
  def __init__(self, size):
    self.operations = []
    self.size = size

  def index_map(self, index_str):
    return self.size - int(index_str)

  def run(self, text: str) -> list:
    regex = r'(?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\d+(?::\d+)?(?:,\d+(?::\d+)?)*)\})|(?:\^\{(?P<controls>\d+(?::\d+)?(?:,\d+(?::\d+)?)*)\}))+'
    results = re.findall(regex, text)
    split_string_by_char = lambda string, char: list(map(self.index_map, string.split(char)))

    self.operations = []
    for gate_name, targets, controls in results:
      if RANGE_SEPARATOR in targets:
        first_target, last_target = split_string_by_char(targets, RANGE_SEPARATOR)
        targets = list(range(first_target, last_target + 1))
      else:
        targets = split_string_by_char(targets, ',')

      if len(controls) > 0:
        if RANGE_SEPARATOR in controls:
          first_control, last_control = split_string_by_char(controls, RANGE_SEPARATOR)
          controls = list(range(first_control, last_control + 1))
        else:
          controls = split_string_by_char(controls, ',')
      else:
        controls = []

      targets.sort()
      controls.sort()
      gate = gates[gate_name](targets, controls)
      self.operations.append(gate)

    return self.operations
