
import sys

sys.path.append('.')

from src.representation.circle_representation import paint_circle_notation

from src.latex.parser import Parser
from src.qcircuit import QCircuit
from src.execution import Execution

parsed_instructions = Parser().run('H_{0,1,2,3}X_{1,2,3}Z_{1}^{2,3}X_{1,2,3}H_{1,2,3}X_{0}^{1,2}X_{0}^{1,3}H_{0,1,2,3}X_{0}')
execution = Execution(parsed_instructions, 4)
qstate = execution.run()
paint_circle_notation(qstate.state)
