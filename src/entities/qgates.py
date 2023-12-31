
from src.entities.qgate import QGate
from src.entities.measurement import M
from math import sqrt

class I(QGate):
  def __init__(self, *conf) -> None:
    super().__init__([[1, 0], [0, 1]], *conf)

class X(QGate):
  def __init__(self, *conf) -> None:
    super().__init__([[0, 1], [1, 0]], *conf)

class Y(QGate):
  def __init__(self, *conf) -> None:
    super().__init__([[0, 1j], [-1j, 0]], *conf)

class Z(QGate):
  def __init__(self, *conf) -> None:
    super().__init__([[1, 0], [0, -1]], *conf)

class H(QGate):
  def __init__(self, *conf) -> None:
    super().__init__([[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]], *conf)

gates_arr = [I, X, Y, Z, H, M]
gates = dict(zip(list(map(lambda gate: gate.__name__, gates_arr)), gates_arr))
