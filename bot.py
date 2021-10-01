import disnake
from disnake.ext import commands
import config
import commands_config
import os

discord = disnake
ccfg = commands_config
cfg = config

client = commands.Bot(command_prefix = cfg.BOT_PREFIX, test_guilds=[cfg.server_id])

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'you forgot this one very important part!!! do `{cfg.BOT_PREFIX}help` for more detail')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission to execute this command")

@client.event
async def on_ready():
    print(client.user.name, 'is online')

# Test command
@client.command()
async def test(ctx):
    await ctx.send('Test success')

@client.slash_command()
async def ping(ctx):
    ping = int(round(client.latency, 3) * 1000)
    embed = discord.Embed(title = "Bot's Ping", description = (f"{ctx.author.display_name} the bot's ping is {ping}ms"))
    await ctx.send(embed = embed)

ping = None

# Ping command
@client.command()
async def ping(ctx):
    ping = int(round(client.latency, 3) * 1000)
    await ctx.send(f'{ctx.author.mention} {ping} ms.')

# Embed command
@client.command()
async def embed(ctx):
    e = discord.Embed(title = ccfg.Example_Embed_Title, description = ccfg.Example_Embed_Title, color = 0x5865f2) # blurple hex code
    e.add_field(name = ccfg.Embed_Name_1, value = (ccfg.Embed_Text_1))
    e.add_field(name = ccfg.Embed_Name_2, value = (ccfg.Embed_Text_2))
    await ctx.send(e = embed)

@client.command()
@commands.has_any_role("") # enter roles that can use command in that and devide them with a comma Don't close the quotes
async def special(ctx):
  await ctx.send('ok a guy with special role!')

# Makes the bot run
client.run(os.environ['token'])
