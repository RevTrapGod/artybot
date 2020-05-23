from discord.ext import commands
from datetime import datetime as d


class Basic(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='ping', description='The ping commmand')
  async def ping_command(self, ctx):
    start = d.timestamp(d.now())
    msg = await ctx.send(content='Pinging')
    time = (d.timestamp(d.now()) - start) * 1000
    await msg.edit(content=f'Pong\nOne message round-trip {time}ms.')
    return