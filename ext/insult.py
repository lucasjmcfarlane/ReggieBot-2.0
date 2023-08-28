import discord
from discord.ext import commands
import random

@commands.command()
async def insult(ctx, user=""):
	insults = [
		"You're dumb, ",
		"You're an idiot, ",
		"Nobody asked, ",
		"Not gonna lie, You kinda suck, ",
		"Moron, "
	]
	message = insults[random.randint(0,len(insults)-1)]

	try: name = ctx.message.guild.get_member(int(user[2:-1])).name
	except: name = user

	if name=="": message+=ctx.author.name
	else: message+=name

	embed = discord.Embed(
		title = message,
		colour = discord.Colour.pink()
	)
	await ctx.channel.send(embed = embed)

async def setup(bot):
	bot.add_command(insult)