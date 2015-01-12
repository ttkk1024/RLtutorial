#coding:utf-8
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import *
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
 
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
#pdfmetrics.registerFont(TTFont('song', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'))
pdfmetrics.registerFont(TTFont('hei', 'rml/fonts/simfang.ttf'))
 
from reportlab.lib import fonts,colors
#fonts.addMapping('song', 0, 0, 'song')
#fonts.addMapping('song', 0, 1, 'song')
fonts.addMapping('hei', 0, 0, 'hei')
fonts.addMapping('hei', 0, 1, 'hei')
 
stylesheet=getSampleStyleSheet()
elements = []
 
doc = SimpleDocTemplate('test.pdf')
 
 
elements.append(Paragraph('<font name="hei">学 生 成 绩 单</font>',stylesheet['Title']))
elements.append(Spacer(1,12))
 
stylesheet.add(ParagraphStyle(name='Justify',alignment=TA_JUSTIFY))
stylesheet['Justify'].fontName = 'hei'
 
elements.append(flowables.Preformatted('课程名称：_____________________                                         主讲教师签名：_____________________' ,stylesheet['Justify']))
elements.append(Spacer(1,12))
 
 
data = []
data.append(['学号','姓名','成绩'])
data.append(['学号','姓名','成绩'])
data.append(['学号','姓名','成绩'])
data.append(['学号','姓名','成绩'])
data.append(['学号','姓名','成绩'])
# import MySQLdb
#
# conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="electsys",charset="utf8")
# cur = conn.cursor()
# sql = 'select s_no,s_name,s_score from student'
# cur.execute(sql)
# result = cur.fetchall()
# for l in result:
#     data.append(l)
#
#ts = [('ALIGN',(0,0),(-1,-1),'CENTER'),('FONT', (0,0), (-1,-1), 'hei')]
ts=[('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black),('FONT', (0,0), (-1,-1), 'hei')]
table = Table(data, 2.1*inch, 0.24*inch, ts)
elements.append(table)
 
doc.build(elements)