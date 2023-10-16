
import re

from src.qgates import gates

class Parser:
  def __init__(self):
    self.operations = []
    self.qstate = None

  def run(self, text: str) -> list:
    regex = r'(?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\d(?:,\d)*)\})|(?:\^\{(?P<controls>\d(?:,\d)*)\}))+'
    results = re.findall(regex, text)

    for gate_name, targets, controls in results:
      targets = list(map(int, targets.split(',')))
      if len(controls) > 0:
        controls = list(map(int, controls.split(',')))
      else:
        controls = []

      gate = gates[gate_name](targets, controls)
      self.operations.append(gate)

    return self.operations
