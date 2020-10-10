# -*- coding: utf-8 -*-
import rhinoscriptsyntax as rs
from Rhomboid import *
from Node import *
from ParallelLine import *
import math
import scriptcontext
import random

random.seed(6)
########################################################################
#Emblem Class
########################################################################
class Emblem():

    def __init__(self,
                 division=4,
                 lineNum=1,
                 l=6,
                 offsets=[],
                 distances=[]):
        """
        コンストラクタ
        :param division:
        :param lineNum:
        :param l:
        :param offsets:
        :param distances:
        """
        self.rhomboids=[]           #Rhomboidのインスタンス
        self.parallelLines=[]       #ParallelLineのインスタンス
        self.nodes=[]               #Nodeのインスタンス
        #
        self.division=division      #分割数
        self.lineNum=lineNum        #lineの本数
        self.l=l                    #菱形の一辺の長さ
        #
        self.offsets=offsets        #ParallelLineのオフセット距離のリスト
        if(len(offsets)==0):
            for i in range(int(self.division/2.0)):
                offset=random.random()*self.l*4.0-self.l*2.0
                self.offsets.append(offset)
        #
        self.distances=distances    #ParallelLineの間隔
        if(len(distances)==0):
            for i in range(int(self.division/2.0)):
                self.distances.append(self.l*2)
        self.tolerance = scriptcontext.doc.ModelAbsoluteTolerance
        
        #setParallelLines
        self.setParallelLines()
        #setIntersectParallelLines
        self.setIntersectParallelLines()
        
        #交点が2つ以上重なった場合、offsetsの値を少し増やす
        tmpList=self.checkSameNodes()
        while len(tmpList)>0:
            print(tmpList)
            for i in tmpList:
                self.offsets[i]+=self.tolerance
            self.parallelLines=[]
            self.nodes=[]
            self.setParallelLines()
            self.setIntersectParallelLines()
            tmpList=self.checkSameNodes()
        
        #setRhomboid
        self.setRhomboid(self.parallelLines[0].lines[0].nodes[0],[0,0,0])

    def setParallelLines(self):
        """
        parallelLineを生成し、parallelLinesに格納
        :return: None
        """
        for i in range(int(self.division/2.0)):
            if(self.division%4==0):
                angle = i * 360.0 / self.division + 360.0 / self.division / 2.0
            else:
                angle = i * 360.0 / self.division
            parallelLine=ParallelLine(i,                    #no
                                      angle,                #angle
                                      self.offsets[i],      #offset
                                      self.distances[i],    #distance
                                      self.lineNum)         #lineNum
            self.parallelLines.append(parallelLine)
    
    def setIntersectParallelLines(self):
        """
        parallelLines同士の交点を設定
        :return: None
        """
        #生成
        for parallelLine in self.parallelLines:
            parallelLine.setIntersectParallelLines(self.parallelLines, self.nodes)
        
        #ソート
        for parallelLine in self.parallelLines:
            for line in parallelLine.lines:
                line.nodesSort()
                
        #ソート
        for node in self.nodes:
            node.lineSort()

    def checkSameNodes(self):
        """
        checkSameNodes: 2つ以上の交点が重なるかチェック
        :return: parallelLineのリスト
        """
        list=[]
        for j,parallelLine in enumerate(self.parallelLines):
            for line in parallelLine.lines:
                for i in range(len(line.nodes)):
                    if(i<len(line.nodes)-1):
                        pt0=line.nodes[i].pt
                        pt1=line.nodes[i+1].pt
                        dis=rs.Distance(pt0, pt1)
                        if(dis<self.tolerance):
                            if(j not in list):
                                list.append(j)
        return list

    def setRhomboid(self,node,movePt):
        """
        菱形を設定
        :param node:
        :param movePt:
        :return:
        """
        #rhomboidを生成
        no=len(self.rhomboids)
        name = "%d-%d" % (node.lines[0].angle, node.lines[1].angle)
        # name="%s[%s]-%s[%s]" % (node.lines[0].no,node.lines[0].no2,node.lines[1].no,node.lines[1].no2)
        ang0=node.lines[0].angle
        ang1=node.lines[1].angle
        angle=ang1-ang0
        rotateAng=(ang0+ang1)/2.0-90
        rhomboid=Rhomboid(no,name,angle,rotateAng,movePt,self.l,node.lines)
        self.rhomboids.append(rhomboid)
        node.isVisited=True

        if(self.division==4 and self.lineNum==1):return #この場合node.linesがないのでreturn

        for line in node.lines:
            #line.nodesの中から自分の位置を取得
            myIndex=line.nodes.index(node)
            
            if(myIndex==0):
                #myIndex+1のnode
                searchNode=line.nodes[myIndex+1]
                if(searchNode.isVisited==False):
                    newNo=-1
                    newName=""
                    newAng0=searchNode.lines[0].angle
                    newAng1=searchNode.lines[1].angle
                    newAngle=newAng1-newAng0
                    newRotateAng=(newAng0+newAng1)/2.0-90
                    newRhomboid=Rhomboid(newNo,newName,newAngle,newRotateAng,[0,0,0],self.l,searchNode.lines)
                    
                    #nowLineNo
                    nowLineNo=line.no
                    
                    #prevLineNo,nextLineNo
                    prevLineNo0=node.lines[0].no
                    prevLineNo1=node.lines[1].no
                    nextLineNo0=searchNode.lines[0].no
                    nextLineNo1=searchNode.lines[1].no
                    
                    #prevDlt
                    if(nowLineNo==prevLineNo0):
                        prevDlt=prevLineNo1-nowLineNo
                    elif(nowLineNo==prevLineNo1):
                        prevDlt=prevLineNo0-nowLineNo
                        
                    #nextDlt
                    if(nowLineNo==nextLineNo0):
                        nextDlt=nextLineNo1-nowLineNo
                    elif(nowLineNo==nextLineNo1):
                        nextDlt=nextLineNo0-nowLineNo
                    
                    #++
                    if(prevDlt>0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[1])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #+-
                    elif(prevDlt>0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[1])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[3])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #-+
                    elif(prevDlt<0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #--
                    elif(prevDlt<0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[3])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    
                    self.setRhomboid(searchNode,newMovePt)
                    
            elif(myIndex==len(line.nodes)-1):
                #myIndex-1のnode
                searchNode=line.nodes[myIndex-1]
                if(searchNode.isVisited==False):
                    newNo=-1
                    newName=""
                    newAng0=searchNode.lines[0].angle
                    newAng1=searchNode.lines[1].angle
                    newAngle=newAng1-newAng0
                    newRotateAng=(newAng0+newAng1)/2.0-90
                    newRhomboid=Rhomboid(newNo,newName,newAngle,newRotateAng,[0,0,0],self.l,searchNode.lines)
                    
                    #nowLineNo
                    nowLineNo=line.no
                    
                    #prevLineNo,nextLineNo
                    prevLineNo0=node.lines[0].no
                    prevLineNo1=node.lines[1].no
                    nextLineNo0=searchNode.lines[0].no
                    nextLineNo1=searchNode.lines[1].no
                    
                    #prevDlt
                    if(nowLineNo==prevLineNo0):
                        prevDlt=prevLineNo1-nowLineNo
                    elif(nowLineNo==prevLineNo1):
                        prevDlt=prevLineNo0-nowLineNo
                        
                    #nextDlt
                    if(nowLineNo==nextLineNo0):
                        nextDlt=nextLineNo1-nowLineNo
                    elif(nowLineNo==nextLineNo1):
                        nextDlt=nextLineNo0-nowLineNo
                    
                    #++
                    if(prevDlt>0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[1])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #-+
                    elif(prevDlt<0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[3])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[1])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #+-
                    elif(prevDlt>0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #--
                    elif(prevDlt<0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[3])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    
                    self.setRhomboid(searchNode,newMovePt)
                    
            else:
                #myIndex+1のnode
                searchNode=line.nodes[myIndex+1]
                if(searchNode.isVisited==False):
                    newNo=-1
                    newName=""
                    newAng0=searchNode.lines[0].angle
                    newAng1=searchNode.lines[1].angle
                    newAngle=newAng1-newAng0
                    newRotateAng=(newAng0+newAng1)/2.0-90
                    newRhomboid=Rhomboid(newNo,newName,newAngle,newRotateAng,[0,0,0],self.l,searchNode.lines)
                    
                    #nowLineNo
                    nowLineNo=line.no
                    
                    #prevLineNo,nextLineNo
                    prevLineNo0=node.lines[0].no
                    prevLineNo1=node.lines[1].no
                    nextLineNo0=searchNode.lines[0].no
                    nextLineNo1=searchNode.lines[1].no
                    
                    #prevDlt
                    if(nowLineNo==prevLineNo0):
                        prevDlt=prevLineNo1-nowLineNo
                    elif(nowLineNo==prevLineNo1):
                        prevDlt=prevLineNo0-nowLineNo
                        
                    #nextDlt
                    if(nowLineNo==nextLineNo0):
                        nextDlt=nextLineNo1-nowLineNo
                    elif(nowLineNo==nextLineNo1):
                        nextDlt=nextLineNo0-nowLineNo
                    
                    #++
                    if(prevDlt>0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[1])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #+-
                    elif(prevDlt>0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[1])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[3])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #-+
                    elif(prevDlt<0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #--
                    elif(prevDlt<0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[3])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    
                    self.setRhomboid(searchNode,newMovePt)
                    
                    
                #myIndex-1のnode
                searchNode=line.nodes[myIndex-1]
                if(searchNode.isVisited==False):
                    newNo=-1
                    newName=""
                    newAng0=searchNode.lines[0].angle
                    newAng1=searchNode.lines[1].angle
                    newAngle=newAng1-newAng0
                    newRotateAng=(newAng0+newAng1)/2.0-90
                    newRhomboid=Rhomboid(newNo,newName,newAngle,newRotateAng,[0,0,0],self.l,searchNode.lines)
                    
                    #nowLineNo
                    nowLineNo=line.no
                    
                    #prevLineNo,nextLineNo
                    prevLineNo0=node.lines[0].no
                    prevLineNo1=node.lines[1].no
                    nextLineNo0=searchNode.lines[0].no
                    nextLineNo1=searchNode.lines[1].no
                    
                    #prevDlt
                    if(nowLineNo==prevLineNo0):
                        prevDlt=prevLineNo1-nowLineNo
                    elif(nowLineNo==prevLineNo1):
                        prevDlt=prevLineNo0-nowLineNo
                        
                    #nextDlt
                    if(nowLineNo==nextLineNo0):
                        nextDlt=nextLineNo1-nowLineNo
                    elif(nowLineNo==nextLineNo1):
                        nextDlt=nextLineNo0-nowLineNo
                    
                    #++
                    if(prevDlt>0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[1])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #-+
                    elif(prevDlt<0 and nextDlt>0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[3])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[1])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #+-
                    elif(prevDlt>0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[0])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    #--
                    elif(prevDlt<0 and nextDlt<0):
                        movePt0=rhomboid.getAbsolutePt(rhomboid.pts[3])
                        movePt1=newRhomboid.getAbsolutePt(newRhomboid.pts[0])
                        newMovePt=rs.VectorSubtract(movePt0, movePt1)
                    
                    self.setRhomboid(searchNode,newMovePt)

    def findRhomboid(self,name):
        """
        同じ名前の菱形を返す
        :param name:
        :return:
        """
        res=None
        for i,rhomboid in enumerate(self.rhomboids):
            if(rhomboid.name==name):
                res=rhomboid
                break
        return res
