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

@client.tree.command(name="fatheriwishtogoon", description="Search the realm")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def search(interaction: discord.Interaction, tags: str):
    await interaction.response.defer()
    
    # Randomize page and clean tags
    random_page = random.randint(0, 50)
    tags_string = tags.replace(" ", "_")
    final_url = f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags={tags_string}&pid={random_page}&json=1"
    
    # URL SCRUBBER
    final_url = final_url.replace("api.rule34", "rule34").replace("xxx//", "xxx/")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    max_retries = 3  # How many times to try different proxies
    for attempt in range(max_retries):
        chosen_proxy = random.choice(proxy_list)
        proxies = {"http": chosen_proxy, "https": chosen_proxy}
        
        try:
            # Short timeout so we don't wait too long for a bad proxy
            response = requests.get(final_url, headers=headers, proxies=proxies, timeout=10)
            
            # If successful (200) and we got data
            if response.status_code == 200:
                data = response.json()
                if data:
                    post = random.choice(data)
                    await interaction.followup.send(post['file_url'])
                    return  # EXIT the function immediately on success!
                else:
                    # If data is empty, the tags might just have no results
                    await interaction.followup.send("The heavens are empty for those tags.")
                    return

            # If we get a 403 or 429, the loop continues and tries a NEW proxy
            print(f"Attempt {attempt+1} failed with status {response.status_code}. Retrying...")
            
        except Exception as e:
            print(f"Attempt {attempt+1} error: {e}")
            # If it's the last attempt, tell the user
            if attempt == max_retries - 1:
                await interaction.followup.send("The realm is currently shielded. Try again in a minute.")

# --- NEW MERGED COMMANDS ---

@client.tree.command(name="fatheriwishtoflip", description="father i wish to flip")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fatheriwishtoflip(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/boom.gif")

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

# Start systems
keep_alive()
client.run(os.environ['DISCORD_TOKEN'])
