import drawSvg as draw
class Filtration:
    def __init__(self,height=100,width=100,max_dim=0):
        self.subs = {}
        self.levels = []

        self.height = height
        self.width = width

        self.max_dim=max_dim

    def add_level(self, level, comp, update=False):
        if len(self.levels)>0 and level <= max(self.levels):
            return "Error, please insert the filtrations in order"
        self.levels.append(level)

        self.subs[level]= comp

        dims = comp.dims
        keys = dims.keys()

        max_dim=max(dims.keys())
        self.max_dim=max(self.max_dim,max_dim)

        if update:

            for level,component in self.subs.items():
                print(component)
                dims = component.dims
                keys = dims.keys()
                for i in range(self.max_dim+1):
                    if i not in keys:
                        comp.add(i,0)


    def draw(self):
        count = len(self.levels)
        w = count*100+20
        h = count*100+20

        d = draw.Drawing(w+50,h,origin=(0,0))

        for i in range(count):
            cheight = i*self.height+10
            els = self.subs[i].draw(retEls=True,off=(0,cheight))
            for j in range(len(els)):
                d.append(els[j])

            l = draw.Line(0,cheight-10,self.width+50,cheight-10,stroke="black",stroke_width=0.5,fill=None)
            d.append(l)
        return d
