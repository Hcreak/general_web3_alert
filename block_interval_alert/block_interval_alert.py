from web3 import Web3
import requests
import os
import time

w3 = Web3(Web3.HTTPProvider(os.getenv("Provider")))
interval_second = int(os.getenv("interval_second"))
slack_bot_webhook = os.getenv("slack_bot_webhook")

last_block_time = w3.eth.get_block('latest')["timestamp"]
print(last_block_time)
diff = int(time.time()) - last_block_time
if  diff > interval_second:
    alert_text = "Interval Timeout for Create Blocks! (*{}s*)".format(diff)
    print(alert_text)
    requests.post(slack_bot_webhook, json={"text": alert_text})
