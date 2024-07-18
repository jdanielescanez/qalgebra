
from src.entities.qstate import QState
from src.entities.qcircuit import QCircuit
from src.io.parser import Parser
from src.io.writer import Writer
from src.entities.execution import Execution
from src.entities.converter import Converter
from src.representation.circle_representation import paint_circle_notation
from src.io.rule_parser import RuleParser
from src.optimizer.optimizer import RuleApplier


class QAlgebra:
  def __init__(self):
    self.qstate = None
    self.operations = []

    self.parser = Parser(0)
    self.writer = Writer()
    self.execution = Execution()
    self.converter = Converter()

  def print_header(self):
    pass # TODO

  def print_title(self):
    Q_ALGEBRA = 'QAlgebra'
    print('\n' + Q_ALGEBRA)
    print('=' * len(Q_ALGEBRA) + '\n')

  def run(self):
    self.print_header()
    try:
      while True:
        self.print_title()
        self.print_menu()
        self.run_option()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting the program.")  

  def print_menu(self):
    print('[1] Set size')
    print('[2] Set to zero state')
    print('[3] Apply gates')
    print('[4] Print current circuit')
    print('[5] Plot circle notation')
    print('[6] Print latex workout')
    print('[7] Print qiskit circuit code')
    print('[8] Optimize circuit (Work in progress...)')

    print('[0] Exit\n')

  def run_option(self):
    switch = { # TODO ARRAY in constructor. Array of (help, function)
      0: exit,
      1: self.set_size,
      2: self.reset,
      3: self.apply_gate,
      4: self.print_circuit,
      5: self.plot_circle_notation,
      6: self.write_latex_workout,
      7: self.print_qiskit_circuit,
      8: self.optimize_circuit,
    }

    try:
      option = int(input('[&] Option: '))
      if not option in switch.keys():
        raise '[!] Not valid option'
    except Exception as e:
      print(e)
      return

    switch[option]()

  def set_size(self):
    try:
      size = int(input('[&] Size: '))
      if size < 0:
        raise '[!] Not valid size (it must be >= 0)'
    except Exception as e:
      print(e)
      return
    
    self.qstate = QState(size)
    self.parser.size = size
    self.reset()

  def reset(self):
    self.qstate.reset()
    self.operations = []

  def apply_gate(self):
    expression = input('[&] Write the gates: ')
    try:
      operations = self.parser.run(expression)
      self.qstate = self.execution.run(self.qstate, operations)
      self.operations += operations
      print('[#] Operations:', self.writer.get_operations_string(self.operations, self.qstate.size))
      print('[#] Current state:', self.qstate)
    except Exception as e:
      print('[!] Not valid expression -', e)

  def print_circuit(self):
    try:
      print(QCircuit(self.operations, self.qstate.size))
    except Exception as e:
      print('[!] Error printing circuit', e)

  def plot_circle_notation(self):
    try:
      paint_circle_notation(self.qstate.state)
    except Exception as e:
      print('[!] Error ploting circle notation', e)

  def write_latex_workout(self):
    filename = input('[&] Write the file name: ')
    self.writer.run(self.operations, self.qstate.size, filename)
    print(f'[#] Check ./examples/output/{filename}.tex and ./examples/output/{filename}.pdf')

  def print_qiskit_circuit(self):
    print(self.converter.to_qiskit(QCircuit(self.operations, self.qstate.size)))

  def optimize_circuit(self):
    filename = input('[&] Write the rules file name: ')
    print('Reading file...')
    RuleParser(filename)
    print('Optimizing...')
    
