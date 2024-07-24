import os
import discord

TOKEN = os.getenv('OTYyNjk5MDUxNDQ5NTkzOTc2.G2QIav.061T89az3FeWuw3x9e86S52N9wnhiUDw8YbA3Y')

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
