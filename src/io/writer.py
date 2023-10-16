


class Writer:
  def __init__(self, execution_engine):
    self.execution_engine = execution_engine

  def run(self, filename: str='./examples/output/out.tex'):
    f = open(filename, 'w')

    text = """
    \\documentclass{article}

    \\usepackage{amsmath}
    \\usepackage{autobreak}

    \\title{Example}
    \\author{Daniel Escanez-Exposito}
    \\date{2023}

    \\begin{document}

    \\maketitle

    \\section{Exercise}
    \\begin{autobreak}
    """

    text += self.format_operations()
    
    text += """
    \\end{autobreak}
    \\end{document}
    """

    f.write(text)
    f.close()

  def format_operations(self):
    text = ''.join([str(op) for op in self.execution_engine.operations])
    text += self.execution_engine.qstate.to_latex() + '\\\\ \\\\ \n'
    while len(self.execution_engine.operations) > 0:
      self.execution_engine.step()
      text += '=' + ''.join([str(op) for op in self.execution_engine.operations])
      text += '[' + self.execution_engine.qstate.to_latex() + ']\\\\ \\\\ \n'
    return text[:-4]
