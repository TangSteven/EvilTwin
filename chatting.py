import discord
from discord.ext import commands
import random

class Chatting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def hello(self, ctx):
        ''' responds with hello to user that called command'''
        await ctx.send(f"""Hello ```yaml
{ctx.author.name}!```""")

    @commands.command()
    async def embedtest(self, ctx):
        embed = discord.Embed(type = "link", title = "Current Song", description = " unravel acoustic version", url =  "https://www.youtube.com/watch?v=E7iEHIEbKKs")
        user_id = 115967377295802374
        user = discord.utils.get(ctx.guild.members, id=int(user_id))
        embed.set_author(name = "Tang", icon_url = user.avatar_url)
        await ctx.send(embed = embed)

    @commands.command()
    async def roll(self, ctx, rolls = 1):
        ''' Gives total and average.2f of rolls '''
        random_rolls = [random.randint(0,6) for i in range(rolls)]
        total = sum(random_rolls)
        avg = total / rolls
        await ctx.send(F"Your {rolls} rolls: **Total**: {total}, **Average**: {avg:.2f}")

    


def setup(bot):
    bot.add_cog(Chatting(bot))