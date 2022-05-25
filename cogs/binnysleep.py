import discord
from discord.commands import Option, slash_command
from discord.ext import commands
import datetime
import asyncio
import pytz
import random 

binnysleeplist = ["<@294956096353730570> It's time to go to sleep!", "<@294956096353730570> go to sleep now you moron!", "<@294956096353730570> It's time to go to sleep you absolute degenerate", "stop watching anime and go to sleep <@294956096353730570>", "go to sleep you have school tomorrow you fucking imbecile <@294956096353730570>", "dude you're not cool when you pull an all nighter go to fucking sleep <@294956096353730570>"]

class gotosleep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bgtask = self.bot.loop.create_task(self.go_to_sleep())

    async def go_to_sleep(self):
        await self.bot.wait_until_ready()
        binnyalarmchannel = self.bot.get_channel(925409964695105606)
        while not self.bot.is_closed():
            if datetime.datetime.now(pytz.timezone('Australia/Brisbane')).strftime("%H:%M") == "00:00":
                await binnyalarmchannel.send(random.choice(binnysleeplist))
            await asyncio.sleep(60)

def setup(bot):
    bot.add_cog(gotosleep(bot)) 