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
    quotes = ['OOH BABY A TRIPLE', 'WHAT DO YOU MEAN', 'that is not true', 'UNBELIEVABLE', 'This Ryze couldnt even graduate 8th grade']
    response = random.choice(quotes)
    await ctx.send(response)

@bot.command(name='picture', help='Self explanatory')
async def pic(ctx) :
    pics = ['ucklar_bowtie.jpg', 'ucklar_linkedin.png', 'ucklar_esports.png', 'ucklar_pimp.jpg', 'ucklar_sleep.jpg', 'ucklar_superbowl.png']
    await ctx.send(file=discord.File(random.choice(pics)))

@bot.command(name='praise', help='Praises the lord')
async def praise(ctx) :
    pasta_pool= [
        'Ucklar <:cbaUcklar:700157400744722513> isn\'t so great? Are you kidding me? When was the last time you saw a player with such an ability and movement with his skills? Ucklar <:cbaUcklar:700157400744722513> puts the game on another level, and we will be blessed if we ever see a player with his skill and passion for the game again. Faker breaks records. Lebron breaks records. Ucklar <:cbaUcklar:700157400744722513> breaks the rules. You can keep your statistics. I prefer the magic. And his haircut.',
        'if ucklar <:cbaUcklar:700157400744722513> has million number of fans i am one of them. if ucklar <:cbaUcklar:700157400744722513> has ten fans i am one of them. if ucklar <:cbaUcklar:700157400744722513> has no fans. that means i am no more on the earth. if world against ucklar <:cbaUcklar:700157400744722513> , i am against the world. i love ucklar <:cbaUcklar:700157400744722513> till my last breath... die hard fan of ucklar <:cbaUcklar:700157400744722513> . Hit like if u think ucklar <:cbaUcklar:700157400744722513> best & smart in the world'
    ]
    response = random.choice(pasta_pool)
    await ctx.send(response)

@bot.command(name='cbaUcklar', help='<cbaUcklar> times whatever amount you want. Max = 50')
async def cbaUcklar(ctx, amt: int) :
    temp = ['<:cbaUcklar:700157400744722513>' for _ in range(amt)]
    response = ''.join(temp)
    await ctx.send(response)

# @bot.event
# async def on_message(message):
#     f = open('chatlog.txt', 'a+')
#     f.write('{}\n'.format(message.content))
#     f.close()


bot.run(TOKEN)
