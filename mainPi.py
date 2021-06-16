# WS server example
import os
import asyncio
import websockets
import base64

key = "You know my diamonds be shining pull up 488 just like what?"


async def hello(websocket, path):
    message = await websocket.recv()
    print(f"Received '{message}'")
    with open('example.jpg', "rb") as img_file:
        imageString = base64.b64encode(img_file.read())
    print(f"Base64 length: {len(imageString)}")
    await websocket.send(imageString)


start_server = websockets.serve(hello, "localhost", 488)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

photo_paths = getPhotos(int(number_photos), int(delay))
