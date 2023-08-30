import discord
from discord.ext import commands
from discord.ext.commands import has_guild_permissions

#MUTE
@commands.command()
@has_guild_permissions(mute_members=True)
async def mute(ctx, member: discord.Member):
    await member.edit(mute=True)
@mute.error
async def mute_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#UNMUTE
@commands.command()
@has_guild_permissions(mute_members=True)
async def unmute(ctx, member: discord.Member):
    await member.edit(mute=False)
@unmute.error
async def unmute_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#DEAFEN
@commands.command()
@has_guild_permissions(deafen_members=True)
async def deafen(ctx, member: discord.Member):
    await member.edit(deafen=True)
@deafen.error
async def deafen_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#UNDEAFEN
@commands.command()
@has_guild_permissions(deafen_members=True)
async def undeafen(ctx, member: discord.Member):
    await member.edit(deafen=False)
@undeafen.error
async def undeafen_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#DISCONNECT
@commands.command()
@has_guild_permissions(move_members=True)
async def disconnect(ctx, member: discord.Member):
    await member.edit(voice_channel=None)
@disconnect.error
async def disconnect_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#MOVE
@commands.command()
@has_guild_permissions(move_members=True)
async def move(ctx, member: discord.Member):
    await member.edit(voice_channel=ctx.message.author.voice.channel)
@move.error
async def move_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#BAN
@commands.command()
@has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
	await ctx.guild.ban(member, reason="Because")
@ban.error
async def ban_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

#KICK
@commands.command()
@has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
	await ctx.guild.kick(member, reason="Because")
@kick.error
async def kick_error(ctx, error):
    await ctx.reply("**You are missing permissions or did something wrong!**")

@commands.command()
@has_guild_permissions(manage_messages=True)
async def clear(ctx, amount=2):
     if (amount > 150): amount = 150
     await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx, error):
	await ctx.reply("**You are missing permissions or did something wrong**")

@commands.command()
async def pingspam(ctx, member: discord.Member):
     for i in range(5):
          await ctx.send(member.mention)


async def setup(bot):
	bot.add_command(mute)
	bot.add_command(unmute)
	bot.add_command(deafen)
	bot.add_command(undeafen)
	bot.add_command(disconnect)
	bot.add_command(move)
	bot.add_command(ban)
	bot.add_command(kick)
	bot.add_command(clear)
	bot.add_command(pingspam)