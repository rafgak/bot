import os
import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
