import pandas as pd
import numpy as np

score_df = pd.read_excel('sample_scores.xlsx')

score_df['average'] = score_df.mean(axis=1,skipna=True,numeric_only=True)
score_df['Pass/Fail'] = np.where(score_df['average']>60,'Pass','Fail')

print(score_df)