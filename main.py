import discord
import os # default module
from dotenv import load_dotenv
import game_db
import pregame

load_dotenv() # load all the variables from the env file
bot = discord.Bot()
game_db.init() # Initialize global games db

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    # Display whose running a given test instance for disambiguation purposes.
    # Leave $INSTANCE unset on prod
    instance = os.getenv('INSTANCE')
    if instance is not None:
        await bot.change_presence(activity=discord.CustomActivity(f"Running on {instance}"))

@bot.slash_command(name="tres", description="Create a game of Tres")
@discord.option("name", str, required=False)
async def tres(ctx: discord.ApplicationContext, name: str | None):
    if not isinstance(ctx.channel, discord.TextChannel):
        await ctx.respond("This command can only be used in text channels.", ephemeral=True)
        return # TODO: this probably invalidates some types of channels that we could reasonably play games in. might need to broaden this
    g = pregame.PreGame(ctx.user, ctx.channel, name)
    await ctx.respond("", embed=g.info_embed(), view=g) # Send a message with our View class that contains the button


bot.run(os.getenv('TOKEN')) # run the bot with the token
