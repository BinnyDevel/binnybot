import discord, os

intents = discord.Intents().all()
bot = discord.Bot(intents=intents)

# Events

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}");
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Binny's Sleep Schedule"))

# Run

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
bot.run("yourmother")
