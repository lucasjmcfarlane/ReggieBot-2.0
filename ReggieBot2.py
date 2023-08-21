import discord
import reggieEmbeds as e

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(msg):
	if msg.author == client.user: return
	msg.content = msg.content.lower()
	if msg.content.startswith("r hello"): await e.hello(msg)
	elif msg.content.startswith("r flipcoin"): await e.flipcoin(msg)
	elif msg.content.startswith("r insult"): await e.insult(msg)
	elif msg.content.startswith("r askreggie"): await e.askreggie(msg)
	# elif msg.content.startswith("r msgfromreggie"): await e.msgfromreggie(msg)
	# elif msg.content.startswith("r lovecalc"): await e.lovecalc(msg)
	# elif msg.content.startswith("r owo"): await e.owo(msg)
	# elif msg.content.startswith("r uwu"): await e.uwu(msg)
	# elif msg.content.startswith("r ppsize"): await e.ppsize(msg)
	# elif msg.content.startswith("r rate"): await e.rate(msg)
	# elif msg.content.startswith("r reggiepic"): await e.reggiepic(msg)
	# elif msg.content.startswith("r clear"): await e.clear(msg)
	# elif msg.content.startswith("r pingspam"): await e.pingspam(msg)
	# elif msg.content.startswith("r reddit"): await e.reddit(msg)

client.run('')