from datetime import datetime
from datetime import timedelta
import pandas
import numpy as np
import xlsxwriter

df = pandas.read_excel('RQ2_Result_FinalCoOccur')

rule = []
for idx_rule, row_rule in df.iterrows():
    rule_info = (
        idx_rule,
        row_rule['source'],
        row_rule['target'],
        row_rule['weight']
    )
    rule.append(rule_info)

co_rule = []
k = 0
for i in range(len(rule)):
    for j in range(i+1,len(rule)):
        if(rule[i][1] == rule[j][2] and rule[i][2] == rule[j][1] and rule[i][3] >= rule[j][3]):
            co_rule.append(rule[i])
        if (rule[i][1] == rule[j][2] and rule[i][2] == rule[j][1] and rule[i][3] < rule[j][3]):
            co_rule.append(rule[j])

workbook = xlsxwriter.Workbook('RQ3_Result_OrderByLift.xls')
sheetRQ1 = workbook.add_worksheet('Days')

print(co_rule)

for i in range(0, len(co_rule)):
    for j in range(0, len(co_rule[i])):
        sheetRQ1.write(i, j, co_rule[i][j])

workbook.close()

print(co_rule)
