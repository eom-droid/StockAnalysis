import pandas as pd
import numpy as np
import get_stock_price as gsp
from pykrx import stock
import math
from sklearn.linear_model import LinearRegression




def is_리츠(comp_name):
    if comp_name[-2:] == '리츠':
        return True
    else:
        #print(comp_name)
        return False

###################### 시총이랑 비교
df_시가총액 = stock.get_market_cap_by_ticker("20210423").reset_index()
# df_주식가격 = gsp.print_stockData('005930','2018-01')
df_4분기 = pd.read_csv('./data/20_4분기/분기_df_with_업종.csv')
df_4분기 = df_4분기.drop('Unnamed: 0',axis = 1)
df_4분기['회사코드'] = df_4분기['회사코드'].apply(lambda x : str(x).zfill(6))

series_of_업종 = df_4분기['업종'].value_counts()
list_of_업종 = list(series_of_업종.index)
list_of_업종_평균_옥수치 = []
#result_df = df_4분기.copy()
###################### 시총이랑 비교
#df_시가총액 = df_시가총액[df_시가총액['시가총액'] < 200000000000]
for 업종 in list_of_업종:
    a = df_4분기[df_4분기['업종'] == 업종]['옥수치20/09'].mean()
    list_of_업종_평균_옥수치.append(a)
dict_of_업종 = dict(zip(list_of_업종, list_of_업종_평균_옥수치))

result_df = pd.merge(df_4분기,df_시가총액,left_on = '회사코드',right_on = '티커')
result_df = result_df[result_df['시가총액'] < 100000000000]






#result_df['회사이름'] = result_df['회사이름'].apply(sort_리츠)
#result_df['순위'] = result_df[result_df['옥수치20/12']]
for ind in result_df.index:
    현재_업종 = result_df.loc[ind,'업종']
    현재_옥수치_2012 = result_df.loc[ind,'옥수치20/12']
    현재_회사코드 = result_df.loc[ind,'회사코드']
    if is_리츠(result_df.loc[ind,'회사이름']):
        result_df = result_df.drop(ind)
        continue
    if math.isnan(현재_옥수치_2012):
        result_df = result_df.drop(ind)
        continue
    if 현재_옥수치_2012 <= 0:
        result_df = result_df.drop(ind)
        continue
    if dict_of_업종[현재_업종] > 현재_옥수치_2012:
        result_df = result_df.drop(ind)
        continue



    stock_price_df = gsp.get_stockData_2_dataframe(현재_회사코드,'2021-01-01')
    stock_price_series = stock_price_df['Close'].values
    
    x = list(range(0,len(stock_price_series)))
    if len(x) < 2:
        continue
    y = np.reshape(stock_price_series,(-1,1))
    x = np.reshape(x, (-1, 1))
    lr = LinearRegression().fit(x,y)
    new_row = {'회사코드':현재_회사코드,'주가상승율':lr.coef_[0,0]}

    #주가 상승율 반영
    if lr.coef_[0,0] <= 0.00000001:
        result_df = result_df.drop(ind)
        continue
    if lr.coef_[0,0] >= 4:
        result_df = result_df.drop(ind)
        continue
    print(new_row)











    
result_df['옥수치20/03'] = round(result_df['옥수치20/03'],3)
result_df['옥수치20/06'] = round(result_df['옥수치20/06'],3)
result_df['옥수치20/09'] = round(result_df['옥수치20/09'],3)
result_df['옥수치20/12'] = round(result_df['옥수치20/12'],3)
a = list(result_df.columns.values)
b = a[0:7]
b.append(a[9])

result_df = result_df[b]
result_df.to_csv('temp.csv')

