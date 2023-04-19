
from flask import Flask, request
import requests

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

PAGE_ACCESS_TOKEN = 'df29b289c1a6a101250d9cad116cc89e'
API = "1250454965900452"

#login lolololol
@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "df29b289c1a6a101250d9cad116cc89e":
            return "Invalid token.", 403
        return request.args['hub.challenge'], 200               
    return "I'm online!", 200                  

@app.route("/", methods=['POST'])
def fbwebhook():
    data = request.get_json()
    print(data)
    try:
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        if message['text'] == "status":
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "online!"
                }
            }
            response = requests.post(API, json=request_body).json()
            return response
        elif message['text'] == "quick":
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "messaging_type": "RESPONSE",
                "message": {
                    "text": "Choose a color:",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "Red",
                            "payload": "<like,smth here?>",
                            "image_url": "http://example.com/img/red.png"
                        }, {
                            "content_type": "text",
                            "title": "Green",
                            "payload": "<I ran out of context lmfao>",
                            "image_url": "http://example.com/img/green.png"
                        }
                    ]
                }
            }
            response = requests.post(API, json=request_body).json()
            return response
    except:
        print("SIGFAULT")