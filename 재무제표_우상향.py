import pandas as pd
import numpy as np
import math
import mglearn
import get_stock_price as gsp

from sklearn.linear_model import LinearRegression
def sort_리츠(comp_name):
    if comp_name[-2:] == '리츠':
        return np.nan
    else:

        return comp_name


def make_csv_상승율_연간():
    옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
    연간_df = pd.read_csv('./data/20_4분기/연간_df_with_업종.csv')
    연간_df =연간_df.drop('Unnamed: 0',axis = 1)
    연간_df['회사코드(clean)'] = 연간_df['회사코드'].apply(lambda x : str(x).zfill(6))
    연간_df = 연간_df.replace([np.inf, -np.inf,0], np.nan)
    연간_df['회사이름'] = 연간_df['회사이름'].apply(sort_리츠)


    옥수치17_12_not_null = pd.notnull(연간_df["옥수치17/12"])
    옥수치18_12_not_null = pd.notnull(연간_df["옥수치18/12"])
    옥수치19_12_not_null = pd.notnull(연간_df["옥수치19/12"])
    #옥수치20_09_not_null = pd.notnull(연간_df["옥수치20/09"])
    옥수치20_12_not_null = pd.notnull(연간_df["옥수치20/12"])
    회사이름_not_null = pd.notnull(연간_df["회사이름"])

    연간_df = 연간_df[회사이름_not_null & 옥수치20_12_not_null &옥수치19_12_not_null & 옥수치18_12_not_null]
    print(연간_df)

    상승세_df = pd.DataFrame(columns=['회사코드','상승율','업종'])
    for stock_code in 연간_df['회사코드(clean)']:

        연간_temp_df = 연간_df[연간_df['회사코드(clean)'] == stock_code ]
        연간_옥수치_list = 연간_temp_df[['옥수치17/12','옥수치18/12','옥수치19/12','옥수치20/12',]]
        연간_옥수치_list = 연간_옥수치_list.dropna(axis = 1).values[0]
        x = list(range(0,len(연간_옥수치_list)))
        if len(x) < 2:
            continue
        y = np.reshape(연간_옥수치_list,(-1, 1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        new_row = {'회사코드':stock_code,'상승율':lr.coef_[0,0],'업종':연간_df[연간_df['회사코드(clean)'] == stock_code]['업종'].values[0]}
        상승세_df = 상승세_df.append(new_row,ignore_index=True)
        print(stock_code)
        #print(type(연간_df[연간_df['회사코드(clean)'] == stock_code]['업종'].values[0]))
        
    상승세_df.to_csv('./data/20_4분기/상승율_17_20.csv')



def make_csv_상승율_분기():
    옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
    연간_df = pd.read_csv('./data/연간_df.csv')
    연간_df =연간_df.drop('Unnamed: 0',axis = 1)
    연간_df['회사코드(clean)'] = 연간_df['회사코드'].apply(lambda x : str(x).zfill(6))
    연간_df = 연간_df.replace([np.inf, -np.inf,0], np.nan)
    연간_df['회사이름'] = 연간_df['회사이름'].apply(sort_리츠)


    옥수치17_12_not_null = pd.notnull(연간_df["옥수치17/12"])
    옥수치18_12_not_null = pd.notnull(연간_df["옥수치18/12"])
    옥수치19_12_not_null = pd.notnull(연간_df["옥수치19/12"])
    옥수치20_09_not_null = pd.notnull(연간_df["옥수치20/09"])
    회사이름_not_null = pd.notnull(연간_df["회사이름"])

    연간_df = 연간_df[회사이름_not_null & 옥수치20_09_not_null &옥수치19_12_not_null & 옥수치18_12_not_null]


    상승세_df = pd.DataFrame(columns=['회사코드','상승율'])
    for stock_code in 연간_df['회사코드(clean)']:

        연간_temp_df = 연간_df[연간_df['회사코드(clean)'] == stock_code ]
        연간_옥수치_list = 연간_temp_df[['옥수치17/12','옥수치18/12','옥수치19/12']]#,'옥수치20/09']]
        연간_옥수치_list = 연간_옥수치_list.dropna(axis = 1).values[0]
        x = list(range(0,len(연간_옥수치_list)))
        #if len(x) < 2:
            #continue
        y = np.reshape(연간_옥수치_list,(-1, 1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        new_row = {'회사코드':stock_code,'상승율':lr.coef_[0,0]}
        상승세_df = 상승세_df.append(new_row,ignore_index=True)
        print(stock_code)
    상승세_df.to_csv('./data/상승율_17_19.csv')
def make_csv_상승율_상승율_17_20_연간():
    옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
    연간_df = pd.read_csv('./data/연간_df.csv')
    연간_df =연간_df.drop('Unnamed: 0',axis = 1)
    연간_df['회사코드(clean)'] = 연간_df['회사코드'].apply(lambda x : str(x).zfill(6))
    연간_df = 연간_df.replace([np.inf, -np.inf,0], np.nan)
    연간_df['회사이름'] = 연간_df['회사이름'].apply(sort_리츠)


    옥수치17_12_not_null = pd.notnull(연간_df["옥수치17/12"])
    옥수치18_12_not_null = pd.notnull(연간_df["옥수치18/12"])
    옥수치19_12_not_null = pd.notnull(연간_df["옥수치19/12"])
    옥수치20_09_not_null = pd.notnull(연간_df["옥수치20/09"])
    회사이름_not_null = pd.notnull(연간_df["회사이름"])

    연간_df = 연간_df[회사이름_not_null & 옥수치20_09_not_null]


    상승세_df = pd.DataFrame(columns=['회사코드','상승율'])
    for stock_code in 연간_df['회사코드(clean)']:

        연간_temp_df = 연간_df[연간_df['회사코드(clean)'] == stock_code ]
        연간_옥수치_list = 연간_temp_df[['옥수치17/12','옥수치18/12','옥수치19/12','옥수치20/09']]
        연간_옥수치_list['옥수치20/09'] = 연간_옥수치_list['옥수치20/09'] + 연간_옥수치_list['옥수치20/09'] / 3
        연간_옥수치_list = 연간_옥수치_list.dropna(axis = 1).values[0]
        x = list(range(0,len(연간_옥수치_list)))
        if len(x) < 2:
            continue

        y = np.reshape(연간_옥수치_list,(-1, 1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        new_row = {'회사코드':stock_code,'상승율':lr.coef_[0,0]}
        상승세_df = 상승세_df.append(new_row,ignore_index=True)
        print(stock_code)
    상승세_df.to_csv('./data/상승율_17_20.csv')


def make_csv_주가_상승율_17_20_연간():
    #옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
    상승율_17_20 = pd.read_csv('./data/상승율_17_20.csv')
    상승율_17_20 = 상승율_17_20.drop('Unnamed: 0',axis = 1)
    상승율_17_20['회사코드'] = 상승율_17_20['회사코드'].apply(lambda x : str(x).zfill(6))
    상승세_df = pd.DataFrame(columns=['회사코드','주가상승율'])

    for stock_code in 상승율_17_20['회사코드']:
        price_df = gsp.get_stockData_2_dataframe(stock_code,'2017-01-01','2020-12-31')
        y = price_df['Close'].values
        x = list(range(0,len(y)))
        if len(y) <= 1:
            continue
        y = np.reshape(y,(-1, 1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        new_row = {'회사코드':stock_code,'주가상승율':lr.coef_[0,0]}
        상승세_df = 상승세_df.append(new_row,ignore_index=True)
        print(stock_code)
    상승세_df.to_csv('./data/주가상승율_17_20.csv')

    상승율_df = pd.read_csv('./data/상승율_17_20.csv')
    상승율_df = 상승율_df.drop('Unnamed: 0',axis = 1)
    주가상승율_df = pd.read_csv('./data/주가상승율_17_20.csv')
    주가상승율_df = 주가상승율_df.drop('Unnamed: 0',axis = 1)
    sum_df = pd.merge(상승율_df,주가상승율_df,on='회사코드')
    sum_df[sum_df['상승율'] > sum_df['주가상승율']]
    print(sum_df)

def make_csv_주가_상승율_19_분기():
    #옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
    상승율_17_20 = pd.read_csv('./data/상승율_17_20.csv')
    상승율_17_20 = 상승율_17_20.drop('Unnamed: 0',axis = 1)
    상승율_17_20['회사코드'] = 상승율_17_20['회사코드'].apply(lambda x : str(x).zfill(6))
    상승세_df = pd.DataFrame(columns=['회사코드','주가상승율'])

    for stock_code in 상승율_17_20['회사코드']:
        price_df = gsp.get_stockData_2_dataframe(stock_code,'2017-01-01','2020-12-31')
        y = price_df['Close'].values
        x = list(range(0,len(y)))
        if len(y) <= 1:
            continue
        y = np.reshape(y,(-1, 1))
        x = np.reshape(x, (-1, 1))
        lr = LinearRegression().fit(x,y)
        new_row = {'회사코드':stock_code,'주가상승율':lr.coef_[0,0]}
        상승세_df = 상승세_df.append(new_row,ignore_index=True)
        print(stock_code)
    상승세_df.to_csv('./data/주가상승율_17_20.csv')

    상승율_df = pd.read_csv('./data/상승율_17_20.csv')
    상승율_df = 상승율_df.drop('Unnamed: 0',axis = 1)
    주가상승율_df = pd.read_csv('./data/주가상승율_17_20.csv')
    주가상승율_df = 주가상승율_df.drop('Unnamed: 0',axis = 1)
    sum_df = pd.merge(상승율_df,주가상승율_df,on='회사코드')
    sum_df[sum_df['상승율'] > sum_df['주가상승율']]
    print(sum_df)












