from discord import app_commands
from discord.utils import get # New import
from discord.ext import commands
from random import randint
from discord.ext import commands, tasks
import discord
import os
import asyncio
import requests
import sys
import re

TOKEN = 'MTI3MjI3MDc4MzQyMjUzMzcxMw.GzVVEr._RqefcWtLHIeeCnEhIvArnU9uYoOfi9jBNWsVI'

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="(", intents=intents)

xertuncord = 1114565796404928594
ragecord = 1219008436428345528 
swagballs = 938728183203758080

tree = bot.tree

@bot.event
async def on_ready():
    sent_today = False
    print(f'We have logged in as {bot.user}')
    await tree.sync(guild=discord.Object(swagballs))
    await tree.sync(guild=discord.Object(ragecord))
    await tree.sync(guild=discord.Object(xertuncord))

bridgeSB_1 = bot.get_channel(1274386678831644753)  # Ragecord
bridgeSB_2 = bot.get_channel(1274458307716845608)  # SwagCord
bridgeSB_3 = bot.get_channel(1274668145243586673)  # Xertuncord
    
    
@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    
    bridgeSB_1 = bot.get_channel(1274386678831644753)  # Ragecord
    bridgeSB_2 = bot.get_channel(1274458307716845608)  # SwagCord
    bridgeSB_3 = bot.get_channel(1274668145243586673)  # Xertuncord
    
    async def send_to_others(original_channel, embed=None):
        if original_channel != bridgeSB_1:
            await bridgeSB_1.send(embed=embed)
        if original_channel != bridgeSB_2:
            await bridgeSB_2.send(embed=embed)
        if original_channel != bridgeSB_3:
            await bridgeSB_3.send(embed=embed)
            
    async def embeddium(original_channel, links, embed=None):
        if original_channel != bridgeSB_1:
            await bridgeSB_1.send(embed=embed)
            await bridgeSB_1.send(links)
        if original_channel != bridgeSB_2:
            await bridgeSB_2.send(links, embed=embed)
            await bridgeSB_2.send(links)
        if original_channel != bridgeSB_3:
            await bridgeSB_3.send(links, embed=embed)
            await bridgeSB_3.send(links)
        
    if message.channel in (bridgeSB_1, bridgeSB_2, bridgeSB_3):
        embed_color = 0xffffff  # Default color
        if message.channel == bridgeSB_1: #ragecord
            embed_color = 0xffffff
        elif message.channel == bridgeSB_2: #swagcord
            embed_color = 0xffdf00
        elif message.channel == bridgeSB_3: #xertuncord
            embed_color = 0xf78eff
        #elif message.channel == bridgeSB_3: #wunkcord
         #   embed_color = 0x00ffcc

        embed = discord.Embed(title='SOE "SwagBalls Passenger Train"', colour=embed_color)  
        embed.set_footer(text="Connecting the Swagosphere, one train at a time.")
        embed.set_author(
            name=f"{str(message.author)} from {str(message.guild)}",
            icon_url=str(message.author.avatar)
        )
        if not message.attachments and not message.stickers:
            embed.add_field(name="Message", value=str(message.clean_content), inline=True)
            await send_to_others(message.channel, embed=embed)
            
            embedlinks = ["https://youtube.com", "https://tenor.com", "https://twitter.com"]
            
            if any(link in message.clean_content for link in embedlinks):
                extracted_links = []
                for link in embedlinks:
                    if link in message.clean_content:
                        # Use regular expression to extract the full URL
                        pattern = re.escape(link) + r'[^\s]*'
                        found_links = re.findall(pattern, message.clean_content)
                        extracted_links.extend(found_links)
                        
                        links_string = '\n'.join(extracted_links)        
                        
                        await embeddium(message.channel, links_string, embed=None)
        
        elif message.attachments and not message.stickers and not message.clean_content:
            embed.add_field(name=(str(message.author) + " from " + str(message.guild)), value=str("Sent an image!"), inline=True)
            attachments = message.attachments[0]
            embed.set_image(url=attachments.url)
            await send_to_others(message.channel, embed=embed)

        # https://priv.au/image_proxy?url=https%3A%2F%2Fpreview.redd.it%2Fzh4z7cem9kg51.png%3Fauto%3Dwebp%26s%3D90ff37f3925e3d8dfe41a88aafcf8f35a414d5b7&h=53cb9d9c3e788179e40d2734bbe2c589fbf4a8f974421588080b194e123625ee
        # ^^^^^ me, probably
        
        elif message.attachments and message.clean_content and not message.stickers:
            embed.add_field(name=(str(message.author) + " from " + str(message.guild)), value=str(message.clean_content), inline=True)
            attachments = message.attachments[0]
            embed.set_image(url=attachments.url)
            await send_to_others(message.channel, embed=embed)
        
        elif not message.attachments and message.stickers:
            embed.add_field(name=(str(message.author) + " from " + str(message.guild)), value=str("Sent a sticker!"), inline=True)
            sticker = message.stickers[0]
            embed.set_image(url=sticker.url)
            await send_to_others(message.channel, embed=embed)

        
            
@tree.command(
    name="ticket",
    description="Buy timed tickets for the SwagBalls Passanger Train",
    guilds=[discord.Object(swagballs), discord.Object(ragecord), discord.Object(xertuncord)],
)
@app_commands.describe(mins="How many minutes do you want your ticket to be usable for. 1min:1000UBUX ratio.")
async def tickets(interaction: discord.Interaction, mins: int):
    # Deducting
    url = f"https://unbelievaboat.com/api/v1/guilds/{interaction.guild_id}/users/{interaction.user.id}"
    if mins <= 0:
        await interaction.response.send_message("```INVALID AMOUNT\nPlease enter valid amount.```")
    else:
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMjcyMzMyMzM5NjkwNzMzNTk2IiwiaWF0IjoxNzIzNDE4MDY4fQ.h5gGc4ZRWOcH1DkYlB-brvUAR91Sij1zckoQdvxG5eU"
        }
        responseC = requests.get(url, headers=headers) 
        bal = responseC.json().get("cash") #gets balance

        if bal >= 1000 * mins: #checks if you have enough
            payload = {
                "reason": "TRAINTICKET\"SBTRAIN\"\"",
                "cash": -1000 * mins
            }
            
            response = requests.patch(url, json=payload, headers=headers)
            
            url = "https://unbelievaboat.com/api/v1/guilds/938728183203758080/users/432437043956809738"
            
            payload = {
                "reason": "TRAINTICKET\"SBTRAIN\"\"",
                "bank": 1000 * mins
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMjcyMzMyMzM5NjkwNzMzNTk2IiwiaWF0IjoxNzIzNDE4MDY4fQ.h5gGc4ZRWOcH1DkYlB-brvUAR91Sij1zckoQdvxG5eU"
            }
            response = requests.patch(url, json=payload, headers=headers)

            
            def TicketRoleIdDetermine():
                if interaction.guild_id == swagballs:
                    return 1274461298960105543
                elif interaction.guild_id == ragecord:
                    return 1274385477126062182
                elif interaction.guild_id == xertuncord:
                	return 1274668418506686527
            
            def StationChannelDetermine():
                if interaction.guild_id == swagballs:
                    return 1274458307716845608
                elif interaction.guild_id == ragecord:
                    return 1274386678831644753
                elif interaction.guild_id == xertuncord:
                    return 1274668145243586673
            
            await interaction.response.send_message(f"### Transaction succesful!\nYou bought {mins} ticket(s) to use in the <#{StationChannelDetermine()}> station.\n{1000 * mins} UBUX have been deducted from your cash account.\n```SENDER: {interaction.user}\nBENEFACTOR(S): 90% - SOE.SWAG.PSNG.TRAN///10% - AWSM.SCE.CNGL.LTD\nAMOUNT: {1000 * mins}.\nTHANK YOU FOR USING OUR SERVICES!```")
            await interaction.user.add_roles(discord.Object(TicketRoleIdDetermine()))
            await asyncio.sleep(mins * 60)
            await interaction.user.remove_roles(discord.Object(TicketRoleIdDetermine()))
            await interaction.followup.send(f"{interaction.user.mention}, your ticket has expired.", ephemeral=True)
            
            me = bot.get_user(432437043956809738)
            await me.send(f'{1000 * mins} acquired.')
        else:
            await interaction.response.send_message("```LOW BALANCE\nPlease try lower amount.\n-# This might mean that you dont have enough **cash**, so make sure to withdraw some!```")
        
@tree.command(
    name="depot",
    description="Debug: Set the bot for maintanance",
    guild=discord.Object(ragecord),
)
async def kill(interaction: discord.Interaction, secs: int):
    if interaction.user.id == 432437043956809738:
        asyncio.sleep(secs)
        sys.exit("Maintanance")
    else:
        await interaction.response.send_message("Missing permissions", ephemeral=True)

bot.run(TOKEN)
