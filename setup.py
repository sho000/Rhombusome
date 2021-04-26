# -*- coding: utf-8 -*-
from draw import *
import rhinoscriptsyntax as rs

##########################################
# setLayer
##########################################
setLayer()
checkFont() # checks if system has 'DIN' font.
##########################################
# EnableRedraw
rs.EnableRedraw(False)
##########################################
# regular lineNum=1
##########################################
#emblems
emblems=[]
for i in range(8):
    division = 4.0 + 2 * i
    lineNum = 1
    l = 6
    offsets=[]
    if (4 + 2 * i == 4):
        offsets = [0, 0]
    else:
        for j in range(4 + 2 * i):
            if (j % 2 == 0):
                offsets.append(l)
            else:
                offsets.append(-l)
    distances = []
    for j in range(4 + 2 * i):
        distances.append(l)
    emblem = Emblem(division,
                    lineNum,
                    l,
                    offsets,
                    distances)
    emblems.append(emblem)
#draw
for i in range(8):
    # drawDivisionLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=True)
    move = [60 + 30 + 60 * i, -90 - 60 * 0, 0]
    rs.MoveObjects(objs, move)

    # drawRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    move = [60 + 30 + 60 * i, -90 - 60 * 1, 0]
    rs.MoveObjects(objs, move)

    # drawRhombusOnRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    objs += drawRhombusOnRegularOffsetLine(emblems[i])
    move = [60 + 30 + 60 * i, -90 - 60 * 2, 0]
    rs.MoveObjects(objs, move)

    # drawEhombusTilingByRegularOffsetLine
    objs = []
    objs += drawEhombusTilingByRegularOffsetLine(emblems[i])
    move = [60 + 30 + 60 * i, -90 - 60 * 3, 0]
    rs.MoveObjects(objs, move)

##########################################
# regular lineNum=2
##########################################
#emblems
emblems=[]
for i in range(8):
    division = 4.0 + 2 * i
    lineNum = 2
    l = 6
    offsets = []
    for j in range(4 + 2 * i):
        offsets.append(0)
    distances = []
    for j in range(4 + 2 * i):
        distances.append(l*2)
    emblem = Emblem(division,
                    lineNum,
                    l,
                    offsets,
                    distances)
    emblems.append(emblem)
#draw
for i in range(8):
    # drawDivisionLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=True)
    move = [60 + 30 + 60 * i, -90 - 60 * 4, 0]
    rs.MoveObjects(objs, move)

    # drawRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    move = [60 + 30 + 60 * i, -90 - 60 * 5, 0]
    rs.MoveObjects(objs, move)

    # drawRhombusOnRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    objs += drawRhombusOnRegularOffsetLine(emblems[i])
    move = [60 + 30 + 60 * i, -90 - 60 * 6, 0]
    rs.MoveObjects(objs, move)

    # drawEhombusTilingByRegularOffsetLine
    objs = []
    objs += drawEhombusTilingByRegularOffsetLine(emblems[i])
    move = [60 + 30 + 60 * i, -90 - 60 * 7, 0]
    rs.MoveObjects(objs, move)

##########################################
# random lineNum=1
##########################################
#emblems
emblems=[]
for i in range(8):
    division = 4.0 + 2 * i
    lineNum = 1
    l = 6
    offsets = []
    distances = []
    for j in range(4 + 2 * i):
        distances.append(l)
    emblem = Emblem(division,
                    lineNum,
                    l,
                    offsets,
                    distances)
    emblems.append(emblem)
#draw
for i in range(8):
    # drawDivisionLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=True)
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 0, 0]
    rs.MoveObjects(objs, move)

    # drawRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 1, 0]
    rs.MoveObjects(objs, move)

    # drawRhombusOnRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    objs += drawRhombusOnRegularOffsetLine(emblems[i])
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 2, 0]
    rs.MoveObjects(objs, move)

    # drawEhombusTilingByRegularOffsetLine
    objs = []
    objs += drawEhombusTilingByRegularOffsetLine(emblems[i])
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 3, 0]
    rs.MoveObjects(objs, move)

##########################################
# regular lineNum=2
##########################################
#emblems
emblems=[]
for i in range(8):
    division = 4.0 + 2 * i
    lineNum = 2
    l = 6
    offsets = []
    distances = []
    emblem = Emblem(division,
                    lineNum,
                    l,
                    offsets,
                    distances)
    emblems.append(emblem)
#draw
for i in range(8):
    # drawDivisionLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=True)
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 4, 0]
    rs.MoveObjects(objs, move)

    # drawRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 5, 0]
    rs.MoveObjects(objs, move)

    # drawRhombusOnRegularOffsetLine
    objs = []
    objs += drawDivisionLine(emblems[i], color=False)
    objs += drawRegularOffsetLine(emblems[i])
    objs += drawRhombusOnRegularOffsetLine(emblems[i])
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 6, 0]
    rs.MoveObjects(objs, move)

    # drawEhombusTilingByRegularOffsetLine
    objs = []
    objs += drawEhombusTilingByRegularOffsetLine(emblems[i])
    move = [660 + 60 + 30 + 60 * i, -90 - 60 * 7, 0]
    rs.MoveObjects(objs, move)

######################################################################
#オリンピック、パラリンピック モーフィング用
######################################################################
# setScale
def setScale(list,scale):
    newList=[]
    for val in list:
        val=val*scale
        newList.append(val)
    return newList

#globals
xNum=8
yNum=4
scale=0.5

#オリンピック
offsets_o=[-5,4,5,-4,-5,4]
distances_o=[12,12,12,12,12,12]
offsets_o=setScale(offsets_o, scale)
distances_o=setScale(distances_o, scale)

#パラリンピック
offsets_p=[-(44.7/2-6),-(32.7/2-6),0,0,(32.7/2-6),(44.7/2-6)]
distances_p=[44.7,32.7,12,12,32.7,44.7]
offsets_p=setScale(offsets_p, scale)
distances_p=setScale(distances_p, scale)

#from o to p
offsets=[]
distances=[]

# move line0
no = 0
div = 4.0
for i in range(int(div)):
    #tmpOffset
    tmpOffset=[]
    for val in offsets_o:
        tmpOffset.append(val)
    d = (offsets_p[no] - offsets_o[no]) / div
    tmpOffset[no] = offsets_o[no] + d * i
    offsets.append(tmpOffset)
    #tmpDistance
    tmpDistance=[]
    for val in distances_o:
        tmpDistance.append(val)
    d = (distances_p[no] - distances_o[no]) / div
    tmpDistance[no] = distances_o[no] + d * i
    distances.append(tmpDistance)
# move line1-4
for j in range(4):
    no = j + 1
    div = 6.0
    for i in range(int(div)):
        #tmpOffset
        tmpOffset=[]
        for k,val in enumerate(offsets[int(j*div+3)]):
            if(k<no):
                tmpOffset.append(offsets_p[k])
            else:
                tmpOffset.append(val)
        d = (offsets_p[no] - offsets_o[no]) / div
        tmpOffset[no] = offsets_o[no] + d * i
        offsets.append(tmpOffset)
        #tmpDistance
        tmpDistance=[]
        for k,val in enumerate(distances[int(j*div+3)]):
            if (k < no):
                tmpDistance.append(distances_p[k])
            else:
                tmpDistance.append(val)
        d = (distances_p[no] - distances_o[no]) / div
        tmpDistance[no] = distances_o[no] + d * i
        distances.append(tmpDistance)
# move line7
no = 5
div = 4.0
for i in range(int(div)):
    # tmpOffset
    tmpOffset = []
    for k,val in enumerate(offsets[4+4*6-1]):
        if (k < no):
            tmpOffset.append(offsets_p[k])
        else:
            tmpOffset.append(val)
    d = (offsets_p[no] - offsets_o[no]) / (div-1)
    tmpOffset[no] = offsets_o[no] + d * i
    offsets.append(tmpOffset)
    # tmpDistance
    tmpDistance = []
    for k,val in enumerate(distances[4+4*6-1]):
        if (k < no):
            tmpDistance.append(distances_p[k])
        else:
            tmpDistance.append(val)
    d = (distances_p[no] - distances_o[no]) / (div-1)
    tmpDistance[no] = distances_o[no] + d * i
    distances.append(tmpDistance)

#print
# for i,offset in enumerate(offsets):
#     print("offsets[%s]=%s" % (i,offset))
# print(offsets_p)
# for i,distance in enumerate(distances):
#     print("distances[%s]=%s" % (i,distance))
# print(distances_p)


#emblemsインスタンス化
emblems=[]
for i in range(len(offsets)):
    division = 12
    lineNum = 2
    l = 6
    emblem = Emblem(division,
                    lineNum,
                    l,
                    offsets[i],
                    distances[i])
    emblems.append(emblem)

#emblems.draw
i=0
for y in range(yNum):
    for x in range(xNum):
        # emblems[cnt].drawParallelLines([57+x*60, 660.5-y*120, 0])
        # emblems[cnt].drawRhomboids([57+x*60, 720.5-y*120, 0])
        # drawRegularOffsetLine
        objs = []
        objs += drawDivisionLine(emblems[i], color=False)
        objs += drawRegularOffsetLine(emblems[i])
        move = [60 + 30 + 60 * x, -90 - 60 * y *2 - 660, 0]
        rs.MoveObjects(objs, move)

        # drawEhombusTilingByRegularOffsetLine
        objs = []
        objs += drawEhombusTilingByRegularOffsetLine(emblems[i])
        move = [60 + 30 + 60 * x, -90 -60 - 60 * y *2 - 660, 0]
        rs.MoveObjects(objs, move)
        i+=1

######################################################################
# ランダムエンブレム
######################################################################
emblems = []
for i in range(xNum*yNum):
    division = 12
    lineNum = 2
    l = 6
    offsets = []
    distances = []
    emblem = Emblem(division,
                    lineNum,
                    l,
                    offsets,
                    distances)
    emblems.append(emblem)

# emblems.draw
i = 0
for y in range(yNum):
    for x in range(xNum):
        # emblems[cnt].drawParallelLines([57+x*60, 660.5-y*120, 0])
        # emblems[cnt].drawRhomboids([57+x*60, 720.5-y*120, 0])
        # drawRegularOffsetLine
        objs = []
        objs += drawDivisionLine(emblems[i], color=False)
        objs += drawRegularOffsetLine(emblems[i])
        move = [660 + 60 + 30 + 60 * x, -90 - 60 * y * 2 - 660, 0]
        rs.MoveObjects(objs, move)

        # drawEhombusTilingByRegularOffsetLine
        objs = []
        objs += drawEhombusTilingByRegularOffsetLine(emblems[i])
        move = [660 + 60 + 30 + 60 * x, -90 - 60 - 60 * y * 2 - 660, 0]
        rs.MoveObjects(objs, move)
        i += 1
##########################################
#EnableRedraw
rs.EnableRedraw(True)


