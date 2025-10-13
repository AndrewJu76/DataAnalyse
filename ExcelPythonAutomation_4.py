import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('OrderHistory.xlsx')

simplified_df = df.groupby('Order Type')
simplified_df['Sales Amount'].mean().plot.pie()
plt.show()
