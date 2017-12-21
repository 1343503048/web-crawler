
# -*- coding: UTF-8 -*-
import xlrd
import xlwt
import sys
default_encoding="utf-8"
if(default_encoding!=sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)
wb = xlrd.open_workbook('data.xlsx')

info = {}

def init():
    info['城市'] = "北京"
    info['季节'] = "夏"
    info['开始时间'] = "20150101"
    info['SO2'] = -1
    info['NO2'] = -1
    info['PM10'] = -1
    info['CO'] = -1
    info['O3'] = -1
    info['PM25'] = -1
    info['结束时间'] = "20151111"
    info['endSO2'] = -1
    info['endNO2'] = -1
    info['endPM10'] = -1
    info['endCO'] = -1
    info['endO3'] = -1
    info['endPM25'] = -1
    info['降水时间'] = 0
    info['降水总量'] = 0
    info['最大降水量'] = 0
    info['最大风速'] = 0  # 风速
    info['最大风速对应风向'] = 0
    info['平均降水强度'] = 0
    info['降水时段平均风速'] = 0


init()

# for i in range(s.nrows):
#     # for j in s.clo_values(s.nclos):
list = []
table = wb.sheets()[0]
res = xlwt.Workbook()
table2 = res.add_sheet('result', cell_overwrite_ok=True)

# 读取表头
for val in table.row_values(0):
    # print unicode(s.row(i)[3].value)
    str = val.encode("utf-8")
    list.append(str)

# 数据处理
sz = 1
vis = 0

s = u'中文'
print s.encode('utf-8')
table2.write(2, 2, s.encode("utf-8"))

for i in range(1, table.nrows, 1) :
    if table.row(i)[list.index('降水量(毫米)')].value == 0.0:
        for j in range(0, 46, 1):
            if vis == 1:
                info['endSO2'] = table.row(i)[list.index('SO2')].value
                info['endNO2'] = table.row(i)[list.index('NO2')].value
                info['endPM10'] = table.row(i)[list.index('PM10')].value
                info['endCO'] = table.row(i)[list.index('CO-1h')].value
                info['endO3'] = table.row(i)[list.index('O3')].value
                info['endPM25'] = table.row(i)[list.index('PM2.5')].value
                info['降水时段平均风速'] /= info['降水时间']
                info['平均降水强度'] /= info['降水时间']
                k = 0
                varList = info.values()
                for vi in varList:
                    a = vi
                    if vi == '安庆':
                        a = 'anqing'
                    elif vi == '宣城':
                        a = 'xuancheng'
                    elif vi == '合肥':
                        a = 'hefei'
                    elif vi == '亳州':
                        a = 'bozhou'
                    elif vi == '夏':
                        a = 'xia'
                    elif vi == '滁州':
                        a = 'xuzhou'
                    elif vi == '春':
                        a = 'chun'
                    elif vi == '秋':
                        a = 'qiu'
                    elif vi == '冬':
                        a = 'dong'
                    elif vi == '蚌埠':
                        a = 'xufeng'
                    elif vi == '池州':
                        a = 'chizhou'
                    elif vi == '芜湖':
                        a = 'wuhu'
                    elif vi == '阜阳':
                        a = 'fuyang'
                    elif vi == '淮北':
                        a = 'huaibei'
                    elif vi == '淮南':
                        a = 'huainan'
                    elif vi == '黄山':
                        a = 'huangshan'
                    elif vi == '六安':
                        a = 'luan'
                    elif vi == '马鞍山':
                        a = 'maanshan'
                    elif vi == '铜陵':
                        a = 'tongling'
                    elif vi == '宿州':
                        a = 'suzhou'
                    table2.write(sz, k, a)
                    k = k + 1
                print sz
                sz += 1
                init()
                vis = 0
            info['SO2'] = table.row(i)[list.index('SO2')].value
            info['NO2'] = table.row(i)[list.index('NO2')].value
            info['PM10'] = table.row(i)[list.index('PM10')].value
            info['CO'] = table.row(i)[list.index('CO-1h')].value
            info['O3'] = table.row(i)[list.index('O3')].value
            info['PM25'] = table.row(i)[list.index('PM2.5')].value
    else :
        if vis == 0:
           vis = 1;
           "{:0 > 2d}"
           info['城市'] =  table.row(i)[list.index('城市')].value
           info['季节'] = table.row(i)[list.index('季节')].value
           info['开始时间'] = table.row(i)[list.index('年')].value + \
                          table.row(i)[list.index('月')].value + \
                          table.row(i)[list.index('日')].value + \
                          table.row(i)[list.index('时次')].value
           info['降水时间'] = 0
           info['降水总量'] = 0
           info['最大降水量'] = 0
           info['最大风速'] = 0  # 风速
           info['最大风速对应风向'] = 0
           info['平均降水强度'] = 0
           info['降水时段平均风速'] = 0

        info['结束时间'] = table.row(i)[list.index('年')].value + \
                          table.row(i)[list.index('月')].value + \
                          table.row(i)[list.index('日')].value + \
                          table.row(i)[list.index('时次')].value
        info['降水时间'] += 1
        info['降水总量'] += table.row(i)[list.index('降水量(毫米)')].value
        info['最大降水量'] = max(info['最大降水量'], table.row(i)[list.index('降水量(毫米)')].value)
        if info['最大风速'] < table.row(i)[list.index('最大风速(米/秒)')].value :
            info['最大风速'] = table.row(i)[list.index('最大风速(米/秒)')].value
            info['最大风速对应风向'] = table.row(i)[list.index('最大风速的风向(度)')].value
        info['平均降水强度'] += table.row(i)[list.index('降水量(毫米)')].value
        info['降水时段平均风速'] += table.row(i)[list.index('最大风速(米/秒)')].value


res.save('demo1.xlsx')