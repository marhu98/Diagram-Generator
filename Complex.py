import numpy as np
import drawSvg as draw

        

class Complex(object):
    
    def __init__(self,height=100,width=100,origin=(0,0),diam=5):
        #self.chains = []
        self.dims = {}
        self.diff = []
        self.height = height
        self.width = width
        
        self.origin = (origin[0],origin[1]-0.1*height)
        self.diam = diam
        
    def add(self,dim,n=1):
        #self.chains.append(Chain(dim))
        if dim not in self.dims.keys():
            self.dims[dim]=n
        else:
            self.dims[dim]+=n
        
    def add_diff(self,dim, index_1, coefs):
        assert dim != 0
        if index_1 >= self.dims[dim]: #or index_2 == self.dims[dim-1]:
            #This means that there are not enough generators
            print("Wrong generators")
            return None
        else:
            self.diff.append({"0":(dim,index_1),"coefs":coefs})
            
    """
    Returns the differential of the matrix
    """        
    def diff_matrix(self):
        pass
    
    
    """
    Return the dimensions of each of the chain groups,
    sorted by dimension. 
    Also sorts the internal dimension dictionary
    """
    def dim_sorted(self):
        values = sorted(self.dims)
        res = {}
        
        for val in values:
            res[val]=self.dims[val]
        self.dims = res
        return res
            
    def __str__(self):
        return str(self.dims) + "\n" + str(self.diff)
     
    def draw(self,save = False, retEls = False,off = (0,0)):
        els = []
        

        d = draw.Drawing(1.2*self.width, 1.2*self.height, origin=self.origin)
        
        self.dim_sorted()
        
        hstep = self.width/len(self.dims)
        
        for i in range(len(self.dims)):
        
            l = draw.Line(off[0]+self.width-i*hstep,off[1]+0,
                          off[0]+self.width-i*hstep,off[1]+self.height,stroke="black",
                          stroke_width=2,fill=None)
        
            els.append(l)
    
    
        for dim,count in self.dims.items():
            for i in range(count):
                vstep = self.height/count
                c = draw.Circle(off[0]+self.width-dim*hstep,
                                off[1]+vstep*i,self.diam,
                               fill="blue",stroke_width=2,stroke="black")
                els.append(c)
                
        for dif in self.diff:
            base = dif["0"]
            coefs = dif["coefs"]
            vstep = self.height/self.dims[base[0]]
            baseCoor = (off[0]+self.width-base[0]*hstep, off[1]+vstep*base[1])
            
            middle = lambda x,y: (x[0]/2+y[0]/2,x[1]/2+y[1]/2+10)
            
            for gen, coef in coefs.items():
                vstep = self.height/self.dims[base[0]-1]
                endCoor = (off[0]+self.width-(base[0]-1)*hstep, off[1]+vstep*gen)
                l = draw.Line(*baseCoor,*endCoor,stroke="grey",stroke_width=1,fill=None)
                
                els.append(l)
                
                p = draw.Path(stroke_width=2, stroke='lime',
                fill='black', fill_opacity=0.2)
                p.M(*baseCoor)  # Start path at point (-10, 20)
                p.L(*endCoor)  # Draw a curve to (70, 20)
                        
                if coef != 1:    
                    text = draw.Text(str(coef), 12, *middle(baseCoor,endCoor), text_anchor='start', valign='middle')    

                    els.append(text)

        if retEls:
            return els
        else:
            for el in els:
                d.append(el)
        return d
