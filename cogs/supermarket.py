import discord
from discord.ext import commands
from discord import app_commands
import random
import os

class supermarket(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        print("Loading supermarket.py...")

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading supermarket.py...")


    @app_commands.command(name="st_pricing", description="Helps you to set prices for Supermarket Together")
    async def st_pricing(self, interaction: discord.Interaction, price: float = 0.00):
        temp_int = price * 2.00 - 0.10
        await interaction.response.send_message(f"Set price to {temp_int}")

    @app_commands.command(name="st_pricing_cents", description="Helps you to set prices for Supermarket Together but uses only cents. 100 = 1$")
    async def st_pricing_cents(self, interaction: discord.Interaction, price: int = 0):
        temp_int = price * 2 - 10
        temp_float = temp_int / 100
        await interaction.response.send_message(f"Set price to {temp_float}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(supermarket(bot))