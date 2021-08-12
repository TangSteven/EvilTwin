import discord
from discord.ext import commands
import youtube_dl
from collections import deque

FFMPEG_OPTIONS = {
                'before_options':
                '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'
            }
YDL_OPTIONS = {'format': 'bestaudio'}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.q = deque()

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel :(")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:  # if bot is not in voice channel
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        try:
            vc = ctx.voice_client
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(
                    url2, **FFMPEG_OPTIONS)
                vc.play(source)
            embed = discord.Embed(title = "Current Song", description = f"Playing **{info.get('title', None)}**", color = discord.Colour.red(), url = url)
            await ctx.send(embed = embed)
        except discord.ClientException:
            print("There is already a song playing")
            self.q.append(url)
            await ctx.send(f"Queued: **{info.get('title', None)}** by {ctx.author.name}")
            # add to song queue
        
        # after each song ends, go to next song at top of queue

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.pause()
            await ctx.send("Paused! ")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.resume()
            await ctx.send("Resuming! ")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client != None:
            ctx.voice_client.stop()
            await ctx.send("Stopping! ")
    
    @commands.command()
    async def queue(self, ctx):
        embed = discord.Embed(title = "Queue")
        counter = 1
        for url in self.q:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            embed.add_field(name = f"{counter})", value = f"{info.get('title', None)}", inline = False)
        await ctx.send(embed = embed)

#add queue
#add looping

def setup(bot):
    bot.add_cog(Music(bot))
