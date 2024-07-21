import re
from typing import List
from src.entities.rule_gate import RuleGate
from src.entities.rule import Rule

class RuleApplier:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def get_indexes_to_apply(self, expression: List[RuleGate], left: List[RuleGate], indexes: List[int]):
        for i in range(len(left)):
            expression_names = list(map(lambda x: x.name, expression))
            try:
                pre_index = indexes[i]
                indexes[i] = expression_names.index(left[i].name, pre_index)
                print(indexes[i], i)
                if pre_index != indexes[i]:
                    for j in range(i, len(indexes)):
                        print(i, j, indexes)
                        indexes[j] = indexes[j - 1] + 1
            except ValueError:
                return None
        print(indexes)
        return indexes

    def apply_rule(self, expression: List[RuleGate], rule: Rule) -> List[RuleGate]:
        new_expression = expression.copy()

        left = rule.left
        indexes = [0] * len(left)
        while True:
            indexes = self.get_indexes_to_apply(expression, left, indexes)
            if indexes == None:
                return new_expression
            

            indexes[-1] += 1
            for j in range(len(indexes)):
                if indexes[len(indexes) - j - 1] == len(expression) - j:
                    indexes[len(indexes) - j - 1] -= len(expression) - j
                    print(j)
                    if j != len(indexes) - 1:
                        indexes[len(indexes) - j - 2] += 1
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