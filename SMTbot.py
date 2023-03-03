import discord
from discord import app_commands
import random
import SMT
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

PlayerList = {}

@tree.command(name="NewPlayer", description="You can start finding demons!")
async def NewPlayer(interaction):
    if SMT.CheckKey() == True:
        return
    PlayerList[interaction.user.id] = SMT.player(interaction.user.id, 1, [])
    await interaction.response.send_message("You have been summoned!")
    


@tree.command(name="Encounter", description="Find a demon!")
async def encounter(interaction):
    encounter = SMT.encountering(1)
    message = encounter.intro()
    await interaction.response.send_message(message)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="with your balls"))
  print("syncing commands")
  await tree.sync()
  print("commands are Ready!")
client.run(DISCORD_TOKEN)