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
CurrentDemons = {}
error1 = "You are not a player!"
error2 = "Code didn't work here"
#Creates a new player at level one
@tree.command(name="newplayer", description="You can start finding demons!")
async def newplayer(interaction):
    if EZ.checkKey(PlayerList, interaction.user.id) == True:
        return await interaction.response.send_message("You have already entered the world of demons", ephemeral=True)
    PlayerList[interaction.user.id] = SMT.player(interaction.user.id, 1, {})
    await interaction.response.send_message("You have been summoned!")

#Encounter a demon!!
#Needs a way to take the encounter and push it into a new slash command for negotiation
#I plan to do this by Creating a new dictionary that has the key as the user, and the value will be the disctionary 
#containing only the encounter obtained in this command
@tree.command(name="encounter", description="Find a demon!")
async def encounter(interaction):
    if EZ.checkKey(PlayerList, interaction.user.id) == True:
        encounter = SMT.encountering(PlayerList[interaction.user.id].lvl)
        #For loop with one value. There has GOT to be a better way of doing this but I can't figure it out right now
        for k, v in encounter.items():
            demon = k
            lvl = str(v)
        CurrentDemons.update({interaction.user.id:encounter})
        await interaction.response.send_message("You encountered a level " + lvl + " " + demon + "!")
    else:
        await interaction.response.send_message(error1, ephemeral=True)

#Temporary command for testing negotiation and other things at any level
#Will be removed before it is officially published
@tree.command(name="setlvl", description="Temp command to set level")
async def levelup(interaction, newlvl: int ):
    PlayerList[interaction.user.id].lvl = newlvl
    await interaction.response.send_message("You have leveled up to level " + str(PlayerList[interaction.user.id].lvl))

#This command will be how a player obtains a new demon. It calls a function which returns true or false,
#true being you did obtain a new demon, and vice versa. It then adds the new demon into the player's storage
@tree.command(name="negotiate", description="Have the demon join your party!")
async def negotiate(interaction):
    if EZ.checkKey(PlayerList, interaction.user.id) == True:
        if EZ.checkKey(CurrentDemons, interaction.user.id) == True:
            for k, v in CurrentDemons[interaction.user.id].items():
                demon = k
                demonlvl = v             
            if SMT.negotiation(PlayerList[interaction.user.id].lvl, demonlvl) == True:
                PlayerList[interaction.user.id].storage.update({demon:demonlvl})
                await interaction.response.send_message(demon + " has joined your party!")
            else:
                await interaction.response.send_message(demon + " did not join your party")
        else:
            await interaction.response.send_message("There are no demons to negotiate with!")
    else: 
        await interaction.response.send_message(error1, ephemeral=True)

#Prints the dictionary that represents a player's demon storage
@tree.command(name="checkparty", description="shows what demons you have")
async def checkparty(interaction):
    if EZ.checkKey(PlayerList, interaction.user.id) == True:
        embedVar = discord.Embed(title=interaction.user.display_name)
        embedVar.add_field(name="Your demon storage: ", value=EZ.printDict(PlayerList[interaction.user.id].storage))
        await interaction.response.send_message(embed=embedVar)
    else:
        await interaction.response.send_message(error1, ephemeral=True)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="with your balls"))
  print("syncing commands")
  await tree.sync()
  print("commands are Ready!")
client.run(DISCORD_TOKEN)