
from src.qstate import QState

class Execution:
  def __init__(self, operations, size):
    self.operations = operations
    self.qstate = QState(size)
  
  def step(self):
    self.qstate = self.operations.pop().apply(self.qstate)
