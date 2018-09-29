import discord
from discord.ext import commands
from random import randint

prefix = '&' # command prefix
prop_file = 'data.txt' # data file
propaganda_list = [] # list for data

bot = commands.Bot(command_prefix=prefix) # bot init

def read_file():
    f = open(prop_file, 'r') # open file 
    for data in f:
        propaganda_list.append(data) # read each line and add to the list
    f.close() # close file

@bot.command()
async def propaganda():
    """Spouts Propagan-- Facts about Communism"""
    await bot.say(propaganda_list[randint(0,len(propaganda_list) - 1)]) # displays random item
    
try:
    read_file() # loads the data
    token_file = open('secret.bot', 'r') # opens and reads secret
    token = token_file.readline()
    token_file.close()
    token = token.replace('\n','')
    bot.run(token) # runs bot
except Exception as error:
    print('Something went wrong ¯\_(ツ)_/¯')
    print(error)
    print(error.args)
finally:
    print('End of Bot.')