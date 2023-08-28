import discord
from discord.ext import commands
from cogwatch import watch
from dotenv import load_dotenv
import os
import asyncio

class ReggieBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="r ", intents=discord.Intents.all())

    @watch(path='ext', preload=True)
    async def on_ready(self):
        print('Bot ready.')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

async def main():
    client = ReggieBot()
    client.remove_command('help')
    load_dotenv()
    await client.start(os.getenv("API_TOKEN"))

asyncio.run(main())
