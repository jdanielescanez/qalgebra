
import sys

sys.path.append('.')

from src.io.writer import Writer
from src.execution import Execution
from src.io.parser import Parser

parsed_instructions = Parser().run('H_{0,1,2,3}X_{1,2,3}Z_{1}^{2,3}X_{1,2,3}H_{1,2,3}X_{0}^{1,2}X_{0}^{1,3}H_{0,1,2,3}X_{0}')
execution = Execution(parsed_instructions, 4)
writer = Writer(execution)

writer.run()
