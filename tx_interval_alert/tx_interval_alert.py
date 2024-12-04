import requests
import os
from datetime import timedelta,datetime

target_address = os.getenv("target_address")
interval_minute = timedelta(minutes=int(os.getenv("interval_minute")))
tg_bot_token = os.getenv("tg_bot_token")
tg_bot_chatid = os.getenv("tg_bot_chatid")
etherscan_url = os.getenv("etherscan_url") if os.getenv("etherscan_url") else "https://api.etherscan.io/api"
etherscan_api_key = os.getenv("etherscan_api_key")

r = requests.get("{}?module=account&action=txlist&address={}&page=1&offset=1&sort=desc&apikey={}".format(etherscan_url,target_address,etherscan_api_key))
last_tx = r.json()["result"][0] 
print(last_tx)

last_tx_time = datetime.fromtimestamp(int(last_tx["timeStamp"]))
if datetime.now() - last_tx_time > interval_minute:
    alert_text = "*{}* Interval Timeout for sending transactions!".format(target_address)
    print(alert_text)
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_bot_token), data={'chat_id':tg_bot_chatid, 'text':alert_text, 'parse_mode':'Markdown'})
