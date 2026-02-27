import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.command()
async def stock(ctx):
    await ctx.send("Blox Fruits Stock Update Coming Soon!")

bot.run(os.getenv("TOKEN"))
