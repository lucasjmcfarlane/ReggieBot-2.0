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
	embed.add_field(name="Insult", value="Insults the user or the member specified.", inline=False)
	embed.add_field(name="LoveCalc", value="Calculate compatability of two members.", inline=False)
	embed.add_field(name="Msgfromreggie", value="Sends a DM to the member specified.", inline=False)
	embed.add_field(name="WelcomeSpeech", value="Sends a welcome message.", inline=False)

	embed.add_field(name="Play", value="Add the given YouTube URL to the play queue", inline=False)
	embed.add_field(name="Pause", value="Pause the currently playing YouTube video", inline=False)
	embed.add_field(name="Resume", value="Resume the currently playing YouTube video", inline=False)
	embed.add_field(name="Skip", value="Skips to the next YouTube video in the queue if there is one", inline=False)
	embed.add_field(name="Stop", value="Stop audio playback, delete the queue, and disconnect the bot", inline=False)

	embed.add_field(name="Mute", value="Mute the given member", inline=False)
	embed.add_field(name="Unmute", value="Unmute the given member", inline=False)
	embed.add_field(name="Deafen", value="Deafen the given member", inline=False)
	embed.add_field(name="Undeafem", value="Undeafen the given member", inline=False)
	embed.add_field(name="Disconnect", value="Disconnect the given member", inline=False)
	embed.add_field(name="Move", value="Move the given member into your current voice channel", inline=False)
	embed.add_field(name="Ban", value="Ban the given member", inline=False)
	embed.add_field(name="Kick", value="Kick the given member", inline=False)
	embed.add_field(name="Clear", value="Clear the given number of messages from the current channel (max=150)", inline=False)
	embed.add_field(name="Pingspam", value="Send 5 pings to the given member", inline=False)

	await ctx.channel.send(embed = embed)

async def setup(bot):
	bot.add_command(help)