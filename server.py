#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    if ("ls" in name):
        greeting = f"ls in name: {name}!"
    elif ("cd" in name):
        greeting = f"cd in name: {name}!"
    elif ("mv" in name):
        greeting = f"mv in name: {name}!"
    else:
        greeting = f": {name}!"
    

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

#Converted to finding Linux commands in names by Deniz Kiratli
#Added mv command for names by H. Berfin Polat
