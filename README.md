# OpenAI Discord Bot

A Discord bot powered by OpenAI's GPT-3 language model API. The bot is designed to respond to user requests in the Discord chat by completing the prompt given by the user.

## Prerequisites
- [Discord account](https://discord.com/register)
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- [Python 3.x](https://www.python.org/downloads/)

## Setup Discord application

1. Create a new Discord application [here](https://discord.com/developers/applications). Name it what ever you want.

2. On the left clolumn select bot and create a new bot. Name your bot and choose its avatar photo.

3. Under 'Privileged Gateway Intents' enable the following
    - PRESENCE INTENT
    - SERVER MEMBERS INTENT
    - MESSAGE CONTENT INTENT
 
 4. Click on 'OAuth2' on the left column
 
 5. Click on 'URL Generator'
 
 6. Under SCOPES check 'bot' and under BOT PERMISSIONS check 'Administrator'.
 
 7. At the bottom of the web page under GENERATED URL you will see a URL. Copy and paste the URL in a web browser to join the bot to your Discord server.


## Installation

1. Clone this repository to your machine:
```
git clone https://github.com/christian45410/openai-discord-bot.git
```

2. Navigate to the project directory:
```
cd openai-discord-bot
```

3. Install the required packages using pip:
```
pip install -r requirements.txt
```
4. Edit the varibles in bot.py

```python
openai_api = "API_KEY_HERE" # openai api key
discord_token = "TOKEN_HERE" # discord bot token
api_delay = "10" # delay between open api calls in seconds. Helps to avoid users spamming api requests.
```

5. Run the bot:
```
python bot.py
```

## Interact with bot in Discord

1. Tag the bots name in discord
```
@MyBot hello! What time is it?
```
