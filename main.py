from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "4logitech"  # must match what you set in Meta dashboard

@app.route('/')
def index():
    return "Webhook is running!", 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    elif request.method == 'POST':
        print("Received webhook data:", request.json)
        return "Event received", 200
