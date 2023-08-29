from discord.ext import commands, tasks
import discord
import asyncio
import yt_dlp

voice_clients = {} #dictionary of voice clients where key is the voice channel id
queues = {} #dictionary of queue arrays of ytdl data where key is the voice channel id
ctxs = {} #ctx for all currently playing voice clients necessary for automatic skip and stop

#https://github.com/Lenart12/GodecBot/blob/master/ytdl.py thank you for the ytdl and ffmpeg config
ytdl = yt_dlp.YoutubeDL({ #configure options for youtube_dl
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
})
ffmpeg_options = { #configure options for ffmpeg
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

#Skip to the next song in queue if playback stops, or disconnect bot if nothing left in queue
@tasks.loop(seconds=5)
async def autoplay():
    for key in voice_clients.keys(): #iterate through running voice clients

        #if the voice client is NOT playing and is NOT paused:
        if not voice_clients[key].is_playing() and not voice_clients[key].is_paused():
            if len(queues[key]) > 0: #if the queue is NOT empty:
                await skip(ctxs[key]) #play next track in queue.
            else: #if the queue Is empty:
                await stop(ctxs[key]) #disconnect the bot and delete corresponding data

#add a song to the queue
@commands.command()
async def play(ctx, url=""):
    try:
        #this is magic to me idk
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        
        #ensure dictionary for guild contains an array
        try: queue = queues[ctx.message.guild.id]
        except: queues[ctx.message.guild.id] = []

        #add song data to the queue and ctx to ctxs dictionary
        queues[ctx.message.guild.id].append(data['url'])
        ctxs[ctx.message.guild.id] = ctx

        #start playback if bot is not already playing
        try:
            if voice_clients[ctx.message.guild.id].is_playing(): pass
        except: await skip(ctx)

        #start the autoplay task if not already running
        try: autoplay.start()
        except: pass

        #react with thumbs up if all goes well
        await ctx.message.add_reaction("👍")

    except: #react with warning if something failed
        await ctx.message.add_reaction("⚠️")

#start playback of next song in the queue
@commands.command()
async def skip(ctx):

    try: #create a voice client if one hasn't been created already
        voice_client = await ctx.message.author.voice.channel.connect()
        voice_clients[ctx.message.guild.id] = voice_client
    except: pass

    #stop current playback if there is one, and start next song in queue
    try:
        player = discord.FFmpegPCMAudio(queues[ctx.message.guild.id].pop(0), **ffmpeg_options)
        voice_clients[ctx.message.guild.id].stop()
        voice_clients[ctx.message.guild.id].play(player)
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("⚠️")

#pause playback
@commands.command()
async def pause(ctx):
    try:
        voice_clients[ctx.message.guild.id].pause()
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("⚠️")

#resume playback
@commands.command()
async def resume(ctx):
    try:
        voice_clients[ctx.message.guild.id].resume()
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("⚠️")

#stop playback, disconnect the bot, delete all associated data
@commands.command()
async def stop(ctx):
    try:
        voice_clients[ctx.message.guild.id].stop()
        await voice_clients[ctx.message.guild.id].disconnect()
        del voice_clients[ctx.message.guild.id]
        del queues[ctx.message.guild.id]
        del ctxs[ctx.message.guild.id]
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("⚠️")

async def setup(bot):
    bot.add_command(play)
    bot.add_command(skip)
    bot.add_command(pause)
    bot.add_command(resume)
    bot.add_command(stop)