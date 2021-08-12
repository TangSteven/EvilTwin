import discord
from discord.ext import commands
import os

import music
import chatting

TOKEN = os.environ['DISCORD_TOKEN']



aactivity = discord.Game("with fire", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), activity = aactivity)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


cogs = [music, chatting]

for i in range(len(cogs)):
    cogs[i].setup(bot)

bot.run(TOKEN)
