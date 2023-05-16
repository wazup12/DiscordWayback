# This example requires the 'message_content' intent.
import discord, json, asyncio, subprocess
from wayback import output
from discord.ext import commands
from discord.utils import get

#-----CONSTANTS-----#
API_PATH = ".secret/wayback.json"
PREFIX = '!'
SLEEP_DURATION = 5e-1
VERSION = ("1.0.0", "Pre-Alpha Build")
NAME = "Wayback"
DEFAULT = "everyone"

#----DEFINITIONS----#
def get_keys(path):
	with open(path) as f:
		return json.load(f)

def to_upper(arg):
	return arg.upper()

def poke_limiter(arg):
	return min(int(arg), 5)

def get_role(guild, role):
    if not guild: return 0
    return get(guild.roles, name=role)


#--TOKEN RETRIEVAL--#
token = get_keys(API_PATH)['API_Key']

#----BOT STARTUP----#
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

#-----COMMANDS------#
@bot.command()
async def echo(ctx: commands.Context, *msg):
	await ctx.send(' '.join(msg))

@bot.command()
async def scream(ctx, *, content: to_upper):
	await ctx.send(content)

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong <:test:1107804011572240404>")

@bot.command()
async def poke(ctx: commands.Context, member: discord.Member, n: poke_limiter):
	for i in range(n):
		await ctx.send(member.mention)
		await asyncio.sleep(SLEEP_DURATION)

@poke.error
async def poke_error(ctx: commands.Context, error):
	await ctx.send(error)

@bot.command()
async def version(ctx):
    await ctx.send(f"Running {NAME} on {VERSION[0]} ({VERSION[1]})")

@bot.command()
async def alert(ctx: commands.Context, *, content):
    role = ctx.guild.default_role
    await ctx.send(f"{role.name}: {content}")

@alert.error
async def poke_error(ctx: commands.Context, error):
	await ctx.send(error)

@bot.command()
async def check(ctx: commands.Context, link):
	results = output(link)
	await ctx.send(results[0])
	await ctx.send(results[1])

@bot.command()
async def cowsay(ctx: commands.Context, *, content):
    message = subprocess.check_output(f"cowsay {content}", shell=True)
    await ctx.send(f"```{message.decode()}```")

@bot.command()
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    await ctx.send("Good night :sleeping:")
    await bot.close()

#------RUNNING------#
bot.run(token)
