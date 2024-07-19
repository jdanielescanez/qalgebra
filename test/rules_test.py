
import sys, readline
sys.path.append('.')


from src.entities.qstate import QState
from src.representation.circle_representation import paint_circle_notation
from src.io.rule_parser import RuleParser
from src.optimizer.optimizer import RuleApplier


### Para linux
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
###

#mpl.rcParams.update(mpl.rcParamsDefault)

from src.qalgebra import QAlgebra

qalgebra = QAlgebra()
size = 2
expression = 'H_{1,2}X_{2}^{1}H_{1,2}'

qalgebra.qstate = QState(size)
qalgebra.parser.size = size
qalgebra.operations = qalgebra.parser.run(expression)

rule_parser = RuleParser('rules/rule01.rq')
rules = rule_parser.get_rule_list()
print(rules)

rule_applier = RuleApplier(rules)
optimized_operations = rule_applier.apply_rules(qalgebra.operations)
optimized_operations_str = qalgebra.writer.get_operations_string(optimized_operations, size)
print(optimized_operations_str)
