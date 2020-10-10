# -*- coding: utf-8 -*-
import rhinoscriptsyntax as rs
import random
from System.Drawing import Color
from emblem.Emblem import *

def setLayer():
    # ---emblem
    if not rs.IsLayer("emblem"):
        ptsLayer = rs.AddLayer("emblem",
                               Color.FromArgb(0, 0, 0),
                               visible=True,
                               locked=False,
                               parent=None)

    # ---emblem.lineBlack
    if not rs.IsLayer("lineBlack"):
        ptsLayer = rs.AddLayer("lineBlack",
                               Color.FromArgb(0, 0, 0),
                               visible=True,
                               locked=False,
                               parent="emblem")
    # ---emblem.lineGray
    if not rs.IsLayer("lineGray"):
        ptsLayer = rs.AddLayer("lineGray",
                               Color.FromArgb(200, 200, 200),
                               visible=True,
                               locked=False,
                               parent="emblem")
    # ---emblem.rhomboidText
    if not rs.IsLayer("textRhomboid"):
        ptsLayer = rs.AddLayer("textRhomboid",
                               Color.FromArgb(0, 0, 0),
                               visible=True,
                               locked=False,
                               parent="emblem")
    # ---emblem.lineGray
    if not rs.IsLayer("srfRhomboid"):
        ptsLayer = rs.AddLayer("srfRhomboid",
                               Color.FromArgb(200, 200, 200),
                               visible=True,
                               locked=False,
                               parent="emblem")
    # ---emblem.line,srf
    for i in range(12):
        if not rs.IsLayer("line%s" % i):
            r = random.randint(0,255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            ptsLayer = rs.AddLayer( "line%s" % i,
                                    Color.FromArgb(r,g,b),
                                    visible=True,
                                    locked=False,
                                    parent="emblem")
            ptsLayer = rs.AddLayer("srf%s" % i,
                                   Color.FromArgb(r, g, b),
                                   visible=True,
                                   locked=False,
                                   parent="emblem")
    # ---emblem.parallelLine.lineText
    if not rs.IsLayer("textLine"):
        ptsLayer = rs.AddLayer("textLine",
                               Color.FromArgb(0, 0, 0),
                               visible=True,
                               locked=False,
                               parent="emblem")

def drawDivisionLine(emblem,color=True):
    objs = []
    # line
    r = 24
    for i in range(int(emblem.division)):
        p = [r, 0, 0]
        if (emblem.division % 4 == 0):
            angle = i * 360.0 / emblem.division + 360.0 / emblem.division / 2.0
        else:
            angle = i * 360.0 / emblem.division
        p = rs.VectorRotate(p, angle, [0, 0, 1])
        obj = rs.AddLine([0, 0, 0], p)
        if(color):
            layer = "line%s" % (i % int(emblem.division/2.0))
        else:
            layer = "lineGray"
        rs.ObjectLayer(obj, layer)
        objs.append(obj)
    # circle
    obj = rs.AddCircle([0, 0, 0], r)
    if (color):
        layer = "lineBlack"
    else:
        layer = "lineGray"
    rs.ObjectLayer(obj, layer)
    objs.append(obj)
    # text
    planeOri = rs.ViewCPlane()
    for i in range(int(emblem.division/2.0)):
        if (emblem.division % 4 == 0):
            angle = i * 360.0 / emblem.division + 360.0 / emblem.division / 2.0
        else:
            angle = i * 360.0 / emblem.division
        p=[r,0,0]
        txt = "%d" % (angle)
        height = 1.2
        pt = [0,height/2.0,0]
        font = "Alte DIN 1451 Mittelschrift"
        font_style = 0
        justification = 2 + 65536
        obj = rs.AddText(txt,
                         pt,
                         height,
                         font,
                         font_style,
                         justification)
        rs.RotateObject(obj, [0,0,0], -90.0, [0, 0, 1], False)
        rs.MoveObject(obj,[r,0,0])
        rs.RotateObject(obj,[0,0,0],angle,[0,0,1],False)
        rs.ObjectLayer(obj, "textLine")
        objs.append(obj)
        rs.ViewCPlane(None,planeOri)
    #return
    return objs

def drawRegularOffsetLine(emblem):
    objs=[]
    #lines
    for parallelLine in emblem.parallelLines:
        for line in parallelLine.lines:
            for i in range(len(line.nodes)-1):
                obj=rs.AddLine(line.nodes[i].pt, line.nodes[i+1].pt)
                name="line%s" % line.no
                rs.ObjectLayer(obj, name)
                objs.append(obj)
    # lineText
    for node in emblem.nodes:
        txt = "%d-%d" % (node.lines[0].angle, node.lines[1].angle)
        height = 1.2
        pt=[node.pt[0],node.pt[1]+height/2.0,node.pt[2]]
        font="Alte DIN 1451 Mittelschrift"
        font_style = 0
        justification = 2+65536
        obj = rs.AddText( txt,
                          pt,
                          height,
                          font,
                          font_style,
                          justification)
        rs.ObjectLayer(obj, "textLine")
        objs.append(obj)

    return objs

def drawRhombusOnRegularOffsetLine(emblem):
    tmpObjs = []
    for rhomboid in emblem.rhomboids:
        objs = []

        # 中点長方形の対角四角形
        for i in range(len(rhomboid.midPts)):
            p0 = rhomboid.midPts[i]
            if (i == 0):
                nextMidPt = rhomboid.midPts[i + 1]
                prevtMidPt = rhomboid.midPts[len(rhomboid.midPts) - 1]
            elif (i == len(rhomboid.midPts) - 1):
                nextMidPt = rhomboid.midPts[0]
                prevtMidPt = rhomboid.midPts[i - 1]
            else:
                nextMidPt = rhomboid.midPts[i + 1]
                prevtMidPt = rhomboid.midPts[i - 1]
            p1 = rs.VectorAdd(p0, nextMidPt)
            p1 = rs.VectorDivide(p1, 2.0)
            p2 = rhomboid.ellipsePts[0]
            p3 = rs.VectorAdd(p0, prevtMidPt)
            p3 = rs.VectorDivide(p3, 2.0)
            pts=[p0, p1, p2, p3, p0]
            obj = rs.AddPolyline(pts)
            if (i % 2 == 0):
                rs.ObjectLayer(obj, "srf%s" % rhomboid.lines[1].no)
            else:
                rs.ObjectLayer(obj, "srf%s" % rhomboid.lines[0].no)
            objs.append(obj)

        # 外周面
        pts = []
        for pt in rhomboid.pts:
            pts.append(pt)
        pts.append(pts[0])
        obj = rs.AddPolyline(pts)
        rs.ObjectLayer(obj, "srfRhomboid")
        objs.append(obj)

        # 外周線
        for i in range(len(rhomboid.pts)):
            if (i == len(rhomboid.pts) - 1):
                obj = rs.AddLine(rhomboid.pts[i], rhomboid.pts[0])
            else:
                obj = rs.AddLine(rhomboid.pts[i], rhomboid.pts[i + 1])
            rs.ObjectLayer(obj, "lineBlack")
            objs.append(obj)

        # move to center
        objs=rs.MoveObjects(objs, [-rhomboid.ellipsePts[0][0],-rhomboid.ellipsePts[0][1],-rhomboid.ellipsePts[0][2]])

        # rotate
        xform = rs.XformRotation2(rhomboid.rotateAng, [0, 0, 1], [0, 0, 0])
        rs.TransformObjects(objs, xform)

        # move
        pts = rs.LineLineIntersection([rhomboid.lines[0].sPt, rhomboid.lines[0].ePt], [rhomboid.lines[1].sPt, rhomboid.lines[1].ePt])
        rs.MoveObjects(objs, pts[0])

        # tmpObjs
        for obj in objs:
            tmpObjs.append(obj)

    return tmpObjs

def drawEhombusTilingByRegularOffsetLine(emblem):
    tmpObjs = []

    # self.rhomboids
    for rhomboid in emblem.rhomboids:
        objs = []

        # 中点長方形の対角四角形
        for i in range(len(rhomboid.midPts)):
            p0 = rhomboid.midPts[i]
            if (i == 0):
                nextMidPt = rhomboid.midPts[i + 1]
                prevtMidPt = rhomboid.midPts[len(rhomboid.midPts) - 1]
            elif (i == len(rhomboid.midPts) - 1):
                nextMidPt = rhomboid.midPts[0]
                prevtMidPt = rhomboid.midPts[i - 1]
            else:
                nextMidPt = rhomboid.midPts[i + 1]
                prevtMidPt = rhomboid.midPts[i - 1]
            p1 = rs.VectorAdd(p0, nextMidPt)
            p1 = rs.VectorDivide(p1, 2.0)
            p2 = rhomboid.ellipsePts[0]
            p3 = rs.VectorAdd(p0, prevtMidPt)
            p3 = rs.VectorDivide(p3, 2.0)
            pts = [p0, p1, p2, p3, p0]
            obj = rs.AddPolyline(pts)
            if (i % 2 == 0):
                rs.ObjectLayer(obj, "srf%s" % rhomboid.lines[1].no)
            else:
                rs.ObjectLayer(obj, "srf%s" % rhomboid.lines[0].no)
            objs.append(obj)

        # 外周面
        pts = []
        for pt in rhomboid.pts:
            pts.append(pt)
        pts.append(pts[0])
        obj = rs.AddPolyline(pts)
        rs.ObjectLayer(obj, "srfRhomboid")
        objs.append(obj)

        # 外周線
        for i in range(len(rhomboid.pts)):
            if (i == len(rhomboid.pts) - 1):
                obj = rs.AddLine(rhomboid.pts[i], rhomboid.pts[0])
            else:
                obj = rs.AddLine(rhomboid.pts[i], rhomboid.pts[i + 1])
            rs.ObjectLayer(obj, "lineBlack")
            objs.append(obj)

        # rotate
        xform = rs.XformRotation2(rhomboid.rotateAng, [0, 0, 1], [0, 0, 0])
        rs.TransformObjects(objs, xform)

        # move
        rs.MoveObjects(objs, rhomboid.movePt)

        # text
        txt = "%s" % (rhomboid.name)
        pt = rhomboid.getAbsolutePt(rhomboid.ellipsePts[0])
        height = 1.2
        pt = [pt[0], pt[1] + height / 2.0, pt[2]]
        obj = rs.AddText(txt,
                         pt,
                         height,
                         font="Alte DIN 1451 Mittelschrift",
                         font_style=0,
                         justification=2 + 65536)
        rs.ObjectLayer(obj, "textRhomboid")
        objs.append(obj)

        # tmpObjs
        for obj in objs:
            tmpObjs.append(obj)

    # move to center
    pts = rs.BoundingBox(tmpObjs)
    center = rs.VectorAdd(pts[0], pts[2])
    center = rs.VectorScale(center, 0.5)
    center = rs.VectorSubtract([0, 0, 0], center)
    rs.MoveObjects(tmpObjs, center)

    return tmpObjs
