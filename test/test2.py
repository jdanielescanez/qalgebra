
import sys

sys.path.append('.')

from src.entities.qstate import QState
from src.entities.qgates import *

qstate = QState(3)
print(qstate)

q1 = H([1]).apply(qstate)
print(q1)

q2 = X([2]).apply(q1)
print(q2)
