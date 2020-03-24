from datetime import datetime
from datetime import timedelta
import pandas
import numpy as np
import xlwt
import xlsxwriter

df = pandas.read_excel('RQ2_Result_TopTen.xlsx', sheet_name = 'TopTen')

rule = []
for idx_co, row_co in df.iterrows():
    co_info = (
        idx_co,
        row_co['source'],
        row_co['target'],
    )
    rule.append(co_info)

co_rule = []
k = 0
for i in range(len(rule)):
    for j in range(i+1,len(rule)):
        if(rule[i][1] == rule[j][2] and rule[i][2] == rule[j][1]):
            co_rule.append(rule[i])
#            co_rule[k] = np.append(co_rule[k], rule[i])
#            k = k+1

workbook = xlsxwriter.Workbook('RQ2_Result_CoOccur.xls')
sheetRQ1 = workbook.add_worksheet('RQ2_CoOccur')

print(co_rule)

for i in range(0, len(co_rule)):
    for j in range(0, len(co_rule[i])):
        sheetRQ1.write(i, j, co_rule[i][j])

workbook.close()
