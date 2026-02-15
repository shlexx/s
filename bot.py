import discord
from discord import app_commands
import requests
import random
import os
import xml.etree.ElementTree as ET
from keep_alive import keep_alive

# --- YOUR PROXY LIST ---
# Keep your Webshare credentials here
proxy_list = [
    "http://hkspqckn:s8m6txvkrgxy@31.59.20.176:6754",
    "http://hkspqckn:s8m6txvkrgxy@23.95.150.145:6114",
    "http://hkspqckn:s8m6txvkrgxy@198.23.239.134:6540",
	"http://hkspqckn:s8m6txvkrgxy@45.38.107.97:6014",
	"http://hkspqckn:s8m6txvkrgxy@107.172.163.27:6543",
	"http://hkspqckn:s8m6txvkrgxy@198.105.121.200:6462",
	"http://hkspqckn:s8m6txvkrgxy@64.137.96.74:6641",
	"http://hkspqckn:s8m6txvkrgxy@216.10.27.159:6837",
	"http://hkspqckn:s8m6txvkrgxy@23.26.71.145:5628",
	"http://hkspqckn:s8m6txvkrgxy@23.229.19.94:8689",
]

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

# --- RULE34 SEARCH COMMAND ---
@client.tree.command(name="fatheriwishtogoon", description="Search the realm")
async def search(interaction: discord.Interaction, tags: str):
    await interaction.response.defer()
    
    tags_string = tags.replace(" ", "_")
    final_url = f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags={tags_string}"
    
    # URL SCRUBBER
    final_url = final_url.replace("xxx//", "xxx/").replace("api.rule34", "rule34")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    chosen_proxy = random.choice(proxy_list)
    proxies = {"http": chosen_proxy, "https": chosen_proxy}

    try:
        response = requests.get(final_url, headers=headers, proxies=proxies, timeout=15)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            posts = root.findall('post')
            if not posts:
                await interaction.followup.send("The realm is empty for these tags.")
                return
            post = random.choice(posts)
            await interaction.followup.send(post.get('file_url'))
        else:
            await interaction.followup.send(f"The realm is unreachable (Status: {response.status_code}).")
    except Exception as e:
        await interaction.followup.send("A connection error occurred. Try again!")

# --- NEW MERGED COMMANDS ---

@client.tree.command(name="fatheriwishtoflip", description="father i wish to flip")
async def fatheriwishtoflip(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/boom.gif")

@client.tree.command(name="fatheriwishtogamble", description="get a random number")
async def fatheriwishtogamble(interaction: discord.Interaction, minimum: int, maximum: int):
    result = random.randint(minimum, maximum)
    await interaction.response.send_message(f"your random number is **{result}**")

@client.tree.command(name="fatheriwishtodecide", description="choose between paths")
async def fatheriwishtodecide(
    interaction: discord.Interaction, 
    pick1: str, pick2: str, 
    pick3: str = None, pick4: str = None, pick5: str = None
):
    all_picks = [p for p in [pick1, pick2, pick3, pick4, pick5] if p is not None]
    await interaction.response.send_message(f"the heavens have spoken: **{random.choice(all_picks)}**")

# Start systems
keep_alive()
client.run(os.environ['DISCORD_TOKEN'])
