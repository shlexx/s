import discord
from discord import app_commands
import os
import random
import string
import secrets
import yt_dlp
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

@client.tree.command(name="fatheriwishtoapolocheese", description="father i wish to apolocheese")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtoapolocheese(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/cheese.gif")

@client.tree.command(name="fatheriwishtovanish", description="father i wish to vanish")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtovanish(interaction: discord.Interaction):
    await interaction.response.send_message("_ _")

@client.tree.command(name="fatheriwishtomessage", description="father i wish to message")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtomessage(interaction: discord.Interaction, message: str, private: bool = False):
    await interaction.response.send_message(message, ephemeral=private)

@client.tree.command(name="fatheriwishtoreceivekeys", description="father i wish to receive keys")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtoreceivekeys(
    interaction: discord.Interaction, 
    amount: int = 1, 
    uppercase: bool = True,
    lowercase: bool = True,
    numbers: bool = True, 
    symbols: bool = False,
    format_as_license: bool = False,
    block_size: int = 4,
    dash_count: int = 2
):
    amount = max(1, min(amount, 10))
    pool = ""
    if uppercase: pool += string.ascii_uppercase
    if lowercase: pool += string.ascii_lowercase
    if numbers: pool += string.digits
    if symbols: pool += "!@#$%^&*"
    if not pool: pool = string.ascii_uppercase
    keys = []
    for _ in range(amount):
        if format_as_license:
            res = "-".join(''.join(secrets.choice(pool) for _ in range(block_size)) for _ in range(dash_count + 1))
        else:
            res = ''.join(secrets.choice(pool) for _ in range(16))
        keys.append(res)
    await interaction.response.send_message(f"```\n{chr(10).join(keys)}\n```", ephemeral=True)

@client.tree.command(name="inshallahiwishtobomb", description="inshallah i wish to bomb")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def inshallahiwishtobomb(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/hover.gif")

@client.tree.command(name="fatheriwishtoplmir", description="father i wish to plant labubu marijuana in romania")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtoplmir(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/labubu.gif")

@client.tree.command(name="fatheriwishtogatuc", description="father i wish to get a tiktok user's country")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtogatuc(interaction: discord.Interaction, url: str):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        region = info.get('region') or info.get('location') or "unknown"
        await interaction.response.send_message(f"the users country/region is: **{region}** (could be incorrect)")

@client.tree.command(name="fatheriwishtorap", description="father i wish to rap")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtorap(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/rap.gif")

keep_alive()
client.run(os.environ['DISCORD_TOKEN'])
