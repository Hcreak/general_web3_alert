from web3 import Web3
import requests
import os
import time

w3 = Web3(Web3.HTTPProvider(os.getenv("Provider")))
interval_second = int(os.getenv("interval_second"))
tg_bot_token = os.getenv("tg_bot_token")
tg_bot_chatid = os.getenv("tg_bot_chatid")

last_block_time = w3.eth.get_block('latest')["timestamp"]
print(last_block_time)
diff = int(time.time()) - last_block_time
if  diff > interval_second:
    alert_text = "Interval Timeout for Create Blocks! (*{}s*)".format(diff)
    print(alert_text)
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_bot_token), data={'chat_id':tg_bot_chatid, 'text':alert_text, 'parse_mode':'Markdown'})
