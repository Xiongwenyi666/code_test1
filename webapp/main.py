### duplicate or run the following statement if the fastapi has not been installed before
# pip install fastapi[all]
from fastapi import FastAPI, WebSocket  
from starlette.websockets import WebSocketDisconnect 
from fastapi.responses import HTMLResponse
import os


app = FastAPI()


class ConnectionManager:
     
    def __init__(self):
        self.active_connections: set[WebSocket] = set()  
        # save the connected usernames
        self.clients: dict[WebSocket, str] = {}



    async def connect(self, websocket: WebSocket, username: str):  
        await websocket.accept()  
        self.active_connections.add(websocket)  
        self.clients[websocket] = username
        print(f"""Connected: {username}""")
        

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:  
            self.active_connections.remove(websocket)  

            if websocket in self.clients:  
                del self.clients[websocket]

    async def broadcast(self, message: str, websocket : WebSocket = None):
        for connection in self.active_connections:
            if connection is not websocket: 
                await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):

    await manager.connect(websocket, username)  # Pass the username to connect method
    # request the clients to send user name

    try:
        # send message
        async for message in websocket.iter_text():
            await manager.broadcast(f"{manager.clients[websocket]}: {message}", websocket)

    except WebSocketDisconnect:
        print(f"Disconnected: {username}")  
        manager.disconnect(websocket)

    except Exception as e:
        print(f"""Error: {e}""")
    
    finally:
        await websocket.close()
        manager.disconnect(websocket)

# get the HTML page
@app.get("/")  
async def read_root():
    current_dir = os.path.abspath(os.curdir).replace('\\',  '/')
    return HTMLResponse(content=open(current_dir + "/webapp/chat_test.html", "r", encoding="utf-8").read())
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host = 'localhost', port= 8000)