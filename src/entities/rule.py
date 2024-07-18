from typing import List, Tuple, Set

class Rule:
    def __init__(self, patron: List[Tuple[str, str]], resultado: Tuple[str, str, str]):
        self.patron = patron
        self.resultado = resultado

    def __repr__(self):
        return f"Rule(pattern={self.patron}, result={self.resultado})"