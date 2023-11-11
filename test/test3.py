
import sys

sys.path.append('.')

from src.entities.qstate import QState
from src.entities.qgates import *
from src.representation.circle_representation import paint_circle_notation

qstate = QState(3)
print(qstate)

q1 = H([1]).apply(qstate)
print(q1)

q2 = X([2]).apply(q1)
print(q2)

paint_circle_notation(q2.state)
