#!/usr/bin/python
# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph,Frame
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Image as platImage
from PIL import Image
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
#支持中文，需要下载相应的文泉驿中文字体
pdfmetrics.registerFont(TTFont('hei', './SimHei.ttf'))
#import testSubFun
#testSubFun.testSubFunc('first')
#设置页面大小
c = canvas.Canvas('测试.pdf',pagesize=A4)
xlength,ylength = A4
print('width:%d high:%d'%(xlength,ylength))
#c.line(1,1,ylength/2,ylength)
#设置文字类型及字号
c.setFont('hei',20)
#生成一个table表格
atable = [[1,2,3,4],[5,6,7,8]]
t = Table(atable,50,20)
t.setStyle(TableStyle([('ALIGN',(0,0),(3,1),'CENTER'),
                       ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
                       ('BOX',(0,0),(-1,-1),0.25,colors.black)]))
textOb = c.beginText(1,ylength-10)
indexVlaue = 0
while(indexVlaue < ylength):
    textStr = '''test 中文写入测试中文写入测试中文写入测试中文写入测试%d'''%indexVlaue
    #print('nextline,nextline%d'%indexVlaue)
    textOb.textLine(textStr)
    indexVlaue = indexVlaue + 1
    break
c.drawText(textOb)
#简单的图片载入
imageValue = 'test.png'
c.drawImage(imageValue,97,97,300,300)
c.drawImage('test.png',50,50,50,50)
t.split(0,0)
t.drawOn(c,100,1)
c.showPage()
#换页的方式不同的showPage
c.drawString(0,0,'helloword')
c.showPage()
