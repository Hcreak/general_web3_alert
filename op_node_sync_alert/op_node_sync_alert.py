from web3 import Web3
import requests
import os

l2_op_api = os.getenv("L2_OP_API")
diff_alert = int(os.getenv("diff_alert"))
slack_bot_webhook = os.getenv("slack_bot_webhook")

syncStatus_body = {
    "jsonrpc": "2.0",
    "id": "anything",
    "method":"optimism_syncStatus",
    "params": []
}
r = requests.post(l2_op_api, json=syncStatus_body)
sync_status = r.json()['result']
current_l1 = sync_status['current_l1']['number']
head_l1 = sync_status['head_l1']['number']
diff = head_l1 - current_l1

print("op sync status:")
print(f"\tcurrent_l1 height: {current_l1}")
print(f"\tcurrent_l1_finalized height: {sync_status['current_l1_finalized']['number']}")
print(f"\thead_l1 height: {head_l1}")
print(f"\tsafe_l1 height: {sync_status['safe_l1']['number']}")
print(f"\tfinalized_l1 height: {sync_status['finalized_l1']['number']}")
print("")
print(f"\thead_l1 - current_l1: {diff}")

if diff > diff_alert:
    alert_text = "head_l1 - current_l1 too high!"
    print(alert_text)
    requests.post(slack_bot_webhook, json={"text": alert_text})
