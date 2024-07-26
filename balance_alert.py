from web3 import Web3
import requests
import os

w3 = Web3(Web3.HTTPProvider(os.getenv("Provider")))
target_address = os.getenv("target_address")
balance_alert = w3.to_wei(os.getenv("balance_alert"),'ether')
slack_bot_webhook = os.getenv("slack_bot_webhook")

cur_balance = w3.eth.get_balance(target_address)
print(cur_balance)
if cur_balance < balance_alert:
    alert_text = "*{}* has Low Balance!(*{} ether*)".format(target_address, w3.from_wei(cur_balance, "ether"))
    print(alert_text)
    requests.post(slack_bot_webhook, json={"text": alert_text})
