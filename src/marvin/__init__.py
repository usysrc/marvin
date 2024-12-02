import asyncio
import os
from nio import AsyncClient

# Define your variables
homeserver_url = os.environ["MATRIX_HOMESERVER"]
access_token = os.environ["MATRIX_ACCESSTOKEN"]
room_id = os.environ["MATRIX_ROOMID"]
message = os.environ["MATRIX_MESSAGE"]


async def send_poll():
    client = AsyncClient(homeserver_url, device_id="PollBot")
    client.access_token = access_token

    try:
        await send_message(client, "montag")
        await send_message(client, "dienstag")
        await send_message(client, "mittwoch")
        await send_message(client, "donnerstag")
        await send_message(client, "freitag")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.close()

async def send_message(client, msg):
    await client.room_send(
        room_id,
        "m.room.message",
        {
            "msgtype": "m.text",
            "body": msg,
        },
        ignore_unverified_devices=True
    )

def run_poll():
    asyncio.get_event_loop().run_until_complete(send_poll())

def main() -> None:
    run_poll()