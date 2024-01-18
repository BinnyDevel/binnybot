from discord.ext import commands
from discord_slash import cog_ext
import datetime
import asyncio
import pytz
import requests

class DailyBinnyWaifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bgtask = self.bot.loop.create_task(self.binny_waifu())

    async def binny_waifu(self):
        await self.bot.wait_until_ready()
        binnywaifuchannel = self.bot.get_channel(911174855821496330)

        while not self.bot.is_closed():
            now_brisbane = datetime.datetime.now(pytz.timezone('Australia/Brisbane'))

            if now_brisbane.hour == 12 and now_brisbane.minute == 0:
                waifuimage = requests.get("https://api.waifu.pics/sfw/waifu")
                waifulink = waifuimage.json()
                await binnywaifuchannel.send(waifulink["url"])
                await binnywaifuchannel.send("<@911172278090367007>")

            await asyncio.sleep(60)

def setup(bot):
    bot.add_cog(DailyBinnyWaifu(bot))
