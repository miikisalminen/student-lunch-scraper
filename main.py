import os
import discord
from scraper import parse
from dotenv import load_dotenv


load_dotenv()
TOKEN = "NzQ4Nzc1MjI5MzE2MjY4MDgy.X0iVRg.qA3IVneiR3Ez-vcMgTdWweMVZmE"

client = discord.Client()

@client.event

async def on_message(message):
	if message.content =="!menu":
		response = parse()
		print(response)
		await message.channel.send(response)
		print("peppu")

async def on_ready():
	print("ONLINE")

client.run(TOKEN)