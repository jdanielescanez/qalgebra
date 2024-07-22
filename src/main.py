
import sys, readline
sys.path.append('.')

### Para linux
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
###

#mpl.rcParams.update(mpl.rcParamsDefault)

from src.qalgebra import QAlgebra

qalgebra = QAlgebra() # TODO catch Ctrl + C
qalgebra.run()
