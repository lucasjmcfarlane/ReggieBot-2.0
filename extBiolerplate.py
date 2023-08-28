import discord
from discord.ext import commands

@commands.command()
async def nameOfCommand(ctx):
    print("Your command goes here!")


async def setup(bot):
    bot.add_command(nameOfCommand)