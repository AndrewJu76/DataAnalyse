import pandas as pd
import matplotlib.pyplot as plt

raw_df = pd.read_csv('./smartphone_cleaned_v5.csv')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('max_colwidth',100)

raw_df.loc[raw_df['rating'].isnull(),'rating'] = raw_df['rating'].mean()
raw_df.loc[raw_df['num_cores'].isnull(),'num_cores'] = raw_df['num_cores'].median()
raw_df.loc[raw_df['fast_charging'].isnull(),'fast_charging'] = raw_df['fast_charging'].value_counts().index[0]

max_df = raw_df.groupby('brand_name')['price'].max()
min_df = raw_df.groupby('brand_name')['price'].min()
result_df = pd.concat([max_df,min_df],axis=1)
result_df.columns = ['max_price','min_price']
result_df = result_df.reset_index()
result_df.plot(x='brand_name',y=['max_price','min_price'],kind = 'bar')
plt.show()

brand_count = raw_df['brand_name'].value_counts().head(20)
brand_count.columns = ['brand_name','count']
brand_count.plot(kind = 'pie',legend = False,autopct='%.1f%%')
plt.show()





