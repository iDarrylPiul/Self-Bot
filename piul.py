from colorama import Fore
from discord.ext import commands
import discord

token = ""


bot = commands.Bot(command_prefix = ("?", ".", "x", "$", "-", "#"), self_bot = True)

@bot.event
async def on_ready():
  await bot.change_presence(activity = discord.Streaming(name = "Me gusta la cerveza fria y vos cuando reis.", url = "https://www.twitch.tv/iww1234"))
  print(f"{Fore.GREEN}Self-Bot loggeado en la cuenta {Fore.RED}{bot.user}")

@bot.command()
async def purge(message, string):
    async for msg in message.channel.history(limit = int(string)):
        if msg.author == bot.user:
            try:
                await msg.delete()
            except:
                pass

while True:
  try:
    bot.run(token, bot = False)
  except:
    print(f"{Fore.GREEN}El token de la cuenta es inválido.")
    quit()
