import os
import discord
from scraper import parse


TOKEN = "BOT TOKEN"

client = discord.Client()

@client.event

async def on_message(message):
	if message.content =="!menu":
		response = parse()
		print(response)
		await message.channel.send(response)

async def on_ready():
	print("ONLINE")

client.run(TOKEN)
