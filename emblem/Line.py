# -*- coding: utf-8 -*-

########################################################################
#Line Class
########################################################################
class Line():
    def __init__(self,no,no2,sPt,ePt,angle):
        self.no=no          #int lineの種類番号 1<=no<=6
        self.no2=no2        #int 同じ種類の中で何番目か
        self.sPt=sPt        #[x,y,z] 始点(描画には使わない。ベクトル用)
        self.ePt=ePt        #[x,y,z] 終点(描画には使わない。ベクトル用)
        self.angle=angle    #float 0<=angle<180
        self.nodes=[]       #Node[] このライン上に乗っている交点
        
    def nodesSort(self):
        if(self.angle>=0 and self.angle<90):
            self.nodes=sorted(self.nodes, key=lambda x: x.pt[0])
        elif(self.angle>=90 and self.angle<180):
            self.nodes=sorted(self.nodes, key=lambda x: x.pt[1])