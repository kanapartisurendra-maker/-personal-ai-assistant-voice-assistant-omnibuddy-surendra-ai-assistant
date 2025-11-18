from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import time

app = FastAPI(title="Personal AI Assistant - Backend")

class ChatRequest(BaseModel):
    text: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    text: str
    audio: Optional[str] = None

def simulate_response(prompt: str) -> str:
    prompt = prompt.strip().lower()
    if not prompt:
        return "I didn't catch that — can you say it again?"
    if "hello" in prompt or "hi" in prompt:
        return "Hello! How can I help you today?"
    if "time" in prompt:
        return f"It is currently {time.strftime('%H:%M:%S')}."
    return f"I received: {prompt[:200]}"

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        reply = simulate_response(req.text)
        return ChatResponse(text=reply, audio=None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}
