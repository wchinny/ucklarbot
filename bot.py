# bot.py
import os
import random
import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='ucklarbot ', help='basically ucklar')

@bot.command(name='pasta', help='Prints out the infamous Ucklar pasta')
async def pasta(ctx) :
    response = 'Hello Hello, I\'m Ucklar~. I found this community on the league forums and it seems fairly interesting. I\'m bronze 1 ;__;, and want more people to play with! I\'m 15, although I\'m mature for my age and you\'ll never even know I\'m that young. I plan to go to college for editing or anything dealing with film except the acting x_x. I\'m looking forward to being apart of this community! Also, I\'d like to become a full member. My IGN is Ucklar, and that is also my name on teamspeak~'
    await ctx.send(response)

@bot.command(name='quote', help='Prints out an Ucklar quote, might be in all caps')
async def quote(ctx) :
    quotes = ['OOH BABY A TRIPLE', 'WHAT DO YOU MEAN', 'that is not true', 'UNBELIEVABLE']
    response = random.choice(quotes)
    await ctx.send(response)

@bot.command(name='picture', help='Self explanatory')
async def pic(ctx) :
    pics = ['ucklar_bowtie.jpg', 'ucklar_linkedin.png', 'ucklar_esports.png', 'ucklar_pimp.jpg', 'ucklar_sleep.jpg']
    await ctx.send(file=discord.File(random.choice(pics)))

@bot.command(name='cbaUcklar', help='<cbaUcklar numAmount>, prints out cbaUcklar however many times you want')
async def cbaUcklar(ctx, amt: int) :
    temp = [':eyes: ' for _ in range(amt)]
    await ctx.send(''.join(temp))

bot.run(TOKEN)