import discord
from discord.commands import Option, slash_command
from discord.ext import commands
import datetime
import asyncio
import pytz
import random 
import asyncio
import requests
import json



class dailybinnywaifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bgtask = self.bot.loop.create_task(self.binny_waifu())

    async def binny_waifu(self):
        await self.bot.wait_until_ready()
        binnywaifuchannel = self.bot.get_channel(911174855821496330)
        while not self.bot.is_closed():
            if datetime.datetime.now(pytz.timezone('Australia/Brisbane')).strftime("%H:%M") == "12:00":
                waifuimage = requests.get("https://api.waifu.pics/sfw/waifu")
                waifulink = waifuimage.json()
                await binnywaifuchannel.send(waifulink["url"])
                await binnywaifuchannel.send("<@911172278090367007>")
            await asyncio.sleep(60)

def setup(bot):
    bot.add_cog(dailybinnywaifu(bot)) 