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

class economy(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        print("Loading economy.py...")

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading economy.py...")

    @app_commands.command(name="balance", description="See the hug balance")
    async def balance(self, interaction: discord.Interaction):
        file = open(f"./bank/{interaction.user.id}.txt", "r")
        temp_int = int(file.read())
        file.close()
        await interaction.response.send_message(f"You have {temp_int} hugs!")
    
    @app_commands.command(name="payday", description="See the hug balance")
    async def balance(self, interaction: discord.Interaction):
        file = open(f"./bank/{interaction.user.id}.txt", "r")
        temp_int = int(file.read())
        file.close()
        await interaction.response.send_message(f"You have {temp_int} hugs!")

    @app_commands.command(name="slots", description="Get more hugs from gambling!")
    async def slots(self, interaction: discord.Interaction):
        emoteArray = []

        for i in range(3):
            temp_val = random.randint(1,4)

            if(temp_val == 1):
                temp_emote = ":grapes:"
            elif(temp_val == 2):
                temp_emote = ":cherries:"
            elif (temp_val == 3):
                temp_emote = ":strawberry:"
            else:
                temp_emote = ":watermelon:"
            
            emoteArray.append(temp_emote)
            
        emote1 = str(emoteArray[0])
        emote2 = str(emoteArray[1])
        emote3 = str(emoteArray[2])

        if (emote1 == ":grapes:" and emote2 == ":grapes:" and emote3 == ":grapes:"):
            writeHugs(interaction.user.id, 500)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 500 hugs!")

        elif (emote1 == ":cherries:" and emote2 == ":cherries:" and emote3 == ":cherries:"):
            writeHugs(interaction.user.id, 1000)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 1000 hugs!")

        elif (emote1 == ":strawberry:" and emote2 == ":strawberry:" and emote3 == ":strawberry:"):
            writeHugs(interaction.user.id, 1250)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 1250 hugs!")

        elif (emote1 == ":watermelon:" and emote2 == ":watermelon:" and emote3 == ":watermelon:"):
            writeHugs(interaction.user.id, 100000)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 100,000 hugs! JACKPOT!")
        else:
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n Better luck next time!")

    @app_commands.command(name="all_in", description="Double or nothing!")
    async def all_in(self, interaction: discord.Interaction):
        temp_val = random.randint(1,100)
        if temp_val == 1:
            file = open(f"./bank/{interaction.user.id}.txt", "r")
            temp_int = int(file.read())
            file = open(f"./bank/{interaction.user.id}.txt", "w")
            file.write(str(temp_int * 2))
            file.close()
            await interaction.response.send_message("You've doubled your Hugs!!! Really lucky!")
        else:
            file = open(f"./bank/{interaction.user.id}.txt", "r")
            temp_int = int(file.read())
            file = open(f"./bank/{interaction.user.id}.txt", "w")
            file.write("0")
            file.close()
            await interaction.response.send_message("You've lost all hugs. T-T")

    @app_commands.command(name="hug", description="Give a hug to someone on the server")
    async def hug(self, interaction: discord.Interaction, hugged_user: discord.Member = None):
        file = open(f"./bank/{interaction.user.id}.txt", "r")
        temp_int = int(file.read())
        file = open(f"./bank/{interaction.user.id}.txt", "w")
        file.write(str(temp_int - 1))
        file.close()
        try:
            writeHugs(hugged_user.id, 1)
        except:
            await interaction.response.send_message("The hugged user does not have a HugBank Account! :(")

        await interaction.response.send_message(f"{interaction.user.mention} hugged <@{hugged_user.id}>!"
                                                "\n"
                                                "https://imgur.com/gallery/V6HmXVi")
        
    @app_commands.command(name="hug_register", description="Register at the HugBank")
    async def hug_register(self, interaction: discord.Interaction):
        if os.path.isfile(f"./bank/{interaction.user.id}.txt"):
            await interaction.response.send_message("You are already registered with HugBank")
        else:
            file = open(f"./bank/{interaction.user.id}.txt", "a")
            file.write(str(100))
            file.close()
            await interaction.response.send_message("HugBank account opened with 100 hugs!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(economy(bot))