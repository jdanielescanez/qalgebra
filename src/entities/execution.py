
from copy import copy

class Execution:
  def __init__(self):
    self.operations = []
    self.qstate = None
  
  def step(self, qstate, operations):
    return operations.pop(0).apply(qstate)

  def run(self, qstate, operations):
    self.qstate = copy(qstate)
    self.operations = copy(operations)
    while len(self.operations) > 0:
      self.qstate = self.step(self.qstate, self.operations)
    return self.qstate
