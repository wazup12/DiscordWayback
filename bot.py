# This example requires the 'message_content' intent.

import discord, json


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$ping'):
        await message.channel.send(f'pong {message.author.mention}')

def get_keys(path):
	with open(path) as f:
		return json.load(f)

token = get_keys(".secret/wayback.json")['API_Key']
client.run(token)
