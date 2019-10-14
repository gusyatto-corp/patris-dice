import discord
import re
import random
import os

import diceroll

client = discord.Client()

pattern = re.compile(r'(\d)[dD](\d+)(.*)')
opt_pattern_with_comment = re.compile(r'^:(.+)')
opt_pattern_with_judge = re.compile(r'^(<|>|<=|>=)(\d+)')

@client.event
async def on_ready():
  print('Logged in.')

def dice_roll(m, n):
  return sum(map(lambda x: x+random.randrange(1,n+1), [0]*m))

@client.event
async def on_message(message):
  if message.content == '!bye':
    await client.close()

  if (re.compile(r'[dD]66').search(message.content)):
    r1 = dice_roll(1,6)
    r2 = dice_roll(1,6)
    msg = str(r1)+str(r2) if r1<=r2 else str(r2)+str(r1)
    msg = message.author.mention + " " + msg
    await client.send_message(message.channel, msg)
    return

  # reg = pattern.search(message.content)
  # if reg:
  #   num1 = int( reg.group(1) )
  #   num2 = int( reg.group(2) )
  #   str1 = str( reg.group(3) )
  #   res = dice_roll(num1, num2)

  #   msg = message.author.mention + " " + str(res)
  #   if str1.find("シークレット")==-1:
  #     await client.send_message(message.channel, msg)
  #   else:
  #     await client.send_message(message.author, msg)

  res = diceroll.Dice.roll_with_pattern(message.content)
  if(res):
    await client.send_message(
      message.channel,
      str(res)
    )

client.run(os.environ['DISCRD_TOKEN'])