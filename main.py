from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

VERIFY_TOKEN = "your_custom_token_here"  # <-- Replace this with your own secret

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return JSONResponse(content=params.get("hub.challenge"))
    return JSONResponse(content="Invalid verification", status_code=403)

@app.post("/webhook")
async def receive_event(request: Request):
    data = await request.json()
    print("Received Webhook Event:", data)
    return JSONResponse(content={"status": "received"}, status_code=200)
