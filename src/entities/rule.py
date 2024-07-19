from typing import List, Tuple, Set
from src.entities.rule_gate import RuleGate

class Rule:
    def __init__(self, left: List[RuleGate], right: List[RuleGate]):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{''.join(map(str, self.left))} => {''.join(map(str, self.right))}"