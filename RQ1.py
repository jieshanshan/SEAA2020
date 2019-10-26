from datetime import datetime

import pandas
import numpy as np
import xlwt


df = pandas.read_excel('FileData.xlsx', sheet_name = 'FileDate')

df['date_changed'] = pandas.to_datetime(df['date_changed'], format='%Y-%m-%d')

file_date = []
for idx1, row1 in df.iterrows():
    file_info = (
        idx1,
        row1['projectname'],
        row1['filename'],
        row1['date_changed'],
    )
    file_date.append(file_info)


df = pandas.read_excel('RuleDate.xlsx', sheet_name = 'RuleDate')

df['date_added'] = pandas.to_datetime(df['date_added'], format='%Y-%m-%d')
df['date_removed'] = pandas.to_datetime(df['date_removed'], format='%Y-%m-%d')
df['date_removed'] = df['date_removed'].map(lambda x: datetime.max if pandas.isnull(x) else x)

issue_date = []
for idx2, row2 in df.iterrows():
    issue_info = (
        idx2,
        row2['filename'],
        row2['rule'],
        row2['date_added'],
        row2['date_removed'],
    )
    issue_date.append(issue_info)


for i in range(len(file_date)):
    for j in range(len(issue_date)):
        if (file_date[i][2] == issue_date[j][1] and issue_date[j][3] <= file_date[i][3] <= issue_date[j][4]):
            file_date[i] = np.append(file_date[i], issue_date[j][2])


print(file_date)

workbook = xlwt.Workbook()
sheetRQ1 = workbook.add_sheet('RQ1', cell_overwrite_ok=True)

for i in range(0, len(file_date)):
    for j in range(0, len(file_date[i])):
        sheetRQ1.write(i, j, file_date[i][j])
workbook.save('RQ1_Result.xls')


