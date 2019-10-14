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

@client.event
async def on_message(message):
  if message.content == '!bye':
    await client.close()

  res = diceroll.Dice.roll_with_pattern(message.content)
  if(res):
    await client.send_message(
      message.channel,
      str(res)
    )

client.run(os.environ['DISCRD_TOKEN'])