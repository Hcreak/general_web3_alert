from web3 import Web3
import requests
import os
import time

w3 = Web3(Web3.HTTPProvider(os.getenv("Provider")))
interval_second = int(os.getenv("interval_second"))
tg_bot_token = os.getenv("tg_bot_token")
tg_bot_chatid = os.getenv("tg_bot_chatid")
tg_bot_message_thread_id = os.getenv("tg_bot_message_thread_id")

last_block_time = w3.eth.get_block('latest')["timestamp"]
print(last_block_time)
diff = int(time.time()) - last_block_time
if  diff > interval_second:
    alert_text = "Interval Timeout for Create Blocks! (*{}s*)".format(diff)
    print(alert_text)
    if tg_bot_message_thread_id:
        req_data = {'chat_id':tg_bot_chatid, 'message_thread_id':tg_bot_message_thread_id, 'text':alert_text, 'parse_mode':'Markdown'}
    else:
        req_data = {'chat_id':tg_bot_chatid, 'text':alert_text, 'parse_mode':'Markdown'}
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_bot_token), data=req_data)
