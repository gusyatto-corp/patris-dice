import discord
import re
import random
import os
import urllib.request
import json

import diceroll
import diceparse

client = discord.Client()

pattern = re.compile(r'((\d)[dD](\d+))(.*)')

parser_pattern = re.compile(r'^\(?\d+[dD][\ddD\(\)\+\-\*]*\d+\)?(.*)')

def getLiveDataList():
  url = 'http://holodule-now-server.herokuapp.com/api/schedule/now'
  res = urllib.request.urlopen(url=url).read()
  live_datas = json.loads(res.decode('utf-8'))
  return live_datas


@client.event
async def on_ready():
  print('Logged in.')

@client.event
async def on_message(message):
  if message.content == '!bye':
    await client.close()

  if message.content == 'ホロライブの配信見たいな':
    await client.send_message(message.channel, (message.author.mention)+'\nなんだと？')
    datas = getLiveDataList()
    if len(datas)==0:
      await client.send_message(message.channel, 'しかし残念だが、今は誰も配信していないようだ...')
      return
    
    await client.send_message(message.channel, 'ならばこちらの配信はいかがだろうか')
    for d in datas:
      await client.send_message(message.channel, d['streaming']['url'])
    await client.send_message(message.channel, 'スパチャの準備はできたか？')
    return 

  dice_parser_reg = parser_pattern.search(message.content)
  if dice_parser_reg:
    msg = message.author.mention + "\n"
    msg += str(diceparse.DiceParser(dice_parser_reg.group(0)).evaluate())
    
    if dice_parser_reg.group(1).find("シークレット")!=-1:
      await client.send_message(message.author, msg)
      return
    
    await client.send_message(message.channel, msg)
    return

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