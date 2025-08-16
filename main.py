import os
import discord
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.environ.get("DISCORD_TOKEN")

class CoachingBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Comandos / sincronizados")

    async def on_ready(self):
        print(f"🤖 Bot conectado como {self.user}")

bot = CoachingBot()

@bot.tree.command(name="coaching", description="Accede al sistema de Coaching de BlockCraft Hosting")
async def coaching(interaction: discord.Interaction):
    await interaction.response.send_message("📘 Bienvenido al sistema de Coaching de **BlockCraft Hosting** 🚀")

keep_alive()
bot.run(TOKEN)
