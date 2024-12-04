from web3 import Web3
import requests
import os

w3 = Web3(Web3.HTTPProvider(os.getenv("Provider")))
target_address = os.getenv("target_address")
balance_alert = w3.to_wei(os.getenv("balance_alert"),'ether')
tg_bot_token = os.getenv("tg_bot_token")
tg_bot_chatid = os.getenv("tg_bot_chatid")

cur_balance = w3.eth.get_balance(target_address)
print(cur_balance)
if cur_balance < balance_alert:
    alert_text = "*{}* has Low Balance! (*{} ether*)".format(target_address, w3.from_wei(cur_balance, "ether"))
    print(alert_text)
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_bot_token), data={'chat_id':tg_bot_chatid, 'text':alert_text, 'parse_mode':'Markdown'})
