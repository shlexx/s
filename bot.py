import discord
from discord import app_commands
import os
import random
from keep_alive import keep_alive

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        # Required for reading message content if you ever add prefix commands
        intents.message_content = True 
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

client = MyBot()

@client.tree.command(name="fatheriwishtoflip", description="father i wish to flip")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtoflip(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/boom.gif")

@client.tree.command(name="fatheriwishtouber", description="father i wish to uber")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtouber(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/uber.gif")

@client.tree.command(name="fatheriwishtomeinkampf", description="father i wish to meinkampf")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtomeinkampf(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/meinkampf.webp")

@client.tree.command(name="fatheriwishtogamble", description="get a random number")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtogamble(interaction: discord.Interaction, minimum: int, maximum: int):
    result = random.randint(minimum, maximum)
    await interaction.response.send_message(f"your random number is **{result}**")

@client.tree.command(name="fatheriwishtodecide", description="choose between paths")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtodecide(
    interaction: discord.Interaction, 
    pick1: str, pick2: str, 
    pick3: str = None, pick4: str = None, pick5: str = None
):
    all_picks = [p for p in [pick1, pick2, pick3, pick4, pick5] if p is not None]
    await interaction.response.send_message(f"the heavens have spoken: **{random.choice(all_picks)}**")

# --- PREDICT / 8-BALL COMMAND ---
@client.tree.command(name="fatheriwishtopredict", description="ask the heavens a question")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtopredict(interaction: discord.Interaction, question: str):
    responses = [
        "yes.",
        "no.",
        "maybe.",
        "maybe not.",
        "i don't know."
    ]
    
    answer = random.choice(responses)
    
    # sending everything in lowercase as requested
    await interaction.response.send_message(f"question: {question.lower()}\nthe heavens say: {answer}")

@client.tree.command(name="fatheriwishtodoom", description="father i wish to doom")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtomeinkampf(interaction: discord.Interaction):
    await interaction.response.send_message("send this in chat:\n```https://doom.p2r3.com/i.webp```")

@client.tree.command(name="fatheriwishtosummonkimjongun", description="father i wish to summon kim jong un")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtosummonkimjongun(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/kju.png")

@client.tree.command(name="fatheriwishtodprk", description="father i wish to dprk")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtodprk(interaction: discord.Interaction):
    await interaction.response.send_message("||https://open.spotify.com/playlist/2I0vVElTzPQxfdyhE5Otc3?si=e34d9fd7e33c4bf2||")

@client.tree.command(name="fatheriwishtoleave", description="father i wish to leave")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtoleave(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/leave.gif")

@client.tree.command(name="fatheriwishtothrowit", description="father i wish to throw it")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtothrowit(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/irony.gif")

# Start systems
keep_alive()
client.run(os.environ['DISCORD_TOKEN'])
