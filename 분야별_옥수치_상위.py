import pandas as pd




연간_옥수치_df = pd.read_csv('./data/연간_df_with_업종.csv')
연간_옥수치_df = 연간_옥수치_df.drop('Unnamed: 0',axis = 1)
업종 = list(연간_옥수치_df['업종'].value_counts().index)
업종별_1위_df = pd.DataFrame()
#print(연간_옥수치_df['업종'].value_counts().tail(50))
'''
for 업종_개별 in 업종:
#업종_개별 = '특수 목적용 기계 제조업'
    sorted_df = 연간_옥수치_df[연간_옥수치_df['업종'] == 업종_개별].sort_values(by = '옥수치20/09',ascending = False).reset_index().drop('index',axis = 1)
    업종별_1위_df = 업종별_1위_df.append(sorted_df.loc[0])
#업종_개별 = '특수 목적용 기계 제조업'

업종별_1위_df.to_csv('./data/업종별1위.csv')
'''


업종_개별 = '건축기술, 엔지니어링 및 관련 기술 서비스업'


sorted_df = 연간_옥수치_df[연간_옥수치_df['업종'] == 업종_개별].sort_values(by = '옥수치20/09',ascending = False).reset_index().drop('index',axis = 1)

print(sorted_df)