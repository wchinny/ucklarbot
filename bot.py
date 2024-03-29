import json
import os
import random
import discord
from discord.ext import commands

from dotenv import load_dotenv


def chunk_list(full_list):
    for i in range(0, len(full_list), 50):
        yield full_list[i : i + 50]


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

with open("responses.json", "r") as f:
    responses = json.load(f)

bot = commands.Bot(command_prefix="ucklarbot ", help="basically ucklar")


@bot.command(name="cbaUcklar", help=responses["cbaUcklar"]["help"])
async def cbaUcklar(ctx, amt: int):
    temp = [responses["cbaUcklar"]["message"] for _ in range(amt)]
    for chunk in chunk_list(temp):
        response = "".join(chunk)
        await ctx.send(response)


@bot.command(name="pasta", help=responses["pasta"]["help"])
async def pasta(ctx):
    response = responses["pasta"]["message"]
    await ctx.send(response)


@bot.command(name="picture", help=responses["picture"]["help"])
async def pic(ctx, name=None):
    if name:
        name_png = "ucklar_" + name + ".png"
        name_jpg = "ucklar_" + name + ".jpg"
        if name_png in responses["picture"]["message"]:
            await ctx.send(file=discord.File(name_png))
        elif name_jpg in responses["picture"]["message"]:
            await ctx.send(file=discord.File(name_jpg))
        else:
            await ctx.send("Hmm. I couldn't find that Ucklar.")
    else:
        pics = responses["picture"]["message"]
        await ctx.send(file=discord.File(random.choice(pics)))


@bot.command(name="praise", help=responses["praise"]["help"])
async def praise(ctx):
    pasta_pool = responses["praise"]["message"]
    response = random.choice(pasta_pool)
    await ctx.send(response)


@bot.command(name="quote", help=responses["quote"]["help"])
async def quote(ctx):
    quotes = responses["quote"]["message"]
    response = random.choice(quotes)
    await ctx.send(response)


bot.run(TOKEN)
