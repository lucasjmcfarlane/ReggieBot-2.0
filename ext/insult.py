import discord
from discord.ext import commands
import random

@commands.command()
async def insult(ctx):
	insults = [
		"You're dumb, ",
		"You're an idiot, ",
		"Nobody asked, ",
		"Not gonna lie, You kinda suck, ",
		"Moron, "
	]
	print("Test")
	name = ctx.message.content[9:]
	if name=="":
		message = insults[random.randint(0,len(insults)-1)] + ctx.author.name
	else:
		message = insults[random.randint(0,len(insults)-1)] + name
	embed = discord.Embed(
		title = message,
		colour = discord.Colour.pink()
	)
	await ctx.channel.send(embed = embed)

async def setup(bot):
	bot.add_command(insult)