# -*- coding: utf-8 -*-
import rhinoscriptsyntax as rs
import math
from System.Drawing import Color
import random


########################################################################
#Rhomboid Class
########################################################################
class Rhomboid():
    def __init__(self,no,name,angle,rotateAng,movePt,l,lines):
        self.no=no
        self.name=name              #交差しているlineとlineのナンバー「0-0」
        self.angle=angle            #ひし形の角度
        self.rotateAng=rotateAng    #頂点周りの回転角度
        self.movePt=movePt          #中心からの絶対移動距離
        self.l=l                    #辺の長さ
        self.lines=lines            #Line[]
        self.pts=[]                 #ひし形を構成する点
        self.midPts=[]              #中点
        self.ellipsePts=[]          #楕円の点、[中心、X軸の点、Y軸の点]
        
        self.setPts()       
        
    def setPts(self):
        #外周点
        pt0=[0,0,0]
        pt1=[self.l,0,0]
        pt1=rs.VectorRotate(pt1, self.angle/2.0, [0,0,1])
        pt3=[self.l,0,0]
        pt3=rs.VectorRotate(pt3, -self.angle/2.0, [0,0,1])
        pt2=rs.VectorAdd(pt1, pt3)
        self.pts.append(pt0)
        self.pts.append(pt1)
        self.pts.append(pt2)
        self.pts.append(pt3)
        
        #中点
        for i in range(len(self.pts)):
            if(i==len(self.pts)-1):
                pt=rs.VectorAdd(self.pts[i], self.pts[0])
                pt=rs.VectorDivide(pt, 2)
            else:
                pt=rs.VectorAdd(self.pts[i], self.pts[i+1])
                pt=rs.VectorDivide(pt, 2)
            self.midPts.append(pt)
            
        #楕円
        pt0=rs.VectorDivide(self.pts[2],2.0)
        l0=self.l*math.sin(math.radians(90/2.0))
        l1=self.l*math.cos(math.radians(self.angle/2.0))
        l2=self.l*math.sin(math.radians(self.angle/2.0))
        pt1=rs.VectorScale([self.l/2.0,0,0], l1/l0)
        pt1=rs.VectorAdd(pt0, pt1)
        pt2=rs.VectorScale([0,self.l/2.0,0], l2/l0)
        pt2=rs.VectorAdd(pt0, pt2)
        self.ellipsePts.append(pt0)
        self.ellipsePts.append(pt1)
        self.ellipsePts.append(pt2)
        
    def getAbsolutePt(self,pt):
        pt=rs.VectorRotate(pt, self.rotateAng,[0,0,1])
        pt=rs.VectorAdd(pt, self.movePt)
        return pt
        