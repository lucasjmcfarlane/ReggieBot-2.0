import discord
from discord.ext import commands
import random

@commands.command()
async def ppsize(ctx):
	length = random.randint(1,15)

	pp="8"
	for i in range(length): pp+="="
	pp+="D\n"

	if (length > 10):
		descrip=" **NICE!**"
	elif (length>5 and length<=10):
		descrip=" **Not too bad!**"
	else:
		descrip=" **That's pretty rough...**"
	await ctx.send(pp)

	embed = discord.Embed(
		title = pp,
		description = descrip,
		colour = discord.Colour.pink()
	)
	await ctx.send(embed=embed)

async def setup(bot):
	bot.add_command(ppsize)