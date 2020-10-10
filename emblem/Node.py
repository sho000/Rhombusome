# -*- coding: utf-8 -*-
import scriptcontext

########################################################################
#Node Class
########################################################################
class Node():
    def __init__(self,pt,lines):
        self.pt=pt              #[x,y,z]
        self.lines=lines        #Line[myLine,yourLine]
        self.isVisited=False    #boolean
        
        
    def lineSort(self):
        self.lines=sorted(self.lines, key=lambda x: x.no)
        
    def checkEqual(self, pt):
        tolerance = scriptcontext.doc.ModelAbsoluteTolerance
        if(self.pt[0] > pt[0]-tolerance and self.pt[0] < pt[0]+tolerance and 
           self.pt[1] > pt[1]-tolerance and self.pt[1] < pt[1]+tolerance and
           self.pt[2] > pt[2]-tolerance and self.pt[2] < pt[2]+tolerance):
            return True
        else:
            return False