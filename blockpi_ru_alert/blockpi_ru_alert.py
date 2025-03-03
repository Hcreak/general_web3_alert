import requests
import os

blockpi_apikey = os.getenv("blockpi_apikey")
balance_alert = int(os.getenv("balance_alert"))
tg_bot_token = os.getenv("tg_bot_token")
tg_bot_chatid = os.getenv("tg_bot_chatid")
tg_bot_message_thread_id = os.getenv("tg_bot_message_thread_id")

blockpi_ruBalance_body = {
    "jsonrpc": "2.0",
    "method": "blockpi_ruBalance",
    "params": [
        {
            "apiKey": blockpi_apikey
        }
    ],
    "id": 1
}

r = requests.post("https://api.blockpi.io/openapi/v1/rpc", json=blockpi_ruBalance_body)
ru_balance = r.json()["result"]["balance"] 
print(ru_balance)

if ru_balance < balance_alert:
    alert_text = "BlockPi RU Packet has Low Balance! (*{}*)".format(ru_balance)
    print(alert_text)
    if tg_bot_message_thread_id:
        req_data = {'chat_id':tg_bot_chatid, 'message_thread_id':tg_bot_message_thread_id, 'text':alert_text, 'parse_mode':'Markdown'}
    else:
        req_data = {'chat_id':tg_bot_chatid, 'text':alert_text, 'parse_mode':'Markdown'}
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_bot_token), data=req_data)