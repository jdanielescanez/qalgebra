
from sympy import re, im
from sympy.printing.latex import latex

class QState:
  def __init__(self, size: int) -> None:
    self.size = size
    self.all_zero()
    self.state[0] = complex(1)
    self.tags = list(map(lambda i: '{0:b}'.format(i).zfill(self.size), list(range(2 ** self.size))))
    self.reversed_tags = list(map(lambda x: x[::-1], self.tags))

  def all_zero(self) -> None:
    self.state = [complex(0)] * 2 ** self.size
    
  def __format_sqrt_i(self, coefficient):
    return str(coefficient).replace('sqrt', '√').replace('*I', 'ⅈ')
  
  def __is_complex(self, number):
    return type(number) == complex or ('sympy' in str(type(number)) and im(number) != 0)

  def __str__(self) -> str:
    string = ''
    for i, coefficient in enumerate(self.state):
      if coefficient != 0:
        sign = '' if self.__is_complex(coefficient) else ('-' if coefficient < 0 else '+')
        formated_coefficient = coefficient if self.__is_complex(coefficient) else abs(coefficient)
        formated_coefficient = (' ' + self.__format_sqrt_i(formated_coefficient)) if formated_coefficient != 1 else ''
        
        string += sign + formated_coefficient + ' |' + self.tags[i] + '> '
    return string

  def to_latex(self) -> str:
    latex_str = ''
    for i, coefficient in enumerate(self.state):
      if coefficient != 0:
        formated_coefficient = latex(coefficient) if coefficient != 1 else ''
        sign = '+' if coefficient != 1 and not formated_coefficient[0] in ['+', '-'] else ''
        latex_str += sign + formated_coefficient + ' |' + self.tags[i] + '\\rangle '
    return latex_str[1:]
