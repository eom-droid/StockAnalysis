
import financial_statements as fs
import get_stock_listed as gsl
import time
import random
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import finance_data_class as fi_class
import get_stock_listed as gsl
import get_stock_price as stock_price_fuc
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

def sort_리츠(comp_name):
    if comp_name[-2:] == '리츠':
        return np.nan
    else:
        #print(comp_name)
        return comp_name
#옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
분기_df = pd.read_csv('./분기_df_with_업종.csv')
분기_df =분기_df.drop('Unnamed: 0',axis = 1)
분기_df['회사코드(clean)'] = 분기_df['회사코드'].apply(lambda x : str(x).zfill(6))
#print(분기_df.dropna(axis = 0))
분기_df = 분기_df.replace([np.inf, -np.inf,0], np.nan)
분기_df['회사이름'] = 분기_df['회사이름'].apply(sort_리츠)
분기_df = 분기_df.dropna(axis = 0)
옥수치2009_over_10_per = 분기_df[분기_df['옥수치20/09'] >= 10].copy()

옥수치_주가_corr_df = pd.read_csv('./옥수치_주가_corr_df.csv')
옥수치_주가_corr_df['회사코드(clean)'] = 옥수치_주가_corr_df['회사코드'].apply(lambda x : str(x).zfill(6))
옥수치_주가_corr_df = 옥수치_주가_corr_df[옥수치_주가_corr_df['corr'] > 0.7]
corr_회사이름 = list(옥수치_주가_corr_df['회사코드(clean)'].values)
옥수치_10_per = list(옥수치2009_over_10_per['회사코드(clean)'].values)
#intersection = list(set(lst1) & set(lst2))
#print( intersection ) # ['C', 'D']

for i in list(set(옥수치_10_per) & set(corr_회사이름)):
    stock_data = stock_price_fuc.get_stockData_2_dataframe(i,'2019-01-01')
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (18, 9)
    plt.rcParams['font.size'] = 12

    fontprop = fm.FontProperties(fname='C:/NanumBarunGothic.ttf',size = 18)
    fig, ax1 = plt.subplots()
    ax1.plot(stock_data.index,stock_data['Close'],color='blue')
    plt.title(옥수치2009_over_10_per.loc[옥수치2009_over_10_per['회사코드(clean)'] == i,'회사이름'].values[0] +'_'+ i + '_'+옥수치2009_over_10_per.loc[옥수치2009_over_10_per['회사코드(clean)'] == i,'업종'].values[0], fontproperties = fontprop)
    plt.grid()
    plt.show()
    