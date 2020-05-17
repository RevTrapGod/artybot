from discord.ext import commands
import discord

class ArtemisBot(commands.Bot):
  def __init__(self):
    self.command_prefix = 'k!'