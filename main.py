import discord
from discord.ext import commands
import os

TOKEN = os.environ['DISCORD_TOKEN']


import music

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(bot)

bot.run(TOKEN)
