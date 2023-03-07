import discord
from discord import app_commands
import random
from dotenv import load_dotenv
import os

import SMT
import EZ

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

PlayerList = {}

#Creates a new player at level one
@tree.command(name="newplayer", description="You can start finding demons!")
async def newplayer(interaction):
    if EZ.checkKey(PlayerList, interaction.user.id) == True:
        return await interaction.response.send_message("You have already entered the world of demons", ephemeral=True)
    PlayerList[interaction.user.id] = SMT.player(interaction.user.id, 1, [])
    await interaction.response.send_message("You have been summoned!")

#Encounter a demon!!
#Needs a way to take the encounter and push it into a new slash command for negotiation
#I plan to do this by Creating a new dictionary that has the key as the user, and the value will be the disctionary 
#containing only the encounter obtained in this command
@tree.command(name="encounter", description="Find a demon!")
async def encounter(interaction):
    encounter = SMT.encountering(PlayerList[interaction.user.id].lvl)
    #For loop with one value. There has GOT to be a better way of doing this but I can't figure it out right now
    for k, v in encounter.items():
        demon = k
        lvl = str(v)
    await interaction.response.send_message("You encountered a level " + lvl + " " + demon + "!")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="with your balls"))
  print("syncing commands")
  await tree.sync()
  print("commands are Ready!")
client.run(DISCORD_TOKEN)