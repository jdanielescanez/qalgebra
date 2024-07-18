
from entities.rule import Rule
import re

class RuleParser:
    def __init__(self, filename: str) -> None: 
        self.rule_list = self.read_file_to_list(filename)

    def parse_rule(self, rule: str) -> Rule:
        pattern = re.compile(r"(\w+)_\{(\w+)\}\^\{(\w+)\}")
        parts = rule.split(' = ')
        left_part = parts[0].strip()
        right_part = parts[1].strip()

        left_matches = pattern.findall(left_part)
        right_match = pattern.match(right_part)

        if not right_match:
            raise ValueError(f"Invalid rule format: {rule}")

        result_name, result_sub, result_super = right_match.groups()

        patron = [(name, sub, super) for name, sub, super in left_matches]
        resultado = (result_name, result_sub, result_super)
        
        return Rule(patron, resultado)

    def get_rule_list(self):
        return self.rule_list
    
    def parse_rule(self, rule: str) -> Rule:
        pattern = re.compile(r"(\w+)_\{(\w+)\}\^\{(\w+)\}")
        parts = rule.split(' = ')
        left_part = parts[0].strip()
        right_part = parts[1].strip()

        left_matches = pattern.findall(left_part)
        right_match = pattern.match(right_part)

        if not right_match:
            raise ValueError(f"Invalid rule format: {rule}")

        result_name, result_sub, result_super = right_match.groups()

        patron = [(name, sub, super) for name, sub, super in left_matches]
        resultado = (result_name, result_sub, result_super)
        
        return Rule(patron, resultado)
    
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