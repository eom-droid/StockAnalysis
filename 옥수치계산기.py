import financial_statements as fs
import get_stock_listed as gsl
import time
import random
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import finance_data_class as fi_class
import get_stock_listed as gsl



list_of_stock =  gsl.get_df()
list_of_stock['종목코드(clean)'] = list_of_stock['종목코드'].apply(lambda x : str(x).zfill(6))


#print(list_of_stock)
분기_df = pd.DataFrame(columns=['회사이름','회사코드','옥수치19/12','옥수치20/03','옥수치20/06','옥수치20/09'])
연간_df = pd.DataFrame(columns=['회사이름','회사코드','옥수치17/12','옥수치18/12','옥수치19/12','옥수치20/09'])
이상한_데이터 = pd.DataFrame(columns= ['회사이름','회사코드'])
#files = open('./over_10%.txt','w')


indexsss = 0

for stock_code in list_of_stock['종목코드(clean)']:
    try:
        html = open('./html/'+stock_code+'.html','r',encoding='utf-8')
        bsObject = BeautifulSoup(html, "html.parser")
    except:
        print('시발')
        continue
    fi1 = fi_class.Financial_Statements(bsObject,stock_code)
    연간_series = fi1.옥_수식_연간()
    분기_series = fi1.옥_수식_분기()
    

    회사이름 = list_of_stock.loc[list_of_stock['종목코드(clean)'] == stock_code,'회사명'].values[0]
    회사코드 = stock_code
    분기_df.loc[indexsss] = [회사이름,회사코드,분기_series[0],분기_series[1],분기_series[2],분기_series[3]]
    연간_df.loc[indexsss] = [회사이름,회사코드,연간_series[0],연간_series[1],연간_series[2],연간_series[3]]
    indexsss += 1


분기_df.to_csv('./분기_df.csv')
연간_df.to_csv('./연간_df.csv')



분기_df = pd.read_csv('./분기_df.csv')
연간_df = pd.read_csv('./연간_df.csv')
분기_df = 분기_df.drop('Unnamed: 0',axis = 1)
연간_df = 연간_df.drop('Unnamed: 0',axis = 1)

for i in list_of_stock['종목코드']:
    분기_df.loc[분기_df['회사코드'] == i,'업종'] = list_of_stock.loc[list_of_stock['종목코드'] == i,'업종'].values[0]
    연간_df.loc[연간_df['회사코드'] == i,'업종'] = list_of_stock.loc[list_of_stock['종목코드'] == i,'업종'].values[0]

분기_df.to_csv('./분기_df_with_업종.csv')
연간_df.to_csv('./연간_df_with_업종.csv')