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
    
    await client.room_send(
        room_id,
        "m.room.message",
        {
            "msgtype": "m.text",
            "body": "Greetings humans!"
        },
        ignore_unverified_devices=True
    )

    poll_content = {
        "org.matrix.msc3381.poll.start": {
            "question": {
                "org.matrix.msc1767.text": "Weekly Gaming Session Poll",
                "body": "Weekly Gaming Session Poll!",
                "msgtype": "m.text"
            },
            "kind": "org.matrix.msc3381.poll.disclosed",
            "max_selections": 1,
            "answers": [
                {"id": "montag", "org.matrix.msc1767.text": "Montag"},
                {"id": "dienstag", "org.matrix.msc1767.text": "Dienstag"},
                {"id": "mittwoch", "org.matrix.msc1767.text": "Mittwoch"},
                {"id": "donnerstag", "org.matrix.msc1767.text": "Donnerstag"},
                {"id": "freitag", "org.matrix.msc1767.text": "Freitag"},]
        }
    }

    await client.room_send(room_id, "org.matrix.msc3381.poll.start", poll_content)
    await client.close()

def run_poll():
    asyncio.get_event_loop().run_until_complete(send_poll())

def main() -> None:
    run_poll()