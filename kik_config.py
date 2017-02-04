from kik import KikApi
import requests
import json
import os

API_KEY = os.getenv('API_KEY')

result = requests.post(
    'https://api.kik.com/v1/config',
    auth=('takeyouanywhere', API_KEY),
    headers={
        'Content-Type': 'application/json'
    },
    data=json.dumps({
        "webhook": "http://viewtheearth.herokuapp.com/incoming",
        "features": {
            "manuallySendReadReceipts": False,
            "receiveReadReceipts": False,
            "receiveDeliveryReceipts": False,
            "receiveIsTyping": False
        }
    })
)
kik = KikApi('takeyouanywhere', API_KEY)
