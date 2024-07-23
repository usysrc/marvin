# Marvin - Matrix Room Scheduler Bot

Marvin is a simple bot designed to send messages to a Matrix room every on a given schedule to inquire about the availability of members for different days of the week.

## Setup

### Prerequisites

- rye: https://rye.astral.sh/

### Environment Variables

Marvin uses the following environment variables to function correctly:

- `MATRIX_HOMESERVER`: The URL of your Matrix homeserver (e.g., `https://matrix.org`)
- `MATRIX_ACCESSTOKEN`: Your Matrix access token
- `MATRIX_ROOMID`: The ID of the Matrix room where messages will be sent
- `MATRIX_MESSAGE`: The message content to be sent

### Installation

1. Clone the repository or download the script.
2. Install the required Python libraries:

   ```sh
   rye sync
   ```

3. Set up the required environment variables. You can create a `.env` file in the same directory by copying the `env.example` as the script for convenience:
   ```sh
   export MATRIX_HOMESERVER="https://matrix.org"
   export MATRIX_ACCESSTOKEN="YOUR_ACCESS_TOKEN"
   export MATRIX_ROOMID="!yourRoomID:matrix.org"
   export MATRIX_MESSAGE="Which day do you want to play?"
   ```

## Usage

To run the bot, execute the `rye run marvin` command.

## Scheduling the Script

This script uses github workflows to run every sunday.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
