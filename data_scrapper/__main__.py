from bs4 import BeautifulSoup
import requests
import pandas as pd

from .db_config import Session
from .db_models import OhlcvdataModel
from .db_config import engine

#coin_symbols = ["neo", "eos", "stellar", "tron", "cardano", "monero", "nem", "siacoin", "verge", "digibyte", "stratis", "reddcoin", "dash", "zcash", "tezos", "vechain"]
coin_symbols = ["bitcoin", "ethereum", "ethereum-classic", "iota", "ripple", "litecoin"]

def tes_insert():
    print('Hello World')

    session = Session()
    new_rec = OhlcvdataModel(
        name='bitfinex'
    )
    session.add(new_rec)
    session.commit()


def add_record(line):
    session = Session()
    new_rec = OhlcvdataModel(
        name='bitfinex'
    )
    session.add(new_rec)
    session.commit()

def main():
    for coin in coin_symbols:
        print(f"coin are valoarea {coin}")
        url = f"https://coinmarketcap.com/currencies/{coin}/historical-data/?start=20130428&end=20190111"
        content = requests.get(url).content
        soup = BeautifulSoup(content,'html.parser')
        table = soup.find('table', {'class': 'table'})
     
        data = [[td.text.strip() for td in tr.findChildren('td')]
                for tr in table.findChildren('tr')]
        df = pd.DataFrame(data)
        df.drop(df.index[0], inplace=True) # first row is empty
        df[0] =  pd.to_datetime(df[0]) # date
        for i in range(1,7):
            df[i] = pd.to_numeric(df[i].str.replace(",","").str.replace("-","")) # some vol is missing and has -
        df.columns = ['Date','Open','High','Low','Close','Volume','Market Cap']
        # import pdb;pdb.set_trace()
        df.set_index('Date',inplace=True)
        df.sort_index(inplace=True)
        df.insert(loc=0, column='name', value=coin)
        excel_name = f'/home/husky/coincapmarket/{coin}.xls'
        export_excel = df.to_excel (excel_name, index = True, header=True)
        df.to_sql('ohlcvdata2', engine, if_exists='append')

if __name__ == '__main__':
    main()

