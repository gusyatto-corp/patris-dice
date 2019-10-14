import discord
import re
import random
import os

import diceroll

client = discord.Client()

pattern = re.compile(r'((\d)[dD](\d+))(.*)')

@client.event
async def on_ready():
  print('Logged in.')

@client.event
async def on_message(message):
  if message.content == '!bye':
    await client.close()

  message_reg = pattern.search(message.content)
  if(message_reg):
    res = diceroll.Dice.roll_with_pattern(message_reg.group(1))

    send_msg = message.author.mention + "\n"
    if(message_reg.group(4)!=""):
      send_msg += "Dice rolled for \"*" + message_reg.group(4).strip() + "*\"\n"
    send_msg += "res: " + str(res) + "-> __**" + str(sum(res)) + "**__\n"

    print(send_msg)

    send_for = message.channel
    if(message_reg.group(4).find("シークレット") != -1):
      send_msg.replace("シークレット", "")
      send_for = message.author

    print(send_msg)

    await client.send_message(send_for, send_msg)


client.run(os.environ['DISCRD_TOKEN'])