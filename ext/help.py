import discord
from discord.ext import commands

@commands.command()
async def help(ctx):
	embed = discord.Embed(
		title = "Help",
		description = "",
		colour = discord.Colour.pink(),
	)

	embed.add_field(name="AskReggie", value="Ask Reggie a question.", inline=False)
	embed.add_field(name="Flipcoin", value="Flips a coin.", inline=False)
	embed.add_field(name="GitHub", value="Sends link to GitHub page.", inline=False)
	embed.add_field(name="Hello", value="Sends a simple greeting message.", inline=False)
	embed.add_field(name="Insult", value="Insults the user or the person specified.", inline=False)
	embed.add_field(name="LoveCalc", value="Calculate compatability of two people.", inline=False)
	embed.add_field(name="Msgfromreggie", value="Sends a DM to the person specified.", inline=False)
	embed.add_field(name="WelcomeSpeech", value="Sends a welcome message.", inline=False)

	embed.add_field(name="Play", value="Add the given YouTube URL to the play queue", inline=False)
	embed.add_field(name="Pause", value="Pause the currently playing YouTube video", inline=False)
	embed.add_field(name="Resume", value="Resume the currently playing YouTube video", inline=False)
	embed.add_field(name="Skip", value="Skips to the next YouTube video in the queue if there is one", inline=False)
	embed.add_field(name="Stop", value="Stop audio playback, delete the queue, and disconnect the bot", inline=False)

	await ctx.channel.send(embed = embed)

async def setup(bot):
	bot.add_command(help)