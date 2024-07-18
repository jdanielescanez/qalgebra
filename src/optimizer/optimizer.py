import re
from typing import List
from src.entities import QGate, Rule

class RuleApplier:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def apply_rule(self, expression: List[QGate], rule: Rule) -> List[QGate]:
        new_expression = []
        i = 0
        while i < len(expression):
            match_found = False
            if i <= len(expression) - len(rule.patron):
                match = True
                subindices = None
                superindices = {}
                for j, (nombre, sub, super) in enumerate(rule.patron):
                    gate = expression[i + j]
                    if gate.nombre != nombre:
                        match = False
                        break
                    if subindices is None:
                        subindices = gate.subindices
                    elif subindices != gate.subindices:
                        match = False
                        break
                    if super not in superindices:
                        superindices[super] = gate.superindices
                    else:
                        if superindices[super] != gate.superindices:
                            match = False
                            break
                if match:
                    result_subindices = subindices
                    result_superindices = set()
                    for key in rule.resultado[2].split('+'):
                        result_superindices.update(superindices[key])
                    new_gate = QGate(rule.resultado[0], result_subindices, result_superindices)
                    new_expression.append(new_gate)
                    i += len(rule.patron)
                    match_found = True
            if not match_found:
                new_expression.append(expression[i])
                i += 1
        return new_expression

    def apply_rules(self, expression: List[QGate]) -> List[QGate]:
        while True:
            new_expression = expression
            for rule in self.rules:  # Apply all rules
                new_expression = self.apply_rule(new_expression, rule)
            if new_expression == expression:  # No rule was applied, we are done
                break
            expression = new_expression
        return expression