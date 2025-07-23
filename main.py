import discord
import os # default module
from dotenv import load_dotenv
import pregame

load_dotenv() # load all the variables from the env file
bot = discord.Bot()
games = {}

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="tres", description="Create a game of Tres") # Create a slash command
async def tres(ctx):
    g = pregame.PreGame()
    games[g.uuid] = g
    await ctx.respond("**Game created!**", view=g.view) # Send a message with our View class that contains the button


bot.run(os.getenv('TOKEN')) # run the bot with the token
