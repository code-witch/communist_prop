import discord
from discord.ext import commands
from random import randint

prefix = '&'
prop_file = 'data.bot'
propaganda_list = []

bot = commands.Bot(command_prefix=prefix)

def read_file():
    f = open(prop_file, 'r')
    for data in f:
        propaganda_list.append(data)
    f.close()

@bot.command()
async def propaganda():
    """Spouts Propagan-- Facts about Communism"""
    print(propaganda_list[randint(0,len(propaganda_list) - 1)])
    await bot.say(propaganda_list[randint(0,len(propaganda_list) - 1)])


try:
    read_file()
    token_file = open('secret.bot', 'r')
    token = token_file.readline()
    token_file.close()
    token = token.replace('\n','')
    bot.run(token)
except Exception as error:
    print('Something went wrong ¯\_(ツ)_/¯')
    print(error)
    print(error.args)
finally:
    print('End of Bot.')