import discord
from discord.ext import commands

@commands.command()
async def github(ctx):
    await ctx.send("https://github.com/lucasjmcfarlane/ReggieBot-2.0")

async def setup(bot):
    bot.add_command(github)