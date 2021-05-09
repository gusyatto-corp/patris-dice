import discord
import re
import random
import os
import urllib.request
import json
import time,asyncio
import threading

import diceroll
import diceparse

client = discord.Client()

pattern = re.compile(r'((\d)[dD](\d+))(.*)')

parser_pattern = re.compile(r'^\(?\d+[dD][\ddD\(\)\+\-\*]*\d+\)?(.*)')

reaction_pattern = ['それな', 'わかる', '本当か？', 'おちつけよ', 'キウイ食うか？', '確かに', '爆弾発言だな(笑)']

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

  if message.author.bot:
    return 

  if random.randrange(0,100)<1:
    await message.channel.send( message.author.mention + " " + random.choice(reaction_pattern))

  if message.content == 'ホロライブの配信見たいな':
    await message.channel.send( (message.author.mention)+'\nなんだと？')
    datas = getLiveDataList()
    if len(datas)==0:
      await message.channel.send( 'しかし残念だが、今は誰も配信していないようだ...')
      return
    
    await message.channel.send( 'ならばこちらの配信はいかがだろうか')
    for d in datas:
      await message.channel.send( d['streaming']['url'])
    await message.channel.send( 'スパチャの準備はできたか？')
    return 

  dice_parser_reg = parser_pattern.search(message.content)
  if dice_parser_reg:
    msg = message.author.mention + "\n"
    msg += str(diceparse.DiceParser(dice_parser_reg.group(0)).evaluate())
    
    if dice_parser_reg.group(1).find("シークレット")!=-1:
      await message.author.send(msg)
      return
    
    await message.channel.send( msg)
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
      await message.author.send(send_msg)
    else:
      await message.channel.send(send_msg)

    print(send_msg)

    await client.send_message(send_for, send_msg)
    return 
    
  if random.randrange(0,100)<1:
    await client.send_message(message.channel, message.author.mention + " " + random.choice(reaction_pattern))


def holodule_job():
  print(getLiveDataList())
  t=threading.Timer(300,holodule_job)
  t.start()

t=threading.Thread(target=holodule_job)
t.start()

client.run(os.environ['DISCRD_TOKEN'])

