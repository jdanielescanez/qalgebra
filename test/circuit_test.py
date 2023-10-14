

import sys

sys.path.append('.')

from src.latex.parser import Parser
from src.qcircuit import QCircuit

parsed_instructions = Parser().run('H_{0,1,2,3}X_{1,2,3}Z_{1}^{2,3}X_{1,2,3}H_{1,2,3}X_{0}^{1,2}X_{0}^{1,3}H_{0,1,2,3}X_{0}')
qc = QCircuit(parsed_instructions, 4)

print(qc)
