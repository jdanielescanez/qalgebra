
from src.entities.rule import Rule
from src.entities.rule_gate import RuleGate
import re

class RuleParser:
    def __init__(self, filename: str) -> None: 
        self.rule_list = self.read_file_to_list(filename)

    def parse_rule(self, rule: str) -> Rule:
        pattern = re.compile(r'(?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\\?[a-z]+(?::\\?[a-z]+)?(?:,\\?[a-z]+)*)\})|(?:\^\{(?P<controls>\\?[a-z]+(?::\\?[a-z]+)?(?:,\\?[a-z]+)*)\}))+')
        parts = rule.split('=')
        left_part, right_part = list(map(lambda elem: elem.strip(), parts))

        left_matches = pattern.findall(left_part)
        right_matches = pattern.findall(right_part)

        if not right_matches:
            raise ValueError(f"Invalid rule format: {rule}")

        left, right = list(map(lambda x: [RuleGate(name, sub, super) for name, sub, super in x], [left_matches, right_matches]))
        
        return Rule(left, right)

    def get_rule_list(self):
        return self.rule_list
    
    def read_file_to_list(self, filename):
        """
        Reads the content of a file and stores each non-empty, non-comment line as an element in a list.

        Args:
            filename (str): The path to the file to be read.

        Returns:
            list: A list of strings, each representing a line from the file.
        """
        rules = []

        try:
            with open(filename, 'r') as file:
                for line in file:
                    # Remove leading/trailing whitespace
                    line = line.strip()
                    # Ignore empty lines and comments (lines starting with #)
                    if line and not line.startswith('#'):
                        rules.append(self.parse_rule(line))
        except FileNotFoundError:
            print(f"[Error] File '{filename}' not found.")
        except IOError as e:
            print(f"[Error] An I/O error occurred: {e}")

        return rules
