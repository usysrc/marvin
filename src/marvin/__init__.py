import requests
import time
import os

# Define your variables
homeserver_url = os.environ["MATRIX_HOMESERVER"]
access_token = os.environ["MATRIX_ACCESSTOKEN"]
room_id = os.environ["MATRIX_ROOMID"]
message = os.environ["MATRIX_MESSAGE"]

# Function to get a monotonically increasing transaction ID
def get_txn_id():
    return str(int(time.time() * 1000))

def send_message(msg):
    # Generate the transaction ID
    txn_id = get_txn_id()

    # Define the endpoint
    endpoint = f"{homeserver_url}/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txn_id}"
    print(endpoint)
    # Define the headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Define the message content
    data = {
        "msgtype": "m.text",
        "body": msg
    }

    # Send the request
    response = requests.put(endpoint, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}")
        print(response.json())

send_message(message)