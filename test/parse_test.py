
import sys

sys.path.append('.')

from src.latex.parser import Parser

parsed_instructions = Parser().run('H_{0,2,3}^{1}X^{0}_{1}')

for instruction in parsed_instructions:
  print(instruction)
