import numpy as np
import drawSvg as draw
from Complex import Complex
from Filtration import Filtration

        
a = Complex()
a.add(0,2)
a.add(1,2)
a.add(2,3)
a.add_diff(1,0,{0:1,1:-1})
a.add_diff(2,1,{1:1})
print(a)

b = Complex()

b.add(0,1)
b.add(1,2)
b.add_diff(1,1,{0:3})

d = a.draw()
d.saveSvg("images/draw.svg")

f = Filtration()
f.add_level(0,a)
f.add_level(1,b,update=True)
f.draw().saveSvg("images/drawFiltered.svg")
