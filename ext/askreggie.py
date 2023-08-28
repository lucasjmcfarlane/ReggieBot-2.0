import discord
from discord.ext import commands
import random

@commands.command()
async def askreggie(ctx):
	responses = [
	"**YES!!**",
	"**OF COURSE!!**",
	"**Yea, probably..**",
	"**idk..**",
	"**Maybe..**",
	"**It's possible..**",
	"**What kind of question is this?? There must be something seriously wrong with you.**",
	"**Bruh...**",
	"**I'm Reggie!**",
	"**NO!!**",
	"**Bruh, there is no way..**",
	"**Nahhh..**"
	]
	embed = discord.Embed(
		title = responses[random.randint(0,len(responses)-1)],
		colour = discord.Colour.pink()
	)
	await ctx.channel.send(embed = embed)


async def setup(bot):
	bot.add_command(askreggie)