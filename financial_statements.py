from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_html_finance_data(stock_code:str,dir_name:str):
    html = urlopen("https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?gicode=A"+stock_code)  
    bsObject = BeautifulSoup(html, "html.parser")
    f = open('./html/'+dir_name+'/'+stock_code+'.html', 'w',encoding='utf-8')
    f.write(str(bsObject))
    f.close()


