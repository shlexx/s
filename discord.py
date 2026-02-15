import discord
import os
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive

# 1. Setup Intents
intents = discord.Intents.default()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # This syncs your slash commands so they show up in Discord
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

bot = MyBot()

@bot.tree.command(name="fatheriwishtoflip", description="father i wish to flip")
async def hello(interaction: discord.Interaction):
    # This response works in DMs, Servers, and as a User App
    await interaction.response.send_message(f"https://cdn.discordapp.com/attachments/1374010242093809674/1472571622656577598/attachment.gif")

# 2. Get the token from Secrets
keep_alive()
token = os.environ['DISCORD_TOKEN']
bot.run(token)
