from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat():
    return {"response": "This is a chat endpoint"}

@app.post("/add_urls")
def add_urls():
    return {"response": "This is an add_urls endpoint"}

@app.post("/add_pdfs")
def add_pdfs():
    return {"response": "This is an add_pdfs endpoint"}

@app.post("/add_texts")
def add_texts():
    return {"response": "This is an add_texts endpoint"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message: {data}")
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        print("WebSocket disconnected")
        await websocket.close()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)