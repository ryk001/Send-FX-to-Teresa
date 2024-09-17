# load package
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os


''' old method 
# get data
# from google_currency import convert
# import json
# usd_to_jpy = json.loads(convert('usd', 'jpy', 1))['amount']
# usd_to_ntd = json.loads(convert('usd', 'twd', 1))['amount']
# ntd_to_jpy = json.loads(convert('twd', 'jpy', 1))['amount']
'''

# google currency
def get_google_currency(source_currency, target_currency):
    url = f"https://www.google.com/search?q={source_currency}+to+{target_currency}"
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser').find("div", class_="BNeawe iBp4i AP7Wnd").get_text().split(' ')[0]

usd_to_jpy = get_exchange_rate('USD', 'JPY')
usd_to_ntd = get_exchange_rate('USD', 'TWD')
ntd_to_jpy = get_exchange_rate('TWD', 'JPY')

# cathay
r = requests.get('https://www.cathaybk.com.tw/cathaybk/personal/product/deposit/currency-billboard')
cathay_usd = float(BeautifulSoup(r.text, "lxml").find_all('tr')[1].find_all('td')[2].find('div').text)

# message
message =(
    f'\n國泰美金兌台幣: {cathay_usd:.2f}\n\n'
    f'USD to JPY: {usd_to_jpy}\n'
    f'USD to NTD: {usd_to_ntd}\n'
    f'NTD to JPY: {ntd_to_jpy}\n'
    'source: Google currency'
)

# send message
def lineNotifyMessage(token, msg):
    r = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {token}"},
        data={"message": msg}
    )
    return r.status_code

token = os.environ['LINE_NOTIFY_TOKEN']
lineNotifyMessage(token, message)
