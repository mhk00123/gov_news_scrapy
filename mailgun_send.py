import requests

def send_email(to, subject, content):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxae3a29c04bea4245bf8cef43b475175a.mailgun.org/messages",
        auth=("api", "key-aad878173c5f50716ea8e0941c708b66"),
        data={"from": "Thomas Mak <mak@makzan.net>",
              "to": to,
              "subject": subject,
              "text": content})

      
