import discord
from discord.ext import commands

@commands.command()
async def msgfromreggie(ctx, user="", msg=""):
	try:
		user = ctx.message.guild.get_member(int(user[2:-1]))
		await user.send(msg)
		await ctx.message.add_reaction("👍")
	except:
		await ctx.message.add_reaction("⚠️")

async def setup(bot):
	bot.add_command(msgfromreggie)