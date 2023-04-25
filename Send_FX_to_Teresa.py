# load package
from google_currency import convert
import pandas as pd
import requests

# get data
usd_to_jpy = convert('usd', 'jpy', 1)[40:45]
usd_to_ntd = convert('usd', 'twd', 1)[40:45]
ntd_to_jpy = convert('twd', 'jpy', 1)[40:44]
Cathay_usd = str(pd.read_html("https://www.cathaybk.com.tw/cathaybk/personal/deposit-exchange/rate/currency-billboard/?p=furtheradvance&p=furtheradvance&p=treeloan&p=mortgage&p=employeeloan&dev=mobile&CUB_SRC=GOOGLE&CUB_CHL1=URL&CUB_CHL2=01&MA_TK=DB197&CUB_DT=20190701&utm_source=Cathay_officialwebsite&utm_medium=loan_homemenu&utm_campaign=19Q3_alwayson&utm_content=1&utm_term=1&DEV=MOBILE")[0]['銀行賣出  Bank sell'][0])

# send message
def lineNotifyMessage(token, msg):
    r = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {token}"},
        data={"message": msg}
    )
    return r.status_code

# wrap_up
message = str('\n' + '國泰美金兌台幣: ' + Cathay_usd + '\n' + '\n' + 'USD to JPY: ' + usd_to_jpy + '\n' + 'USD to NTD: ' + usd_to_ntd + '\n' + 'NTD to JPY: '+ ntd_to_jpy + '\n' + 'source: Google currency')
token = 'nw5bget1lcPWVdhJrjvhCnigDsb6XWyyf4OVailNqzf'
lineNotifyMessage(token, message)
