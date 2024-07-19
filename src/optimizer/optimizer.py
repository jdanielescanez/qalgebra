import re
from typing import List
from src.entities.rule_gate import RuleGate
from src.entities.rule import Rule

class RuleApplier:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def apply_rule(self, expression: List[RuleGate], rule: Rule) -> List[RuleGate]:
        new_expression = []
        i = 0
        while i < len(expression):
            match_found = False
            if i <= len(expression) - len(rule.left):
                match = True
                targets = None
                controls = {}
                for j, gate_left in enumerate(rule.left):
                    gate = expression[i + j]
                    if gate.__class__.__name__ != gate_left.tag:
                        match = False
                        break
                    if targets is None:
                        targets = gate.targets
                    elif targets != gate.targets:
                        match = False
                        break
                    if super not in controls:
                        controls[super] = gate.controls
                    else:
                        if controls[super] != gate.controls:
                            match = False
                            break
                if match:
                    result_targets = targets
                    result_controls = set()
                    for key in rule.resultado[2].split('+'):
                        result_controls.update(controls[key])
                    new_gate = RuleGate(rule.resultado[0], result_targets, result_controls)
                    new_expression.append(new_gate)
                    i += len(rule.left)
                    match_found = True
            if not match_found:
                new_expression.append(expression[i])
                i += 1
        return new_expression

    def apply_rules(self, expression: List[RuleGate]) -> List[RuleGate]:
        while True:
            new_expression = expression
            for rule in self.rules:  # Apply all rules
                new_expression = self.apply_rule(new_expression, rule)
            if new_expression == expression:  # No rule was applied, we are done
                break
            expression = new_expression
        return expression