#coding:utf-8
__author__ = 'SharpShell'

import qrcode
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('hei', 'rml/fonts/simfang.ttf'))
from reportlab.pdfgen import canvas
from reportlab.lib import colors, fonts
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Image


fonts.addMapping('hei', 0, 0, 'hei')
fonts.addMapping('hei', 0, 1, 'hei')

stylesheet = getSampleStyleSheet()

class Car(object):
    """合格证信息"""
    pass
car = Car()


with open("data/11.txt") as input_data:
    input_list = [num.split('|') for num in input_data.readlines()]
output_list = input_list[6:-1]
for li in output_list:
    car.zhgzn = li[9]
    car.zhgrq  = li[23]
    car.ename  = "山东梅拉德能源动力科技有限公司"
    car.carname= "雷丁牌"
    car.zpzmx = li[10]
    car.zclsbn = li[2]
    car.zys = li[11]
    car.zdjlx = li[15]
    car.zdjn = li[7]
    car.zkzqn = li[3]
    car.dclx  = "动力免维护胶体电池"
    car.zjgl = li[16]
    if car.zpzmx in ['D50 乐享2014版','D50 众享2014版','D50 福享2014版','D50 劲享2014版','D50 尊享2014版','D50 乐享2015版','D50 众享2015版','D50 福享2015版']:
        car.wkcc = "3320*1540*1480"
        car.ltgg = "145/70R12"
        car.lj = "1360"
        car.zj = "2260"
    elif car.zpzmx in ['D60 乐享2014版','D60 尊享2014版']:
        car.wkcc = "3994*1618*1500"
        car.ltgg = "165/65R14"
        car.lj = "1420"
        car.zj = "2400"
    elif car.zpzmx in ['D70 乐享2015版','D70 福享2015版','D70 尊享2015版']:
        car.wkcc = "3356*1540*1480"
        car.ltgg = "145/70R12"
        car.lj = "1360"
        car.zj = "2260"
    car.lts = "4"
    car.zh = li[25]
    car.zzl = li[26]
    car.zzbzl = li[24]
    car.zcs = li[27]
    car.zzzrq = li[22]

    qr = qrcode.QRCode(
       version = 2 ,
       error_correction = qrcode.ERROR_CORRECT_L,
       box_size = 10,
       border = 1
    )
    qr.add_data('车辆品牌:'+car.carname+'\n'
               +'车辆型号:'+car.zpzmx+'\n'
               +'车辆识别代号:'+car.zclsbn+'\n'
               +'电机编号:'+car.zdjn+'\n'
               +'控制器号:'+car.zkzqn+'\n'
               +'功率:'+car.zjgl+'\n'
               +'整备质量:'+car.zzbzl)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("rml/img/"+car.zclsbn+".jpg")

    doc = SimpleDocTemplate('output/'+car.zclsbn+".pdf", pagesize=A4)
    # container for the 'Flowable' objects
    elements = []

    I = Image('rml/img/'+car.zclsbn+'.jpg')
    I.drawHeight = 1.4*inch*I.drawHeight / I.drawWidth
    I.drawWidth = 1.4*inch

    data = [['1.合格证编号',car.zhgzn , '2.发证日期',car.zhgrq ],
       ['3.车辆制造企业名称', car.ename, '', ''],
       ['4.车辆品牌/车辆名称',car.carname, '电动代步车辆', ''],
       ['5.车辆型号',car.zpzmx , '6.车辆识别代码/车架号',car.zclsbn ],
       ['7.车身颜色', car.zys, '', ''],
       ['8.底盘型号/底盘ID', '--', '', '--'],
       ['9.底盘合格证编号', '--', '10.驱动电机型号', car.zdjlx],
       ['11.电机编号', car.zdjn, '12.控制器号', car.zkzqn],
       ['13.电池类型', '动力免维护胶体电池', '14.功率（KW）',car.zjgl ],
       ['15.排放标准', '零排放', '--', '--'],
       ['16.百公里耗电(kwh)', '--', '--', '--'],
       ['17.外廓尺寸', car.wkcc, '18.货箱内部尺寸(mm)', '--'],
       ['19.轮胎数', '4', '20.轮胎规格', car.ltgg],
       ['21.轮距(前/后)(mm)', car.lj, car.lj, '--'],
       ['22.轴距', car.zj, '', ''],
       ['23.轴荷(kg)', car.zh, '', ''],
       ['24.轴数', '2', '25.转向形式', '方向盘'],
       ['26.总质量(kg)', car.zzl, '27.整备质量(kg)', car.zzbzl ],
       ['28.额定载质量(kg)', '300', '29.载质量利用系数', '--'],
       ['30.驾驶室准乘人数', '--', [I], ''],
       ['31.额定载客', '4', '', ''],
       ['32.最高设计时速(KM/H)', car.zcs, '', ''],
       ['33.车辆制造日期', car.zzzrq, '', ''],
       ['备注:', '', '', ''],
       ['车辆制造企业信息:\n本产品经过检验，达到出厂质量的要求，准予出厂，特此声明。\n车辆生成单位名称:山东梅拉德能源动力科技有限公司\n生产单位地址:山东省潍坊市昌乐县比德文千亩产业园', '', '', ''],
       ['本产品经过检验，达到出厂质量的要求，准予出厂，特此声明。', '', '', ''],
       ['车辆生成单位名称:山东梅拉德能源动力科技有限公司', '', '', ''],
       ['生产单位地址:山东省潍坊市昌乐县比德文千亩产业园', '', '', '']]

    t = Table( data, 1.8 * inch, 0.3 * inch)
    t.setStyle(TableStyle([#('ALIGN',(1,1),(-1,-1),'RIGHT'),
                           #('TEXTCOLOR',(1,1),(-1,-1),colors.red),
                          # ('VALIGN',(0,0),(0,-1),'TOP'),
                          # ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                           ('ALIGN',(0,24),(-1,-1),'LEFT'),
                           ('VALIGN',(0,24),(-1,-1),'TOP'),
                          # ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONT', (0,0), (-1,-1), 'hei'),
                           ('SPAN',(1,1),(3,1)),
                           ('SPAN',(1,5),(2,5)),
                           ('SPAN',(1,14),(3,14)),
                           ('SPAN',(1,15),(3,15)),
                           ('SPAN',(2,19),(3,23)),
                           ('SPAN',(0,23),(1,23)),
                           ('SPAN',(0,24),(3,27)),
                           ('SPAN',(1,4),(3,4)),
                           ('SPAN',(2,2),(3,2))
                           ]))
    elements.append(t)
    # write the document to disk
    doc.build(elements)
    print car.zclsbn + " Finished"


print("ALL Finished!")
