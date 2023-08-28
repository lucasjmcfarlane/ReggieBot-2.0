import discord
from discord.ext import commands

@commands.command()
async def msgfromreggie(ctx, user : discord.User, *, msg):
    await user.send(msg)
    await ctx.message.add_reaction("👍")

async def setup(bot):
    bot.add_command(msgfromreggie)