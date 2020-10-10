# -*- coding: utf-8 -*-
import rhinoscriptsyntax as rs
from Line import *
from Node import *
import random

########################################################################
#ParallelLine Class
########################################################################
class ParallelLine():
    def __init__(self,no,angle,offset,dis,lineNum):
        self.no=no              #平行線の種類
        self.angle=angle        #角度
        self.dis=dis            #間隔
        self.len=70             #ラインの長さ
        self.lines=[]           #Line[] ラインのインスタンス
        self.offset=offset      #-self.dis/2.0からself.dis/2.0まで
        self.lineNum=lineNum    #ラインの本数
        
        self.setLine()
    
        
    def setLine(self):
        for i in range(int(self.lineNum)):
            # sPt=[-self.len/2.0, -self.dis*(self.lineNum-1)/2.0+self.dis*i+self.offset, 0]
            # ePt=[ self.len/2.0, -self.dis*(self.lineNum-1)/2.0+self.dis*i+self.offset, 0]
            sPt = [-self.len / 2.0, -self.dis * (self.lineNum - 1) / 2.0 + self.dis * i + self.offset, 0]
            ePt = [self.len / 2.0, -self.dis * (self.lineNum - 1) / 2.0 + self.dis * i + self.offset, 0]

            sPt=rs.VectorRotate(sPt, self.angle, [0,0,1])
            ePt=rs.VectorRotate(ePt, self.angle, [0,0,1])
            line=Line(self.no,      #int lineの種類番号 1<=no<=6
                      i,            #int 同じ種類の中で何番目か
                      sPt,          #[x,y,z] 始点(描画には使わない。ベクトル用)
                      ePt,          #[x,y,z] 終点(描画には使わない。ベクトル用)
                      self.angle)   #float 0<=angle<180
            self.lines.append(line)
        
    def setIntersectParallelLines(self,parallelLines,nodes):
        for parallelLine in parallelLines:
            if(self.no==parallelLine.no):continue
            for myLine in self.lines:
                for yourLine in parallelLine.lines:
                    pts = rs.LineLineIntersection([myLine.sPt,myLine.ePt], [yourLine.sPt,yourLine.ePt])
                    if pts is not None:
                        node = Node(pts[0],[myLine,yourLine])
                        node=self.checkNodes(node,nodes)
                        myLine.nodes.append(node)
                    
    def checkNodes(self,node,nodes):
        tmp=None
        for n in nodes:
            if(n.checkEqual(node.pt)):
                tmp=n
                break
        if(tmp==None):
            tmp=node
            nodes.append(node)
        return tmp
        
            
        