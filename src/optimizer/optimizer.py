import re
from typing import List
from src.entities.rule_gate import RuleGate
from src.entities.rule import Rule
from functools import reduce

class RuleApplier:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def get_indexes_to_apply(self, expression: List[RuleGate], left: List[RuleGate], indexes: List[int]):
        for i in range(len(left)):
            expression_names = list(map(lambda x: x.name, expression))
            try:
                pre_index = indexes[i]
                indexes[i] = expression_names.index(left[i].name, pre_index)
                if pre_index != indexes[i]:
                    for j in range(i, len(indexes)):
                        indexes[j] = indexes[j - 1] + 1
            except ValueError:
                return None
        return indexes

    def apply_rule(self, expression: List[RuleGate], rule: Rule) -> List[RuleGate]:
        new_expression = expression.copy()

        left = rule.left
        indexes = [0] * len(left)
        while True:
            indexes = self.get_indexes_to_apply(expression, left, indexes)
            if indexes == None:
                return new_expression
            
            set_names = reduce(lambda x, y: x.union(y), [set(x.targets).union(set(x.controls)) for x in left])
            dic_names = {k: [] for k in set_names}
            aux_expression = list(map(new_expression.__getitem__, indexes))
            for name in set_names:
                for rule_gate, gate in zip(left, aux_expression):
                    if name in rule_gate.targets:
                        dic_names[name].append(gate.targets)
                    if name in rule_gate.controls:
                        dic_names[name].append(gate.controls)
            dic_names = {k: set(reduce(lambda x, y: set(x).intersection(set(y)), dic_names[k])) for k in set_names}

            if all([len(dic_names[k]) > 0 for k in set_names]):
                for i in indexes[::-1]:
                    del new_expression[i]

                origin = indexes[0]
                right = rule.right

                for i, rule_gate in enumerate(right):
                    new_expression.insert(origin + i, rule_gate.get_gate_by_dic(dic_names))

            indexes[-1] += 1
            for j in range(len(indexes)):
                real_index = len(indexes) - j - 1
                if indexes[real_index] == len(expression) - j:
                    indexes[real_index] -= len(expression) - j
                    if real_index != 0:
                        indexes[real_index - 1] += 1
                    else:
                        return new_expression

    def apply_rules(self, expression: List[RuleGate]) -> List[RuleGate]:
        new_expression = expression.copy()
        while True:
            for rule in self.rules: # Apply all rules
                new_expression = self.apply_rule(new_expression, rule)
            if new_expression == expression: # No rule was applied, we are done
                break
            expression = new_expression.copy()
        return new_expression