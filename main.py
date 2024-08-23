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
intents.typing = True
intents.message_content = True
bot = commands.Bot(command_prefix="(", intents=intents)

xertuncord = 1114565796404928594
ragecord = 1219008436428345528 
swagballs = 938728183203758080
sharkpark = 855454505478127647

tree = bot.tree

async def typingIndicator(original_channel, typer):
    for station in bot.stations:
        if station is not None and original_channel != station:
            await station.send(f"-# {typer} is typing...")
            print(f"Sent typing notification to {station} from {original_channel}")
        elif message.author.id == 555186744593743897:
    	    return

@bot.event
async def on_typing(channel: discord.abc.Messageable, user: discord.Member | discord.User, when):
    if channel in bot.stations:
        await typingIndicator(channel, user)

@bot.event
async def on_ready():
    sent_today = False
    print(f'We have logged in as {bot.user}')
    await tree.sync(guild=discord.Object(swagballs))
    await tree.sync(guild=discord.Object(ragecord))
    await tree.sync(guild=discord.Object(xertuncord))
    await tree.sync(guild=discord.Object(sharkpark))

    # Retrieve channels after the bot is ready
    bridgeSB_1 = bot.get_channel(1274386678831644753)  # Ragecord
    bridgeSB_2 = bot.get_channel(1274458307716845608)  # SwagCord
    bridgeSB_3 = bot.get_channel(1274668145243586673)  # Xertuncord
    bridgeSB_4 = bot.get_channel(1276559880093962250)  # Shark Park

    # Debug: Ensure channels are retrieved correctly
    print(f'bridgeSB_1: {bridgeSB_1}')
    print(f'bridgeSB_2: {bridgeSB_2}')
    print(f'bridgeSB_3: {bridgeSB_3}')
    print(f'bridgeSB_4: {bridgeSB_4}')

    # Store channels in a list
    stations = [bridgeSB_1, bridgeSB_2, bridgeSB_3, bridgeSB_4]

    # Store the stations list in the bot object for later use
    bot.stations = stations


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    elif message.author.id == 555186744593743897:
    	return
    
    async def send_to_others(original_channel, embed=None):
        for station in bot.stations:
            if station is not None and original_channel != station:
                await station.send(embed=embed)
            
    async def embeddium(original_channel, links, embed=None):
        for station in bot.stations:
            if station is not None and original_channel != station:
                await station.send(embed=embed)
                await station.send(links)
                
    channel_colors = {
        bot.stations[0]: 0xffffff,  # Ragecord
        bot.stations[1]: 0xffdf00,  # SwagCord
        bot.stations[2]: 0xf78eff,  # Xertuncord
        bot.stations[3]: 0x2e008b,  # Shark Park
    }

    if message.channel in bot.stations:
        embed_color = channel_colors[message.channel]

        

        embed = discord.Embed(title='SOE "SwagBalls Passenger Train"', colour=embed_color)  
        embed.set_footer(text="Connecting the Swagosphere, one train at a time.")
        embed.set_author(
            name=f"{str(message.author)} from {str(message.guild)}",
            icon_url=str(message.author.avatar)
        )
        if not message.attachments and not message.stickers:
            embed.add_field(name="Message", value=str(message.clean_content), inline=True)
            await send_to_others(message.channel, embed=embed)
            
            url_pattern = r'https?://[^\s]+'
            non_url_text = re.sub(url_pattern, '', message.content)
            match = re.search(url_pattern, message.content)
            if match:
                url = match.group()
                await embeddium(message.channel, url, embed=embed)
            
        
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
    guilds=[discord.Object(swagballs), discord.Object(ragecord), discord.Object(xertuncord), discord.Object(sharkpark)],
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
                elif interaction.guild_id == sharkpark:
                    return 1276560153688408130
            
            def StationChannelDetermine():
                if interaction.guild_id == swagballs:
                    return 1274458307716845608
                elif interaction.guild_id == ragecord:
                    return 1274386678831644753
                elif interaction.guild_id == xertuncord:
                    return 1274668145243586673
                elif interaction.guild_id == sharkpark:
                    return 1276559880093962250
            
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

