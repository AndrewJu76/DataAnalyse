import pandas as pd

excel_file = 'Pandas_Workbook.xlsx'
df = pd.read_excel(excel_file)
print(df)

# print(df['Name'].where(df['Occupation'] == 'Programe_1'))
# programmers = df['Name'].where(df['Occupation'] == 'Programe_1')
# print(programmers.dropna())

excel_files = ['Pandas_Workbook.xlsx','Pandas_Workbook_copy.xlsx','Pandas_Workbook_copy_2.xlsx']

for individual_file in excel_files:
    df = pd.read_excel(individual_file)
    programmers = df['Name'].where(df['Occupation'] == 'Programe_1').dropna()
    print('File Name' + individual_file)
    print(programmers)