import csv
import numpy as np
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += int(num[i])
    return nsum / len(num)
with open("/Users/rockter/test.csv","r",encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    cxsj = []
    xbsw = []
    slx = []
    for row in reader:
        cxsj.append(row['程序设计'])
        xbsw.append(row['细胞生物'])
        slx.append(row['生理学'])
cxsj.sort()
max_cxsj=cxsj[len(cxsj)-1]
min_cxsj=cxsj[0]
averagenum_cxsj=averagenum(cxsj)
print("程序设计平均分为",averagenum_cxsj)
print("程序设计分数最高为：",max_cxsj)
print("程序设计分数最低为",min_cxsj)

xbsw.sort()
max_xbsw=xbsw[len(xbsw)-1]
min_xbsw=xbsw[0]
averagenum_xbsw=averagenum(xbsw)
print("程序设计平均分为",averagenum_xbsw)
print("程序设计分数最高为：",max_xbsw)
print("程序设计分数最低为",min_xbsw)

slx.sort()
max_slx=slx[len(slx)-1]
min_slx=slx[0]
averagenum_slx=averagenum(slx)
print("程序设计平均分为",averagenum_slx)
print("程序设计分数最高为：",max_slx)
print("程序设计分数最低为",min_slx)
