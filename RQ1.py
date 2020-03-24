from datetime import datetime

import openpyxl
import pandas

df = pandas.read_excel('RQ1_RuleData.xlsx')

df['date_added'] = pandas.to_datetime(df['date_added'], format='%m/%d/%y')
df['date_removed'] = pandas.to_datetime(df['date_removed'], format='%m/%d/%y')
df['date_removed'] = df['date_removed'].map(lambda x: datetime.max if pandas.isnull(x) else x)

issue_dict = {}
for idx, row in df.iterrows():
    issue_info = (
        idx,
        row['rule'],
        row['date_added'],
        row['date_removed'],
    )
    issue_dict.setdefault(row['filename'], [])
    issue_dict[row['filename']].append(issue_info)


pair_bucket = []
for f, arr in issue_dict.items():

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i][1] != arr[j][1] and arr[i][3] >= arr[j][2]) and (arr[i][2] <= arr[j][3]):
                pair_bucket.append((f, arr[i], arr[j]))



wb = openpyxl.load_workbook('RQ2_Result_CoOccur.xlsx')
sheet = wb.get_sheet_by_name('RQ2')
row1 = ('filename','i1_id','i1_rule','i1_date_added','i1_date_removed','i2_id','i2_rule','i2_date_added','i2_date_removed')
sheet.append(row1)


for pair in pair_bucket:
    row = (
        pair[0],
        pair[1][0],
        pair[1][1],
        pair[1][2].strftime('%Y-%m-%d'),
        pair[1][3].strftime('%Y-%m-%d') if pair[1][3] < datetime.max else '',
        pair[2][0],
        pair[2][1],
        pair[2][2].strftime('%Y-%m-%d'),
        pair[2][3].strftime('%Y-%m-%d') if pair[2][3] < datetime.max else '',
    )
    sheet.append(row)
    print(row)


wb.save('RQ2_Result_CoOccur.xlsx')

