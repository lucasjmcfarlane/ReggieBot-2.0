import discord
from discord.ext import commands, tasks
import asyncio
import yt_dlp

voice_clients = {}
queues = {}
ctxs = {}

opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0',
}
ytdl = yt_dlp.YoutubeDL(opts)

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

@tasks.loop(seconds=5)
async def coroutine():
    for key in voice_clients.keys():
        if not voice_clients[key].is_playing():
            await skip(ctxs[key])

@commands.command()
async def play(ctx, url=""):
    try:
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        
        try: queue = queues[ctx.message.guild.id]
        except: queues[ctx.message.guild.id] = []
        queues[ctx.message.guild.id].append(data['url'])

        ctxs[ctx.message.guild.id] = ctx

        try:
            if voice_clients[ctx.message.guild.id].is_playing():
                print("already playing, do not start playback")
        except:
            await skip(ctx)

        try: coroutine.start()
        except: print("Coroutine already running!")

        await ctx.message.add_reaction("👍")

    except Exception as e:
        print(e)
        await ctx.message.add_reaction("⚠️")

@commands.command()
async def skip(ctx):
    try:
        voice_client = await ctx.message.author.voice.channel.connect()
        voice_clients[ctx.message.guild.id] = voice_client
    except:
        print("a voice client has already been created!")

    try:
        player = discord.FFmpegPCMAudio(queues[ctx.message.guild.id].pop(0), **ffmpeg_options)
        voice_clients[ctx.message.guild.id].stop()
        voice_clients[ctx.message.guild.id].play(player)
        await ctx.message.add_reaction("👍")
    except Exception as e:
        print(e)
        await ctx.message.add_reaction("⚠️")

@commands.command()
async def pause(ctx):
    try:
        voice_clients[ctx.message.guild.id].pause()
        await ctx.message.add_reaction("👍")
    except Exception as e:
        print(e)
        await ctx.message.add_reaction("⚠️")

@commands.command()
async def resume(ctx):
    try:
        voice_clients[ctx.message.guild.id].resume()
        await ctx.message.add_reaction("👍")
    except Exception as e:
        print(e)
        await ctx.message.add_reaction("⚠️")

@commands.command()
async def stop(ctx):
    try:
        voice_clients[ctx.message.guild.id].stop()
        await voice_clients[ctx.message.guild.id].disconnect()
        del voice_clients[ctx.message.guild.id]
        del queues[ctx.message.guild.id]
        del ctxs[ctx.message.guild.id]
        await ctx.message.add_reaction("👍")
    except Exception as e:
        print(e)
        await ctx.message.add_reaction("⚠️")

async def setup(bot):
    bot.add_command(play)
    bot.add_command(skip)
    bot.add_command(pause)
    bot.add_command(resume)
    bot.add_command(stop)