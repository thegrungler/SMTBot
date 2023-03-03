import discord
from discord.ext import commands
import random
import SMT

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

Pixie = SMT.demon("Pixie", 1, "Dia", "Zio", "Garu")
Pixie.intro()
print("\n", SMT.dmgCalc(1,1))
#@client.event
#async def on_ready():
#    print(f'We have logged in as {client.user}')