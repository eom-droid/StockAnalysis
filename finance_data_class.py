
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


class Financial_Statements:
    def clean_index(self,index_of_thing):
        result = []
        for i in index_of_thing:
            a = i.get_text()
            if '펼치기' not in a:
                result.append(a.replace('\n','').lstrip().replace('\xa0','_'))
            else:
                result.append(a.replace('\n','')[:-14].lstrip())
        return result
    def clean_columns(self,columns_of_thing):
        result = []
        for i in columns_of_thing:
            result.append(i.get_text())
        return result
    def clean_values(self,values_of_thing):
        result = []
        for i in values_of_thing:
            try:
                result.append(float(i.get_text().replace(',','')))
            except:
                result.append(0)
        return result

    def __init__(self,bsObject,stock_codes):
        self.stock_code = stock_codes

        연간_포괄손익계산서_columns = self.clean_columns(bsObject.select('#divSonikY > table > thead > tr > th')[1:])
        연간_포괄손익계산서_index = self.clean_index(bsObject.select('#divSonikY > table > tbody > tr > th'))# 인덱스 완료
        연간_포괄손익계산서_values= np.reshape(self.clean_values(bsObject.select('#divSonikY > table > tbody > tr >td')),(len(연간_포괄손익계산서_index),len(연간_포괄손익계산서_columns)))
        self.연간_포괄손익계산서_df = pd.DataFrame(index = 연간_포괄손익계산서_index, columns = 연간_포괄손익계산서_columns,data = 연간_포괄손익계산서_values)

        분기_포괄손익계산서_columns = self.clean_columns(bsObject.select('#divSonikQ > table > thead > tr > th')[1:])
        분기_포괄손익계산서_index = self.clean_index(bsObject.select('#divSonikQ > table > tbody > tr > th'))# 인덱스 완료
        분기_포괄손익계산서_values= np.reshape(self.clean_values(bsObject.select('#divSonikQ > table > tbody > tr >td')),(len(분기_포괄손익계산서_index),len(분기_포괄손익계산서_columns)))
        self.분기_포괄손익계산서_df = pd.DataFrame(index = 분기_포괄손익계산서_index, columns = 분기_포괄손익계산서_columns,data = 분기_포괄손익계산서_values)



        연간_재무상태표_columns = self.clean_columns(bsObject.select('#divDaechaY > table > thead > tr > th')[1:])
        연간_재무상태표_index = self.clean_index(bsObject.select('#divDaechaY > table > tbody > tr > th'))# 인덱스 완료
        연간_재무상태표_values= np.reshape(self.clean_values(bsObject.select('#divDaechaY > table > tbody > tr >td')),(len(연간_재무상태표_index),len(연간_재무상태표_columns)))
        self.연간_재무상태표_df = pd.DataFrame(index = 연간_재무상태표_index, columns = 연간_재무상태표_columns,data = 연간_재무상태표_values)

        분기_재무상태표_columns = self.clean_columns(bsObject.select('#divDaechaQ > table > thead > tr > th')[1:])
        분기_재무상태표_index = self.clean_index(bsObject.select('#divDaechaQ > table > tbody > tr > th'))# 인덱스 완료
        분기_재무상태표_values= np.reshape(self.clean_values(bsObject.select('#divDaechaQ > table > tbody > tr >td')),(len(분기_재무상태표_index),len(분기_재무상태표_columns)))
        self.분기_재무상태표_df = pd.DataFrame(index = 분기_재무상태표_index, columns = 분기_재무상태표_columns,data = 분기_재무상태표_values)


        '''
        연간_현금흐름표_columns = self.clean_columns(bsObject.select('#divCashY > table > thead > tr > th')[1:])
        연간_현금흐름표_index = self.clean_index(bsObject.select('#divCashY > table > tbody > tr > th'))# 인덱스 완료
        연간_현금흐름표_values= np.reshape(self.clean_values(bsObject.select('#divCashY > table > tbody > tr >td')),(len(연간_현금흐름표_index),len(연간_현금흐름표_columns)))
        self.연간_현금흐름표_df = pd.DataFrame(index = 연간_현금흐름표_index, columns = 연간_현금흐름표_columns,data = 연간_현금흐름표_values)

        분기_현금흐름표_columns = self.clean_columns(bsObject.select('#divCashQ > table > thead > tr > th')[1:])
        분기_현금흐름표_index = self.clean_index(bsObject.select('#divCashQ > table > tbody > tr > th'))# 인덱스 완료
        분기_현금흐름표_values= np.reshape(self.clean_values(bsObject.select('#divCashQ > table > tbody > tr >td')),(len(분기_현금흐름표_index),len(분기_현금흐름표_columns)))
        self.분기_현금흐름표_df = pd.DataFrame(index = 분기_현금흐름표_index, columns = 분기_현금흐름표_columns,data = 분기_현금흐름표_values)
        '''

    def 옥_수식_연간(self):
        date_columns = self.연간_재무상태표_df.columns
        유동금융자산 = 0
        현금및현금성자산 = 0
        투자부동산 = 0
        장기금융자산 = 0
        관계기업등지분관련투자자산 = 0
        기타금융업자산 = 0
        자산_비영업포함 = 0

        영업이익 = 0
        #비영업이익
        try:
            유동금융자산 = self.연간_재무상태표_df.loc['유동금융자산']
        except:
            유동금융자산 = 0

        try:
            현금및현금성자산 = self.연간_재무상태표_df.loc['현금및현금성자산']
        except:
            현금및현금성자산 = 0

        try:
            투자부동산 = self.연간_재무상태표_df.loc['투자부동산']
        except:
            투자부동산 = 0

        try:
            장기금융자산 = self.연간_재무상태표_df.loc['장기금융자산']
        except:
            장기금융자산 = 0

        try:
            관계기업등지분관련투자자산 = self.연간_재무상태표_df.loc['관계기업등지분관련투자자산']
        except:
            관계기업등지분관련투자자산 = 0

        try:
            기타금융업자산 = self.연간_재무상태표_df.loc['기타금융업자산']
        except:
            기타금융업자산 = 0

        try:
            자산_비영업포함 = self.연간_재무상태표_df.loc['자산']
        except:
            자산_비영업포함 = 0
        
        try:
            영업이익 = self.연간_포괄손익계산서_df.loc['영업이익'][date_columns]
        except:
            return [np.nan,np.nan,np.nan,np.nan]
        
        영업이익 = 영업이익.astype(int)
        #영업이익 = self.연간_포괄손익계산서_df.loc['영업이익'][date_columns].astype(int)
        try:
            영업자산 = (자산_비영업포함 -유동금융자산-현금및현금성자산-투자부동산-장기금융자산-관계기업등지분관련투자자산 - 기타금융업자산).astype(int)
        except:
            return [np.nan,np.nan,np.nan,np.nan]

        ock_수식 = 영업이익/영업자산 * 100
        return ock_수식


        '''
        print(self.stock_code)

        #비영업자산
        date_columns = self.연간_재무상태표_df.columns
        유동금융자산 = self.연간_재무상태표_df.loc['유동금융자산']
        현금및현금성자산 = self.연간_재무상태표_df.loc['현금및현금성자산']
        투자부동산 = self.연간_재무상태표_df.loc['투자부동산']
        장기금융자산 = self.연간_재무상태표_df.loc['장기금융자산']
        관계기업등지분관련투자자산 = self.연간_재무상태표_df.loc['관계기업등지분관련투자자산']
        기타금융업자산 = self.연간_재무상태표_df.loc['기타금융업자산']
        자산_비영업포함 = self.연간_재무상태표_df.loc['자산']


        영업자산 = 자산_비영업포함 -유동금융자산-현금및현금성자산-투자부동산-장기금융자산-관계기업등지분관련투자자산 - 기타금융업자산
        영업이익 = self.연간_포괄손익계산서_df.loc['영업이익'][date_columns]
        ock_수식 = 영업이익.astype(int)/영업자산.astype(int) * 100
        return ock_수식
'''

    def 옥_수식_분기(self):
        date_columns = self.분기_재무상태표_df.columns
        print(self.stock_code)
        유동금융자산 = 0
        현금및현금성자산 = 0
        투자부동산 = 0
        장기금융자산 = 0
        관계기업등지분관련투자자산 = 0
        기타금융업자산 = 0
        자산_비영업포함 = 0

        영업이익 = 0
        #비영업이익
        try:
            유동금융자산 = self.분기_재무상태표_df.loc['유동금융자산']
        except:
            유동금융자산 = 0

        try:
            현금및현금성자산 = self.분기_재무상태표_df.loc['현금및현금성자산']
        except:
            현금및현금성자산 = 0

        try:
            투자부동산 = self.분기_재무상태표_df.loc['투자부동산']
        except:
            투자부동산 = 0

        try:
            장기금융자산 = self.분기_재무상태표_df.loc['장기금융자산']
        except:
            장기금융자산 = 0

        try:
            관계기업등지분관련투자자산 = self.분기_재무상태표_df.loc['관계기업등지분관련투자자산']
        except:
            관계기업등지분관련투자자산 = 0

        try:
            기타금융업자산 = self.분기_재무상태표_df.loc['기타금융업자산']
        except:
            기타금융업자산 = 0

        try:
            자산_비영업포함 = self.분기_재무상태표_df.loc['자산']
        except:
            자산_비영업포함 = 0
        '''
        try:
            영업이익 = self.분기_포괄손익계산서_df.loc['영업이익'][date_columns].astype(int)
        except:
            print('영업이익 이상함')
            영업이익 = 0
        '''



        try:
            영업이익 = self.분기_포괄손익계산서_df.loc['영업이익'][date_columns]
        except:
            return [np.nan,np.nan,np.nan,np.nan] 

        영업이익 = 영업이익.astype(int)
        try:
            영업자산 = (자산_비영업포함 -유동금융자산-현금및현금성자산-투자부동산-장기금융자산-관계기업등지분관련투자자산 - 기타금융업자산).astype(int)
        except:
            print('영업자산 뭔가 이상함')
            return [np.nan,np.nan,np.nan,np.nan]
        
        ock_수식 = 영업이익/영업자산 * 100
        return ock_수식

        


    def __del__(self):
        print(self.stock_code+'가 종료')
    




