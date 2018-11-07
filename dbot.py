import discord
from discord.ext import commands
import asyncio
import random
from time import sleep

from Bot import ChatBot as bot

ob = bot.ChatBot.getBot()

bot = commands.Bot(command_prefix='!', description="BotCosby")

f = open("token")
t = f.read()
f.close()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description="Conversation")
async def echo(text):
    """Have a Cosby-sation!"""
    await bot.say(ob.response(text))

bot.run(t)
