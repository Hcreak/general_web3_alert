import requests
import os
from datetime import timedelta,datetime

target_address = os.getenv("target_address")
interval_minute = timedelta(minutes=int(os.getenv("interval_minute")))
slack_bot_webhook = os.getenv("slack_bot_webhook")
etherscan_api_key = os.getenv("etherscan_api_key")

r = requests.get("https://api.etherscan.io/api?module=account&action=txlist&address={}&page=1&offset=1&sort=desc&apikey={}".format(target_address,etherscan_api_key))
last_tx = r.json()["result"][0] 
print(last_tx)

last_tx_time = datetime.fromtimestamp(int(last_tx["timeStamp"]))
if datetime.now() - last_tx_time > interval_minute:
    alert_text = "*{}* Interval Timeout for sending transactions!".format(target_address)
    print(alert_text)
    requests.post(slack_bot_webhook, json={"text": alert_text})
