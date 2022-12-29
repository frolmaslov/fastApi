import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    id = 0
    while True:
        id += 1
        data = await websocket.receive_text()
        
        await websocket.send_json({
                "Message": f"{data}",
                "ID:": id
            })


if __name__ == "__main__":
    uvicorn.run("main:app")