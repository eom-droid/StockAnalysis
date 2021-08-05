import pandas as pd


def save_csv():
    code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
    db = pd.DataFrame(code_df)
    db.to_csv('./data/stock_list.csv', mode = 'w', encoding = 'euc-kr')


def get_df():
    code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
    db = pd.DataFrame(code_df)
    return db

def get_stock_name(stock_num,stock_listed_df = None):
    if stock_listed_df is None:
        stock_listed_df = get_df()
        return stock_listed_df.loc[stock_listed_df['종목코드'] == int(stock_num),'회사명'].values[0]
    else:
        return stock_listed_df.loc[stock_listed_df['종목코드'] == int(stock_num),'회사명'].values[0]