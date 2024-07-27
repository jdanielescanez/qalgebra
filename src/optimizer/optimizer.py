import re
from typing import List
from src.entities.qgate import QGate
from src.entities.rule_gate import RuleGate
from src.entities.rule import Rule
from functools import reduce

class RuleApplier:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def get_indexes_to_apply(self, expression: List[RuleGate], left: List[RuleGate], indexes: List[int]):
        new_indexes = indexes.copy()
        for i in range(len(left)):
            expression_names = list(map(lambda x: x.name, expression))
            try:
                pre_index = new_indexes[i]
                new_indexes[i] = expression_names.index(left[i].name, pre_index)
                if pre_index != new_indexes[i]:
                    for j in range(i + 1, len(new_indexes)):
                        new_indexes[j] = new_indexes[j - 1] + 1
                # TODO: Check if there is some ilegal index inside the indexes window
            except ValueError:
                return None
        return new_indexes

    def next_indexes(self, indexes, new_expression):
        new_indexes = indexes.copy()
        new_indexes[-1] += 1
        for j in range(len(new_indexes)):
            real_index = len(new_indexes) - j - 1
            if new_indexes[real_index] == len(new_expression) - j:
                new_indexes[real_index] -= len(new_expression) - j
                if real_index != 0:
                    new_indexes[real_index - 1] += 1
                else:
                    return None
        
        return new_indexes

    def apply_rule(self, expression: List[QGate], rule: Rule) -> List[QGate]:
        new_expression = expression.copy()

        left = rule.left
        indexes = [0] * len(left)
        while True:
            indexes = self.get_indexes_to_apply(new_expression, left, indexes)
            if indexes == None:
                return new_expression
            
            set_names = reduce(lambda x, y: x.union(y), [set(x.targets).union(set(x.controls)) for x in left])
            dic_names = {k: [] for k in set_names}
            aux_expression = list(map(new_expression.__getitem__, indexes))
            for i, gate in enumerate(aux_expression):
                if len(left[i].controls) == 0 and len(gate.controls) != 0:
                    indexes = self.next_indexes(indexes, new_expression)
                    if indexes == None:
                        return new_expression
                    break; continue

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

                # for i, rule_gate in enumerate(right):
                #     gate_in = rule_gate.get_gate_by_dic(dic_names)
                #     if gate_in.name != 'I':
                #         new_expression.insert(origin + i, gate_in)

            indexes = self.next_indexes(indexes, new_expression)
            if indexes == None:
                return new_expression

    def apply_rules(self, expression: List[QGate]) -> List[QGate]:
        new_expression = expression.copy()
        while True:
            for rule in self.rules: # Apply all rules
                aux_expression = new_expression.copy()
                while True:
                    new_expression = self.apply_rule(new_expression, rule)
                    if aux_expression == new_expression:
                        break
                    aux_expression = new_expression.copy()
            if new_expression == expression: # No rule was applied, we are done
                break
            expression = new_expression.copy()
        return new_expression