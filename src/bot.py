from discord.ext import commands
import discord
from basic import Basic

class Artemis(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix=['k!', 'K!', 'a!', 'A!'], case_insensitive = True) # don't think we need both cases with this set to true

    self.add_cog(Basic(self))
  
  async def on_command_error(self, ctx, exception):
    if isinstance(exception, commands.MissingRequiredArgument):
      await self.send_command_help(ctx)
  
  async def send_command_help(self, ctx):
    return await ctx.send_help(ctx.command)