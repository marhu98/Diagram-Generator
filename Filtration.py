class Filtration:
    def __init__(self,height=100,width=100):
        self.subs = {}
        self.levels = []
        
        self.height = height
        self.width = width
        
    def add_level(self, level, comp):
        if len(self.levels)>0 and level <= max(self.levels):
            return "Error, please insert the filtrations in order"
        self.levels.append(level)
        self.subs[level]= comp
        
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
