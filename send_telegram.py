#!/usr/bin/env python3

# узнать chat_id нужно в username_to_id_bot

import requests

def send_telegram(text: str):    
    # Redmi8T
    token = "2093200328:AAHjZhfN1ghTz_8yZI6BLCXNHOt2HDuy-cY"
    chat_id = "1487509241"

    # S20+
    # token = "1939255090:AAHXgKAxy0KQY-zHzonRRwvGo_Yh8PgAj5k"
    # chat_id = "389561175"

    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": chat_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram('test_message')
