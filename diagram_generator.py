import numpy as np
import drawSvg as draw
from Complex import Complex

        
a = Complex()
a.add(0,2)
a.add(1,2)
a.add(2,3)
a.add_diff(1,0,{0:1,1:-1})
a.add_diff(2,1,{1:1})
print(a)

d = a.draw()
d.saveSvg("draw.svg")
