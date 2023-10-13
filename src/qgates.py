
from src.qgate import QGate
from sympy import sqrt

class Identity(QGate):
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

class Hadamard(QGate):
  def __init__(self, *conf) -> None:
    super().__init__([[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]], *conf)
