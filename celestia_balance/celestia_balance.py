import requests
import os
import json

Provider = os.getenv("Provider")
target_address = os.getenv("target_address")
balance_alert = int(os.getenv("balance_alert"))
tg_bot_token = os.getenv("tg_bot_token")
tg_bot_chatid = os.getenv("tg_bot_chatid")

celestia_result = os.popen(f"/bin/celestia-appd query bank balances {target_address} --node {Provider} -o json").read()
cur_balance = int(json.loads(celestia_result)["balances"][0]["amount"])

print(cur_balance)
if cur_balance < balance_alert:
    alert_text = "*{}* has Low Balance! (*{}*)".format(target_address, cur_balance)
    print(alert_text)
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_bot_token), data={'chat_id':tg_bot_chatid, 'text':alert_text, 'parse_mode':'Markdown'})
