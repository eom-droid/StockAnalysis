

'''#분기
def sort_리츠(comp_name):
    if comp_name[-2:] == '리츠':
        return np.nan
    else:
        #print(comp_name)
        return comp_name
옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
분기_df = pd.read_csv('./분기_df.csv')
분기_df =분기_df.drop('Unnamed: 0',axis = 1)
분기_df['회사코드(clean)'] = 분기_df['회사코드'].apply(lambda x : str(x).zfill(6))
#print(분기_df.dropna(axis = 0))
분기_df = 분기_df.replace([np.inf, -np.inf,0], np.nan)
분기_df['회사이름'] = 분기_df['회사이름'].apply(sort_리츠)
분기_df = 분기_df.dropna(axis = 0)


index = 0
for stock_code in 분기_df['회사코드(clean)']:
    stock_price = stock_price_fuc.get_stockData_2_dataframe(stock_code,'2019-10-01','2020-09-30')
    stock_price = stock_price.resample('1M').mean()[['Close']]
    stock_price.index = stock_price.index.strftime('%Y-%m')
    print(stock_code)
    분기_2019_4분기_주가 = []
    분기_2020_1분기_주가 = []
    분기_2020_2분기_주가 = []
    분기_2020_3분기_주가 = []
    for i in stock_price.index:
        a = 0
        if i < '2020-01':
            분기_2019_4분기_주가.append(stock_price.loc[i].values[0])
        elif i < '2020-04':
            분기_2020_1분기_주가.append(stock_price.loc[i].values[0])
        elif i < '2020-07':
            분기_2020_2분기_주가.append(stock_price.loc[i].values[0])
        elif i < '2020-10':
            분기_2020_3분기_주가.append(stock_price.loc[i].values[0])
    #print(분기_2019_4분기_주가)
    if (len(분기_2019_4분기_주가) & len(분기_2020_1분기_주가) & len(분기_2020_2분기_주가) & len(분기_2020_3분기_주가)) == 0:
        continue
    else:
        분기_2019_4분기_주가 = sum(분기_2019_4분기_주가) /len(분기_2019_4분기_주가)
        분기_2020_1분기_주가 = sum(분기_2020_1분기_주가) /len(분기_2020_1분기_주가)
        분기_2020_2분기_주가 = sum(분기_2020_2분기_주가) /len(분기_2020_2분기_주가)
        분기_2020_3분기_주가 = sum(분기_2020_3분기_주가) /len(분기_2020_3분기_주가)

    분기_2019_4분기_옥수치 = 분기_df.loc[분기_df['회사코드(clean)'] == stock_code,'옥수치19/12'].values[0]
    분기_2020_1분기_옥수치 = 분기_df.loc[분기_df['회사코드(clean)'] == stock_code,'옥수치20/03'].values[0]
    분기_2020_2분기_옥수치 = 분기_df.loc[분기_df['회사코드(clean)'] == stock_code,'옥수치20/06'].values[0]
    분기_2020_3분기_옥수치 = 분기_df.loc[분기_df['회사코드(clean)'] == stock_code,'옥수치20/09'].values[0]

    raw_data = {'주가': [분기_2019_4분기_주가, 분기_2020_1분기_주가, 분기_2020_2분기_주가, 분기_2020_3분기_주가],
                '옥수치': [분기_2019_4분기_옥수치, 분기_2020_1분기_옥수치, 분기_2020_2분기_옥수치, 분기_2020_3분기_옥수치],
                'Date': ['2019-12','2020-03','2020-06','2020-09']}
    a = pd.DataFrame(raw_data)
    a = a.set_index('Date')
    corr = a.corr(method= 'pearson')


    분기별_corr = corr.iloc[0,1]
    옥수치_주가_corr_df.loc[index] = [stock_code,분기_df.loc[분기_df['회사코드(clean)'] == stock_code,'회사이름'].values[0],분기별_corr]
    index +=1
옥수치_주가_corr_df.to_csv('./옥수치_주가_corr_df.csv')

'''






'''
#연간
def sort_리츠(comp_name):
    if comp_name[-2:] == '리츠':
        return np.nan
    else:
        #print(comp_name)
        return comp_name
옥수치_주가_corr_df = pd.DataFrame(columns = ['회사코드','회사이름','corr'])
연간_df = pd.read_csv('./연간_df.csv')
연간_df =연간_df.drop('Unnamed: 0',axis = 1)
연간_df['회사코드(clean)'] = 연간_df['회사코드'].apply(lambda x : str(x).zfill(6))
#print(연간_df.dropna(axis = 0))
연간_df = 연간_df.replace([np.inf, -np.inf,0], np.nan)
연간_df['회사이름'] = 연간_df['회사이름'].apply(sort_리츠)
연간_df = 연간_df.dropna(axis = 0)


index = 0
for stock_code in 연간_df['회사코드(clean)']:
    stock_price = stock_price_fuc.get_stockData_2_dataframe(stock_code,'2017-01-01','2020-09-30')
    stock_price = stock_price.resample('1M').mean()[['Close']]
    stock_price.index = stock_price.index.strftime('%Y-%m')
    print(stock_code)
    연간_2017_4분기_주가 = []
    연간_2018_4분기_주가 = []
    연간_2019_4분기_주가 = []
    연간_2020_3분기_주가 = []
    for i in stock_price.index:
        a = 0
        if i < '2017-12':
            연간_2017_4분기_주가.append(stock_price.loc[i].values[0])
        elif i < '2018-12':
            연간_2018_4분기_주가.append(stock_price.loc[i].values[0])
        elif i < '2019-12':
            연간_2019_4분기_주가.append(stock_price.loc[i].values[0])
        elif i < '2020-09':
            연간_2020_3분기_주가.append(stock_price.loc[i].values[0])
    #print(분기_2019_4분기_주가)
    if (len(연간_2017_4분기_주가) & len(연간_2018_4분기_주가) & len(연간_2019_4분기_주가) & len(연간_2020_3분기_주가)) == 0:
        continue
    else:
        연간_2017_주가 = sum(연간_2017_4분기_주가) /len(연간_2017_4분기_주가)
        연간_2018_주가 = sum(연간_2018_4분기_주가) /len(연간_2018_4분기_주가)
        연간_2019_주가 = sum(연간_2019_4분기_주가) /len(연간_2019_4분기_주가)
        연간_2020_주가 = sum(연간_2020_3분기_주가) /len(연간_2020_3분기_주가)

    연간_2017_옥수치 = 연간_df.loc[연간_df['회사코드(clean)'] == stock_code,'옥수치17/12'].values[0]
    연간_2018_옥수치 = 연간_df.loc[연간_df['회사코드(clean)'] == stock_code,'옥수치18/12'].values[0]
    연간_2019_옥수치 = 연간_df.loc[연간_df['회사코드(clean)'] == stock_code,'옥수치19/12'].values[0]
    연간_2020_옥수치 = 연간_df.loc[연간_df['회사코드(clean)'] == stock_code,'옥수치20/09'].values[0]

    raw_data = {'주가': [연간_2017_주가, 연간_2018_주가, 연간_2019_주가, 연간_2020_주가],
                '옥수치': [연간_2017_옥수치, 연간_2018_옥수치, 연간_2019_옥수치, 연간_2020_옥수치],
                'Date': ['2017-12','2018-12','2019-12','2020-09']}
    a = pd.DataFrame(raw_data)
    a = a.set_index('Date')
    corr = a.corr(method= 'pearson')


    연간별_corr = corr.iloc[0,1]
    옥수치_주가_corr_df.loc[index] = [stock_code,연가_df.loc[연가_df['회사코드(clean)'] == stock_code,'회사이름'].values[0],연간별_corr]
    index +=1
옥수치_주가_corr_df.to_csv('./옥수치_주가_corr_df.csv')
'''
