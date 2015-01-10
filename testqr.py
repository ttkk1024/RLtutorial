#coding:utf-8
__author__ = 'SharpShell'

import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=1
)
qr.add_data("车辆制造企业：山东梅拉德能源动力科技有限公司\n车辆品牌：雷丁牌\n车辆型号：D50  乐享版  象牙白\n车辆识别代号：LDEA01*01004936*F\n电机编号：DPD14011671\n控制器号：20131224072\n生产日期：2014年1月23日\n电池类型：动力免维护铅酸蓄电池\n功率：48V4KW\n驱动电机型号：直流他例驱动电机\n外廓尺寸：3320mm*1540mm*1480mm\n轮胎规格：145/70R12\n整备质量：760KG\n额定载质量：300KG")
qr.make(fit=True)
img = qr.make_image()
img.save("dhqme_qrcode.jpg")