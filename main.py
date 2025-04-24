from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

VERIFY_TOKEN = "4logitech"  # Replace this with your actual verify token

@app.get("/")
async def root():
    return {"message": "Auto DM FastAPI is running!"}

@app.get("/webhook", response_class=PlainTextResponse)
async def verify_webhook(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge
    else:
        return PlainTextResponse("Verification failed", status_code=403)

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    # Process the webhook data (for now, just return it)
    return {"received_data": data}
