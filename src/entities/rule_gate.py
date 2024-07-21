
class RuleGate():
  def __init__(self, name: str, targets: list, controls: list=[]) -> None:
    self.name = name
    self.targets = targets.split(',')
    self.controls = controls
    if self.controls:
      self.controls = self.controls.split(',')
    else:
      self.controls = []

  def __repr__(self):
    return f"{self.name}_{{{','.join(self.targets)}}}" + (f"^{{{','.join(self.controls)}}}" if self.controls else '')