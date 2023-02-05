import discord
import openai
import time


openai_api = "API_KEY_HERE" #openai api key
discord_token = "TOKEN_HERE" # discord bot token
api_delay = "10" # delay between open api calls in seconds. Helps to avoid users spamming api requests.

openai.api_key = openai_api
intents = discord.Intents.default()

intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Discord bot started!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith(f"<@{client.user.id}>"):
        return

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.content.replace(f'<@{client.user.id}>', '').strip()}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    await message.channel.send(response["choices"][0]["text"])
    time.sleep(api_delay)

client.run(discord_token)