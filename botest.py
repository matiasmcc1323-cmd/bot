import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents = intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def bye(ctx):
    await ctx.send("Bye!")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def magicball(ctx, *text: str):
    if not text:
        await ctx.send("You need to provide text!")
    else:
        answer = random.choice(["Yes", "No", "Maybe"])
        await ctx.send(answer)
        
@bot.command()
async def rps(ctx, text):
    if text in ["paper", "scissors", "rock"]:
        choice = random.choice(["paper", "scissors", "rock"])
        if text == "paper":
            if choice == "paper":
                await ctx.send(f"My choice was {choice}, it was a tie")
            elif choice == "scissors":
                await ctx.send(f"My choice was {choice}, I won")
            elif choice == "rock":
                await ctx.send(f"My choice was {choice}, you won")
        elif text == "scissors":
            if choice == "paper":
                await ctx.send(f"My choice was {choice}, you won")
            elif choice == "scissors":
                await ctx.send(f"My choice was {choice}, it was a tie")
            elif choice == "rock":
                await ctx.send(f"My choice was {choice}, I won")
        elif text == "rock":
            if choice == "paper":
                await ctx.send(f"My choice was {choice}, I won")
            elif choice == "scissors":
                await ctx.send(f"My choice was {choice}, you won")
            elif choice == "rock":
                await ctx.send(f"My choice was {choice}, it was a tie")
    else:
        await ctx.send("That's not a valid answer")

@bot.command()
async def reverse(ctx, *, text: str):
    if not text:
        await ctx.send("You need to provide text")
    else:
        result = ""
        for i in text:
            result = i + result

        await ctx.send(result)

@bot.command()
async def meme(ctx):
    listofmemes = os.listdir('memes')
    randomeme = random.choice(listofmemes)
    with open(f"memes/{randomeme}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal_photo(ctx):
    listofanimals = os.listdir("funny_animals")
    animal = random.choice(listofanimals)
    with open(f"funny_animals/{animal}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

bot.run('token')
