import discord
from discord.ext import commands
import random

@commands.command()
async def lovecalc(ctx, user1="Reggie", user2="Reggie"):

	try: user1 = ctx.message.guild.get_member(int(user1[2:-1])).name
	except: user1 = user1

	try: user2 = ctx.message.guild.get_member(int(user2[2:-1])).name
	except: user2 = user2
	
	i = random.randint(1,100)
	embed = discord.Embed(
		title = f"{user1} and {user2} : ",
		description = f"Your compatibility is {i}%!!!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = "https://i.kym-cdn.com/photos/images/original/001/461/337/f96.gif")
	await ctx.send(embed=embed)

async def setup(bot):
	bot.add_command(lovecalc)