from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


df = pd.read_csv('./data/컨센서스_분기.txt',sep = '\t')
df.to_csv('./data/shit.csv')