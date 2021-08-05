
import financial_statements as fs
import get_stock_listed as gsl
import time
stock_list_df = gsl.get_df()
import random
#stockcode = '005930'
#fs.get_html_finance_data(stockcode)

stock_list_df['종목코드(clean)'] = stock_list_df['종목코드'].apply(lambda x : str(x).zfill(6))
for i in stock_list_df['종목코드(clean)']:
    random_time = random.uniform(0.05, 0.15)
    time.sleep(random_time)
    try:
        fs.get_html_finance_data(i,'17년도부터_2020_4분기')
    except:
        print('이상현상 발생 ' + i)
        break
    