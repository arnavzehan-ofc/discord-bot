import discord
from discord.ext import tasks, commands
import asyncio
import os
from datetime import datetime

TOKEN = os.getenv("TOKEN")  # IMPORTANT: Use environment variable for safety

GUILD_ID = 1375652993952776263
CHANNEL_ID = 1376217931934859284
ROLE_ID = 1376063226298499194

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")
    check_time.start()

@tasks.loop(minutes=1)
async def check_time():
    now = datetime.utcnow()
    if now.minute == 30:
        guild = bot.get_guild(GUILD_ID)
        channel = guild.get_channel(CHANNEL_ID)
        role = guild.get_role(ROLE_ID)

        if channel and role:
            await channel.send(f"⏰🍃 Yooo Wakeup {role.mention}! It’s Nourishment or Plantation Time HH:30!")

bot.run(TOKEN)
