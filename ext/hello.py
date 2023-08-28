import discord
from discord.ext import commands

@commands.command()
async def hello(ctx):
	embed = discord.Embed(
		title = "Hi! My name is Reggie!",
		description = "I am your server's new Discord bot, created by yours truly, Yomiko12#1137",
		colour = discord.Colour.pink(),
	)
	embed.set_image(url="https://i.pinimg.com/originals/aa/01/90/aa019023148ed37537f9d22fcbe53041.gif")
	await ctx.channel.send(embed = embed)

async def setup(bot):
    bot.add_command(hello)