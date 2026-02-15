import discord
import os
from discord import app_commands
from keep_alive import keep_alive
import random
import requests
import xml.etree.ElementTree as ET

# --- Bot Initialization ---
class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

bot = MyBot()

U_INSTALL = app_commands.allowed_installs(guilds=True, users=True)
U_CONTEXT = app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)

# --- Utility Commands ---

@bot.tree.command(name="fatheriwishtoflip", description="father i wish to flip")
@U_INSTALL
@U_CONTEXT
async def fatheriwishtoflip(interaction: discord.Interaction):
    await interaction.response.send_message("https://raw.githubusercontent.com/shlexx/gif/refs/heads/main/boom.gif")

@bot.tree.command(name="fatheriwishtogamble", description="get a random number")
@U_INSTALL
@U_CONTEXT
async def fatheriwishtogamble(interaction: discord.Interaction, minimum: int, maximum: int):
    result = random.randint(minimum, maximum)
    await interaction.response.send_message(f"your random number is **{result}**")

@bot.tree.command(name="fatheriwishtodecide", description="choose between paths")
@U_INSTALL
@U_CONTEXT
async def fatheriwishtodecide(
    interaction: discord.Interaction, 
    pick1: str, pick2: str, 
    pick3: str | None = None, pick4: str | None = None, pick5: str | None = None
):
    all_picks = [p for p in [pick1, pick2, pick3, pick4, pick5] if p is not None]
    await interaction.response.send_message(f"the heavens have spoken: **{random.choice(all_picks)}**")

# --- The Search Command (With Forced Slash Removal) ---

@bot.tree.command(name="fatheriwishtogoon", description="Father, show me the forbidden art")
@U_INSTALL
@U_CONTEXT
@app_commands.choices(media_type=[
    app_commands.Choice(name="Any", value="any"),
    app_commands.Choice(name="Image/GIF Only", value="image"),
    app_commands.Choice(name="Video Only", value="video")
])
async def fatheriwishtogoon(
    interaction: discord.Interaction, 
    tag1: str, 
    private: bool = True, 
    media_type: str = "any",
    tag2: str | None = None, 
    blacklist: str | None = None
):
    await interaction.response.defer(ephemeral=private)

    # 1. Format Tags
    search_tags = [tag1.strip().lower().replace(" ", "_")]
    if tag2:
        search_tags.append(tag2.strip().lower().replace(" ", "_"))
    if media_type == "video":
        search_tags.append("-image")
    elif media_type == "image":
        search_tags.append("-video")
    if blacklist:
        search_tags.extend([f"-{b.strip()}" for b in blacklist.split(",")])

    tags_string = "+".join(search_tags)

    # 2. MANUALLY BUILD CLEAN URL
    # We use rule34.xxx directly and force-delete any double slashes
    url_base = "https://rule34.xxx"
    url_path = "/index.php?page=dapi&s=post&q=index&limit=100&tags="
    final_url = f"{url_base}{url_path}{tags_string}"

    # Scrubbing logic to prevent the 'None' result crash
    final_url = final_url.replace("xxx//", "xxx/")
    final_url = final_url.replace("api.rule34", "rule34")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(final_url, headers=headers, timeout=10)
        print(f"DEBUG FINAL URL: {response.url}")

        root = ET.fromstring(response.text)
        posts = root.findall('post')

        if posts:
            # Filter valid links to avoid 'None' errors
            valid_links = [p.get('file_url') for p in posts if p.get('file_url')]

            if not valid_links:
                await interaction.followup.send("Links found, but they are empty.", ephemeral=private)
                return

            chosen_url = random.choice(valid_links)
            is_v = any(chosen_url.lower().endswith(ex) for ex in ['.mp4', '.webm', '.mov'])
            icon = "🎥" if is_v else "🖼️"

            await interaction.followup.send(f"{icon} Results for: **{tag1}**\n{chosen_url}", ephemeral=private)
        else:
            await interaction.followup.send(f"The heavens found nothing for: `{tag1}`.", ephemeral=private)

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        try:
            await interaction.followup.send("The realm is unreachable.", ephemeral=private)
        except:
            pass

# --- Start ---
keep_alive()
bot.run(os.environ['DISCORD_TOKEN'])
