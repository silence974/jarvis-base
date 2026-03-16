from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.utils import from_env, secret_from_env
from langchain_openai import ChatOpenAI

load_dotenv()

app = FastAPI(debug=True)


class Master:
    def __init__(self) -> None:
        self.chat_model = ChatOpenAI(
            model="deepseek-chat",
            temperature=0,
            streaming=True,
            api_key=secret_from_env("DEEPSEEK_API_KEY")(),
            base_url=from_env("DEEPSEEK_API_BASE_URL")(),
        )
        self.MEMORY_KEY = "chat_history"
        self.SYSTEMPL = ""
        self.prompt = SystemMessage(content="你是一个助手，协助用户完成各种任务。")
        self.memory = ""
        self.agent_executor = create_agent(
            self.chat_model, tools=[], system_prompt=self.prompt, debug=True
        )

    def run(self, query: str):
        message = HumanMessage(content=query)
        result = self.agent_executor.invoke(message)
        return result


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(query: str):
    master = Master()
    response = master.run(query)
    return {"response": response}


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
