from discord.ext import commands
from datetime import datetime as d
from timer import Timer
from periodic import Periodic
import random
from googletrans import Translator

class Basic(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.meow_timer = Periodic(60 * 5, self.meow)
    self.set_hunger_level()
    self.translator = Translator()

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

  @commands.command(name='feed', description='Feed Artemis so she won\'t meow for 5 hours')
  async def feed_command(self, ctx):
    self.should_meow = False
    Timer(60 * 60 * 5, self.set_hunger_level)
    await ctx.send('Thanks for feeding me ILY!')
    return

  @commands.command(name='fuckboi', description='Arty says sum shi')
  async def fuckbot_command(self, ctx):
    phrases = [
      'u up? lmao', 
      'send nudes', 
      'what\'s poppin', 
      'wyd bb', 
      'show nip bb', 
      'u should smile', 
      'i\'m not like other cats', 
      'lookin juicy'
    ]

    await ctx.send(random.choice(phrases))
    return


  @commands.command(name='translate', description='Arty translates stuff to Korean')
  async def translate_command(self, ctx):
    msg = ctx.message.content
    prefix = ctx.prefix
    alias = ctx.invoked_with
    text = msg[len(prefix) + len(alias):]
    translation_result = self.translator.translate(text, dest='ko')
    await ctx.send(translation_result.text)
    return

  async def meow(self):
    if self.should_meow and random.random() < .75 :
      channel =  self.bot.get_channel(714225123368108072) #hard coded channel id for general 
      await channel.send('meow')
    return

  def set_hunger_level(self):
    self.should_meow = True





  

  

  



    
