
import sys

sys.path.append('.')

from src.entities.qstate import QState
from src.entities.qgates import *

qstate = QState(2)
print(qstate)

q1 = H([0]).apply(qstate)
print(q1)

q2 = X([1], [0]).apply(q1)
print(q2)

q3 = Y([0]).apply(q2)
print(q3)
