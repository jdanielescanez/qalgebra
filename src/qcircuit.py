
class QCircuit:
  def __init__(self, operations, size):
    self.WIRE = '―'
    self.CONTROL = '●'

    self.operations = operations[::-1]
    self.size = size
    self.horizontal_wires_zone = []
    self.matrix = self.__get_matrix()

  def __get_matrix(self):
    matrix = []
    for _ in range(self.size):
      matrix.append([])

    for op in self.operations:
      indexes = op.targets + op.controls
      max_qubit = max(list(map(lambda i: len(matrix[i]), indexes)))

      for target in op.targets:
        while len(matrix[target]) - 1 < max_qubit:
          matrix[target].append(self.WIRE)
        matrix[target][max_qubit] = op.get_name()

      for control in op.controls:
        while len(matrix[control]) - 1 < max_qubit:
          matrix[control].append(self.WIRE)
        matrix[control][max_qubit] = self.CONTROL
      
      horizontal_wires_zone = list(range(min(indexes), max(indexes))) if len(op.controls) > 0 else []
      self.horizontal_wires_zone.append(horizontal_wires_zone)

    return matrix

  def __str__(self):
    qc_string = ''
    max_size = max(list(map(lambda i: len(i), self.matrix)))

    for i, qubit in enumerate(self.matrix):
      qubit_string = 'q[' + str(i) + '] ' + self.WIRE
      next_horizontals_string = ' ' * len(qubit_string)
      for j, cell in enumerate(qubit):
        qubit_string += self.WIRE + cell + self.WIRE
        horizontal_wire = '|' if i in self.horizontal_wires_zone[j] else ' '
        next_horizontals_string += ' ' + horizontal_wire + ' '

      padding = 3 * (max_size - len(qubit)) * self.WIRE
      next_horizontals_string += padding + '\n'

      qc_string += qubit_string + padding + '\n' + next_horizontals_string

    return qc_string[:-(len(next_horizontals_string) + 1)]
