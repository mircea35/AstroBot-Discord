import discord
from discord.ext import commands
from discord import app_commands
import random
import os

def writeHugs(user_id, hugs = int):
    file = open(f"./bank/{user_id}.txt", "r")
    temp_int = int(file.read())
    file = open(f"./bank/{user_id}.txt", "w")
    file.write(str(temp_int + hugs))
    file.close()

class supermarket(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        print("Loading supermarket.py...")

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading supermarket.py...")


    @app_commands.command(name="st_pricing", description="Helps you to set prices for Supermarket Together")
    async def balance(self, interaction: discord.Interaction, price: float = 0.00):
        temp_int = price * 2 - 0.10
        await interaction.response.send_message(f"Set price to {temp_int}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(supermarket(bot))