from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get the data sent with the webhook
    # Process the data or perform any desired actions
    # ...
    print(data)
    return 'Webhook received successfully'


@app.route('/trigger_message', methods=['POST'])
def trigger_curl_request():
    url = 'https://graph.facebook.com/v16.0/114080598373447/messages'

    headers = {
        'Authorization': 'Bearer EAANNZB3mZC2mQBALdvHsFqZCQNjg4My6Jw8T8sOlp6pzSxH8YF9jz1Gbj3ZBsn95AdBIBGhMEs0GSBlFp1y0uJXZAt5Phkm8MZCw87jOxZC0wh68ZBZBQhxtk1xLkwGjRkUVKfRkgSQPtHNAnXj2NXSK4k1Q2Mw2ORu2ZAWWN1YTD53MaibWG0JJekFNHiPj2dmZBJedqrgdtkZALwZDZD',
        'Content-Type': 'application/json'
    }

    # Get the values from the request payload
    name = request.json.get('name')
    to = request.json.get('to')

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": name,
            "language": {
                "code": "en_US"
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.text, response.status_code

if __name__ == '__main__':
    app.run()
