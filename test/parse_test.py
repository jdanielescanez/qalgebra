
import sys

sys.path.append('.')

from src.parser.parser import Parser

parsed_instructions = Parser().run('H_{0,2,3}^{1}')

for instruction in parsed_instructions:
  print(instruction)
