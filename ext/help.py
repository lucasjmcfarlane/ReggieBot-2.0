import discord
from discord.ext import commands
import os

@commands.command()
async def help(ctx):
	embed = discord.Embed(
		title = "Help",
		description = "",
		colour = discord.Colour.pink(),
	)

	embed.add_field(name="Flipcoin", value="Flips a coin.", inline=False)
	embed.add_field(name="Hello", value="Sends a simple greeting message.", inline=False)
	embed.add_field(name="Insult", value="Insults the user or the person specified.", inline=False)
	embed.add_field(name="Msgfromreggue", value="Sends a DM to the person specified.", inline=False)

	await ctx.channel.send(embed = embed)

async def setup(bot):
	bot.add_command(help)