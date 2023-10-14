
class QCircuit:
  def __init__(self, operations, size):
    self.WIRE = '―'
    self.CONTROL = '●'

    self.operations = operations[::-1]
    self.size = size
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

    return matrix

  def __str__(self):
    qc_string = ''
    max_size = max(list(map(lambda i: len(i), self.matrix)))

    for i, qubit in enumerate(self.matrix):
      qubit_string = 'q[' + str(i) + '] ' + self.WIRE
      for cell in qubit:
        qubit_string += self.WIRE + cell + self.WIRE

      padding = 3 * (max_size - len(qubit)) * self.WIRE
      qc_string += qubit_string + padding + '\n'

    return qc_string
