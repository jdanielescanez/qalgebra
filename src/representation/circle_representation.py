# Import math libraries
import numpy as np
import cmath
from math import sin, cos, pi, sqrt, log

# Import graphical representation libraries
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

# See: https://stackoverflow.com/questions/44970010/
#          axes-class-set-explicitly-size-width-height-of-axes-in-given-units
# Used to set the ax size
def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

# See: https://gist.github.com/LyleScott/e36e08bfb23b1f87af68c9051f985302
# Used to rotate the phase in the circle
def rotate(origin, point, radians):
    x, y = point
    ox, oy = origin

    qx = ox + cos(radians) * (x - ox) + sin(radians) * (y - oy)
    qy = oy - sin(radians) * (x - ox) + cos(radians) * (y - oy)

    return qx, qy

# Represents a statevector using the Circle Notation
class CircleNotation:
    # Constructor
    def __init__(self, statevector):
        self.SCALE = 1
        self.statevector = np.asarray(statevector)
    
    # Draw one circle in its ax using its radius, phase and tag
    def draw_circle_in_ax(self, radius, phase, tag, ax):
        # Initial configuration of ax and variables
        origin = [0, 0]
        set_size(2 * len(self.statevector), 2 * len(self.statevector), ax)
        ax.set_xlim((- 1.25 * self.SCALE, 1.25 * self.SCALE))
        ax.set_ylim((- 1.25 * self.SCALE, 1.1 * self.SCALE))
        ax.axis('off')
        ax.set_aspect('equal', adjustable='box')
        
        # Draw the inner circle if the radius is not zero
        if radius != 0:
            color_hsv = (((2*pi + phase) % (2*pi)) / (2*pi), radius, 0.75)
            color_rgb = mpl.colors.hsv_to_rgb(color_hsv)
            circle = plt.Circle(origin, radius=radius * self.SCALE, color=color_rgb)
            new_point = rotate(origin, [origin[0] + self.SCALE, origin[1]], 2 * pi - phase)
            ax.plot([origin[0], new_point[0]], [origin[1], new_point[1]], color='black')
            ax.add_patch(circle)
            
        # Draw the outer circle
        circle_base = plt.Circle(origin, radius=self.SCALE, color='black', fill=False)
        ax.add_patch(circle_base)
        
        # Draw the tag below the circle
        ax.text(origin[0] + 0.1 * self.SCALE, origin[1] - 1.6 * self.SCALE, r'$|' + tag + r'\rangle$', \
                color="black", fontsize=30, horizontalalignment='center')
    
    # Prints the statevector using the Circle Notation
    def paint(self):
        # Uses as many circles as there are elements in the state vector
        fig, ax_v = plt.subplots(ncols=len(self.statevector))
        # Calculates the tag format depending of the statevector size
        tag_format = '0' + str(int(log(len(self.statevector), 2))) + 'b'
            
        # For each state in statevector, draw its circle computing its radius and phase
        for index, state in enumerate(self.statevector):
            radius, phase = cmath.polar(state)
            self.draw_circle_in_ax(radius, phase, format(index, tag_format), ax_v[index])

        # Prints all drawn circles
        plt.show()

# Prints the statevector using the Circle Notation
def paint_circle_notation(statevector):
    circles_notation = CircleNotation(statevector)
    circles_notation.paint()
