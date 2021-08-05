import pandas as pd
import get_stock_price as gsp
from sklearn.linear_model import LinearRegression
import numpy as np
def 상승율10_옥수치_1():
    상승율_df = pd.read_csv('./data/상승율_17_19.csv')
    상승율_df = 상승율_df.drop('Unnamed: 0',axis = 1)
    연간_옥수치_df = pd.read_csv('./data/연간_df_with_업종.csv')
    연간_옥수치_df = 연간_옥수치_df.drop('Unnamed: 0',axis = 1)


    상승율_df = pd.merge(상승율_df,연간_옥수치_df,on = '회사코드')
    상승율 = (상승율_df['상승율'] > 10)
    옥수치_nonminus_19 = (상승율_df['옥수치19/12']>1)
    옥수치_nonminus_20 = (상승율_df['옥수치20/09']>1)
    상승율10이상_옥수치1이상 = 상승율_df[상승율 & 옥수치_nonminus_19 & 옥수치_nonminus_20].copy()
    print(상승율10이상_옥수치1이상[상승율10이상_옥수치1이상['옥수치19/12'] < 상승율10이상_옥수치1이상['옥수치20/09']])
def 상승율05_옥수치_1():
    상승율_df = pd.read_csv('./data/상승율_17_19.csv')
    상승율_df = 상승율_df.drop('Unnamed: 0',axis = 1)
    연간_옥수치_df = pd.read_csv('./data/연간_df_with_업종.csv')
    연간_옥수치_df = 연간_옥수치_df.drop('Unnamed: 0',axis = 1)


    상승율_df = pd.merge(상승율_df,연간_옥수치_df,on = '회사코드')
    상승율 = (상승율_df['상승율'] > 0.5)
    #옥수치_nonminus_19 = (상승율_df['옥수치19/12']>1)
    옥수치_nonminus_20 = (상승율_df['옥수치20/09']>20)
    temp_df = 상승율_df[상승율 & 옥수치_nonminus_20].copy()
    print(temp_df[temp_df['옥수치19/12'] < temp_df['옥수치20/09']])

def 상승율05():
    상승율_df = pd.read_csv('./data/상승율_17_19.csv')
    상승율_df = 상승율_df.drop('Unnamed: 0',axis = 1)
    연간_옥수치_df = pd.read_csv('./data/연간_df_with_업종.csv')
    연간_옥수치_df = 연간_옥수치_df.drop('Unnamed: 0',axis = 1)


    상승율_df = pd.merge(상승율_df,연간_옥수치_df,on = '회사코드')
    상승율 = (상승율_df['상승율'] > 0.5)
    #옥수치_nonminus_19 = (상승율_df['옥수치19/12']>1)
    옥수치_nonminus_20 = (상승율_df['옥수치20/09']>10)
    temp_df = 상승율_df[상승율 & 옥수치_nonminus_20].copy()
    temp_df = temp_df[temp_df['업종'] != '의료용품 및 기타 의약 관련제품 제조업']
    temp_df.head(50)
    temp_df.to_csv('./temp.csv')
    #print()




상승율05()
def 상승율과주가_corr():
    상승율_df = pd.read_csv('./data/상승율_17_20.csv')
    상승율_df = 상승율_df.drop('Unnamed: 0',axis = 1)
    주가상승율_df = pd.read_csv('./data/주가상승율_17_20.csv')
    주가상승율_df = 주가상승율_df.drop('Unnamed: 0',axis = 1)
    sum_df = pd.merge(상승율_df,주가상승율_df,on='회사코드')
    sum_df['회사코드'] = sum_df['회사코드'].apply(lambda x : str(x).zfill(6))
    sum_df = sum_df[sum_df['상승율'] > 0]
    sum_df = sum_df[sum_df['주가상승율'] > 0]
    sum_df[sum_df['상승율'] > sum_df['주가상승율']]
    print(sum_df)
    #연간_옥수치_df = pd.read_csv('./data/연간_df_with_업종.csv')
    #연간_옥수치_df = 연간_옥수치_df.drop('Unnamed: 0',axis = 1)
    
    #stock_code = '005930'
    #stock_price_df = gsp.get_stockData_2_dataframe(stock_code,'2019-01-01','2020-12-31')

    #print(stock_price_df)



def 주가상승율():
    temp_df = pd.read_csv('./temp.csv')
    temp_df['회사코드'] = temp_df['회사코드'].apply(lambda x : str(x).zfill(6))
    temp_df = temp_df.drop('Unnamed: 0',axis = 1)
    temp_df = temp_df.set_index('회사코드')
    temp_df = temp_df.drop(['옥수치17/12','옥수치18/12','옥수치19/12'],axis = 1)
    for stock_code in temp_df.index:
        stock_price_df = gsp.get_stockData_2_dataframe(stock_code,'2020-01-01')
        stock_price_series = stock_price_df['Close'].values
        
        x = list(range(0,len(stock_price_series)))
        if len(x) < 2:
            continue
        y = np.reshape(stock_price_series,(-1,1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        #회사이름 = temp_df.loc[temp_df['회사코드'] == stock_code,'회사이름']
        new_row = {'회사코드':stock_code,'주가상승율':lr.coef_[0,0]}
        #index_temp += 1
        #sum_temp = lr.coef_[0,0]
        #to_csv_temp.append(new_row)
        
        if lr.coef_[0,0] > -0.008498646024521404:
            temp_df = temp_df.drop(stock_code)
        else:
            print(new_row)
    #print(sum_temp/index_temp)
    temp_df.to_csv('./temp_under_0.008.csv')

주가상승율()

'''
    y = price_df['Close'].values
        x = list(range(0,len(y)))
        if len(y) <= 1:
            continue
        y = np.reshape(y,(-1, 1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        new_row = {'회사코드':stock_code,'주가상승율':lr.coef_[0,0]}
        상승세_df = 상승세_df.append(new_row,ignore_index=True)
        print(stock_code)'''