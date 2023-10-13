
from ..src.qstate import QState
from ..src.qgates import *


qstate = QState(3)
print(qstate)

q1 = Hadamard([1]).apply(qstate)
print(q1)

q2 = X([2], []).apply(q1)
print(q2)
