import pandas as pd
import os

# df1 = pd.read_excel('Project1.xlsx')
# df2 = pd.read_excel('Project2.xlsx')
#
# print(df1)
# print(df2)

dfs = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xlsx'):
            df = pd.read_excel(file)
            dfs.append(df)
    # print(root)
    # print(dirs)
    # print(files)

# pandas 默认会把第一行当作列名（表头）‌，这是 read_csv() 和 read_excel() 的默认行为，对应参数 header=0
# 添加 年终奖金
for df in dfs:
    df['年终奖'] = ''
    for index, row in df.iterrows():
        score = row['绩效']
        group = row['项目组']
        if group == '项目组1':
            row['项目组'] = '项目组3'
        bonus = 0
        if score > 95:
            bonus = 8000
        elif score > 70:
            bonus = 7000
        else:
            bonus = 4000
        # print(index,row['绩效'],row['项目组'])
        row['年终奖'] = bonus
        # 必须要重新赋值回去
        df.iloc[index] = row

# 合并表格
new_df = pd.concat(dfs,ignore_index=True)
# print(new_df)

new_df.to_excel('new_project.xlsx',index=False)