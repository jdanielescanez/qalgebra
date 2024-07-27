
from src.entities.qgates import gates
from functools import reduce

class RuleGate():
  def __init__(self, name: str, targets: list, controls: list=[]) -> None:
    self.name = name
    self.targets = targets.split(',')
    self.controls = controls
    if self.controls:
      self.controls = self.controls.split(',')
    else:
      self.controls = []

  def get_gate_by_dic(self, parameters: dict):
    targets_list = [parameters[t_param] for t_param in self.targets]
    targets = set(reduce(lambda x, y: set(x).union(set(y)), targets_list))

    controls_list = [parameters[t_param] for t_param in self.controls]
    controls = [] if len(controls_list) == 0 else set(reduce(lambda x, y: set(x).union(set(y)), controls_list))

    return gates[self.name](targets, controls)

  def __repr__(self):
    return f"{self.name}_{{{','.join(self.targets)}}}" + (f"^{{{','.join(self.controls)}}}" if self.controls else '')
