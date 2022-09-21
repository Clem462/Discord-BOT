import random
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 357048653875249152  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1, 6))

@bot.event
async def hello(message):
    await bot.process_commands(message)
    if message.content == "Salut tout le monde":
        await message.channel.send(f"Salut tout seul {message.author.mention}")
    else:
        await message.channel.send("Bye")



token = "MTAyMjE5MjgyMjMwNjIxODAwNg.GmlaZh.KmpNPoPllMUIkvnfAZV_lTjJoAfD3dxLAImCrk"
bot.run(token)  # Starts the bot
