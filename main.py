import discord
from discord.ext import commands
from message import message_on

#-------------------Globales-------------------#

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

#-------------------EVENTOS-------------------#
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Resolver tus dudas : )"), status=discord.Status.dnd)
    await bot.tree.sync()

@bot.event
async def on_message(message):
  await message_on(message, bot)

#-------------------Arranque-------------------#

bot.run("TOKEN_DISCORD")