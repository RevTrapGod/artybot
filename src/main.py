from discord.ext import commands
import discord

# don't ever commit with this token here you dumbfuck :o
token =  '%placeholder%'
bot = commands.Bot(command_prefix='k!')


@bot.command(name='echo')
async def echo(ctx, arg):
  await ctx.send(arg)

bot.run(token)
