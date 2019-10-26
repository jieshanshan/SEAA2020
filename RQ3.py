from datetime import datetime
from datetime import timedelta
import pandas
import numpy as np
import xlsxwriter

df = pandas.read_excel('RQ2Selection.xlsx', sheet_name = 'Select')

rule = []
for idx_rule, row_rule in df.iterrows():
    rule_info = (
        idx_rule,
        row_rule['source'],
        row_rule['target'],
    )
    rule.append(rule_info)

co_rule = []
k = 0
for i in range(len(rule)):
    for j in range(i+1,len(rule)):
        if(rule[i][1] == rule[j][2] and rule[i][2] == rule[j][1]):
            co_rule.append(rule[i])


df = pandas.read_excel('RQ3Data.xlsx', sheet_name = 'Sheet1')

df['i1_date_added'] = pandas.to_datetime(df['i1_date_added'], format='%Y-%m-%d')
df['i2_date_added'] = pandas.to_datetime(df['i2_date_added'], format='%Y-%m-%d')

file_date = []
for idx_file, row_file in df.iterrows():
    file_info = (
        idx_file,
        row_file['projectname'],
        row_file['filename'],
        row_file['i1_rule'],
        row_file['i1_date_added'],
        row_file['i2_rule'],
        row_file['i2_date_added'],
    )
    file_date.append(file_info)

interval = 0

for i in range(len(co_rule)):
    for j in range(len(file_date)):
        if (co_rule[i][1] == file_date[j][3] and co_rule[i][2] == file_date[j][5]):
            interval = (file_date[j][4] - file_date[j][6]).days
            co_rule[i] = np.append(co_rule[i], interval)
            co_rule[i] = co_rule[i].astype(object)
        if(co_rule[i][1] == file_date[j][5] and co_rule[i][2] == file_date[j][3]):
            interval = (file_date[j][6] - file_date[j][4]).days
            co_rule[i] = np.append(co_rule[i], interval)
            co_rule[i] = co_rule[i].astype(object)


workbook = xlsxwriter.Workbook('RQ3Results.xls')
sheetRQ1 = workbook.add_worksheet('Days')

print(co_rule)

for i in range(0, len(co_rule)):
    for j in range(0, len(co_rule[i])):
        sheetRQ1.write(i, j, co_rule[i][j])

workbook.close()