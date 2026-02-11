import discord
from botlogic import gen_pass
from botlogic import flip_a_coin
from botlogic import random_number

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$ranpass'):
        password = gen_pass(10)
        await message.channel.send(password)
    elif message.content.startswith('$flipacoin'):
        coin = flip_a_coin()
        await message.channel.send(coin)
    elif message.content.startswith('$rannum'):
        number = random_number(100)
        await message.channel.send(str(number))
    else:
        await message.channel.send(message.content)

client.run("token")
