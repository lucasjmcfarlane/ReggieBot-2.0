import discord
from discord.ext import commands
import random

@commands.command()
async def flipcoin(ctx):
	i = random.randint(1,2)
	if i==1: headsTails = "Heads!"
	else: headsTails = "Tails!"
	embed = discord.Embed(
		title = headsTails,
		colour = discord.Colour.pink()
	)
	embed.set_image(url="https://media.giphy.com/media/gVROkjyShPnos/giphy.gif")
	await ctx.channel.send(embed = embed)

async def setup(bot):
    bot.add_command(flipcoin)