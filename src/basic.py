from discord.ext import commands
from datetime import datetime as d
from timer import Timer
import random

class Basic(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.meow_timer = Timer(self.meow)

  @commands.command(name='ping', description='The ping commmand')
  async def ping_command(self, ctx):
    start = d.timestamp(d.now())
    msg = await ctx.send(content='Pinging')
    time = (d.timestamp(d.now()) - start) * 1000
    await msg.edit(content=f'Pong\nOne message round-trip {time}ms.')
    return

  @commands.command(name='echo', description='The echo command')
  async def echo_command(self, ctx):
    msg = ctx.message.content

    prefix = ctx.prefix
    alias = ctx.invoked_with
    text = msg[len(prefix) + len(alias):]
    if text == '':
      await ctx.send(content='You need to specify the text!')
    else:
      await ctx.send(content=f'**{text}**')
    return


  async def meow(self):
    if random.random() < .15:
      channel =  self.bot.get_channel(710729000556953654) #hard coded channel id for general 
      await channel.send('meow')
    return

  



    