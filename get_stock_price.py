import FinanceDataReader as fdr
from datetime import datetime

def full_name_of_date(input_date):
    if len(input_date) == 10:
        return input_date
    elif len(input_date) == 7:
        return input_date + '-01'
    elif len(input_date) == 4:
        return input_date + '-01-01'
    else:
        print("뭔가이상한데")


def print_stockData(stock_code,start_day,end_day = None):
    if end_day is None:
        df = fdr.DataReader(stock_code, start_day)
        print(df)
    else:
        df = fdr.DataReader(stock_code, start_day,end_day)
        print(df)



def get_stockData_2_csv(stock_code,start_day,end_day = None):
    if end_day is None:
        df = fdr.DataReader(stock_code, start_day)
        end_day = datetime.today().strftime("%Y-%m-%d")
        df.to_csv('data/'+ stock_code+'_'+full_name_of_date(start_day)+ '_' + full_name_of_date(end_day)+'.csv')
    else:
        df = fdr.DataReader(stock_code, start_day,end_day)
        df.to_csv('data/'+ stock_code+'_'+full_name_of_date(start_day)+ '_' + full_name_of_date(end_day)+'.csv')
        print('\n'+str(len(df))+'row saved_as_csv\n' )

def get_stockData_2_dataframe(stock_code,start_day,end_day = None):
    if end_day is None:
        df = fdr.DataReader(stock_code, start_day)
        return df

    else:
        df = fdr.DataReader(stock_code, start_day,end_day)
        return df


