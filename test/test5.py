
import sys

sys.path.append('.')

from src.representation.circle_representation import paint_circle_notation

from src.io.parser import Parser
from src.entities.execution import Execution
from src.entities.qstate import QState

parsed_instructions = Parser().run('H_{0-1}X_{1}')
execution = Execution()
qstate = execution.run(QState(2), parsed_instructions)
paint_circle_notation(qstate.state)
print(qstate)
