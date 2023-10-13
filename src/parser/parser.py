
from src.qgates import gates

class Parser:
  def __init__(self):
    self.operations = []

  def run(self, text: str) -> list:
    while text != '':
      text = self.parseGate(text)
    return self.operations

  def parseGate(self, text: str) -> str:
    gate_name, text = self.extractGate(text)

    text = self.parseArgs(gate_name, text)
    return text

  def extractGate(self, text: str):
    gate_name = ''
    while text[0] != '^' and text[0] != '_':
      gate_name, text = gate_name + text[0], text[1:]
    
    return gate_name, text
           

  def parseArgs(self, gate_name: str, text: str) -> str:
    controls = []
    while text != '' and (text[0] == '^' or text[0] == '_'):
      if text[0] == '_':
        text = text[2:] # remove ^{
        args = text.split('}')[0] # get args
        targets = list(map(int, args.split(',')))
        text = text[len(args) + 1:] # remove args and }

      if text[0] == '^':
        text = text[2:] # remove ^{
        args = text.split('}')[0] # get args
        controls = list(map(int, args.split(',')))
        text = text[len(args) + 1:] # remove args and }
    
    gate = gates[gate_name](targets, controls)
    self.operations.append(gate)
    return text
