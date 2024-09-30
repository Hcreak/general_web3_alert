import requests
import os

blockpi_apikey = os.getenv("blockpi_apikey")
balance_alert = int(os.getenv("balance_alert"))
slack_bot_webhook = os.getenv("slack_bot_webhook")

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
    requests.post(slack_bot_webhook, json={"text": alert_text})