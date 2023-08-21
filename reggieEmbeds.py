import discord
import random

async def hello(msg):
	embed = discord.Embed(
		title = "Hi! My name is Reggie!",
		description = "I am your server's new Discord bot, created by yours truly, Yomiko12#1137",
		colour = discord.Colour.magenta(),
	)
	embed.set_image(url="https://i.pinimg.com/originals/aa/01/90/aa019023148ed37537f9d22fcbe53041.gif")
	await msg.channel.send(embed = embed)


async def flipcoin(msg):
	i = random.randint(1,2)
	if i==1: headsTails = "Heads!"
	else: headsTails = "Tails!"
	embed = discord.Embed(
		title = headsTails,
		colour = discord.Colour.magenta()
	)
	embed.set_image(url="https://media.giphy.com/media/gVROkjyShPnos/giphy.gif")
	await msg.channel.send(embed = embed)


async def insult(msg):
	insults = [
	"You're dumb ",
	"You're an idiot, ",
	"Nobody asked, ",
	"Not gonna lie, You kinda suck ",
	  "Moron "
	]
	name = msg.content[9:]
	if name=="":
		message = insults[random.randint(0,len(insults)-1)] + msg.author.name
	else:
		message = insults[random.randint(0,len(insults)-1)] + name
	embed = discord.Embed(
		title = message,
		colour = discord.Colour.magenta()
	)
	await msg.channel.send(embed = embed)


async def askreggie(msg):
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
		colour = discord.Colour.magenta()
	)
	await msg.channel.send(embed = embed)
