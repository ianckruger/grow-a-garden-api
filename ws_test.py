import asyncio
import json
import websockets

async def listen():
    url = "wss://gagapi.liriosha/dev/ws"
    print("Connecting to Grow a Garden Web Socket")

    try:
        async with websockets.connect(url) as ws:
            print("connected")
            async for message in ws:
                data = json.loads(message)
                print("Data Captured")
                print(json.dumps(data,indent=2))
    
    except Exception as e:
        print(f"Connection error: {e}")

asyncio.run(listen())