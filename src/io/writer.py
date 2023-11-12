
import os  
from copy import copy

from src.entities.execution import Execution
from src.entities.qstate import QState
from pdflatex import PDFLaTeX

class Writer:
  def get_latex(self, operations, size):
    operations_copy = copy(operations)
    text = """
    \\documentclass{article}

    \\usepackage{amsmath}

    \\title{Example}
    \\author{Daniel Escanez-Exposito}
    \\date{2023}

    \\begin{document}

    \\maketitle

    \\section{Exercise}
    $
    """

    text += self.format_operations(operations_copy, size)
    
    text += """
    $
    \\end{document}
    """

    return text

  def run(self, operations, size, filename: str='out'):
    tex_path = f'./examples/output/{filename}.tex'
    pdf_path = f'./examples/output/{filename}.pdf'

    f = open(tex_path, 'w')
    text = self.get_latex(operations, size)
    f.write(text)
    f.close()

    pdfl = PDFLaTeX.from_texfile(tex_path)
    pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
    os.system(f'mv {pdf_path.split("/")[-1]} {pdf_path}')

  def get_operations_string(self, operations, size):
    return ''.join([op.get_formatted_string(size) for op in operations])
  
  def format_operations(self, operations, size):
    execution_engine = Execution()
    qstate = QState(size)
    
    text = qstate.to_latex()
    text += self.get_operations_string(operations, size) + '\\\\ \\\\ \n'
    while len(operations) > 0:
      qstate = execution_engine.step(qstate, operations)
      text += '= [' + qstate.to_latex() + ']'
      text += self.get_operations_string(operations, size) + '\\\\ \\\\ \n'
    return text[:-4]
