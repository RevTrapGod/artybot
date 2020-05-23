from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# don't ever commit with this token here you dumbfuck :o
bot = commands.Bot(command_prefix='k!')


@bot.command(name='echo')
async def echo(ctx, arg):
  await ctx.send(arg)

@bot.command(name="up")
async def you_up(ctx):
  await ctx.send('u up? lmao')

bot.run(TOKEN)
