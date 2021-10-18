import os
import discord
import requests
import json
import random
from replit import db


trigger_words=['ringo','hey,ringo','hey ringo','Ringo','Hey,Ringo','Hey Ringo','Hey,ringo','Hey ringo','Hi,ringo','hi,ringo','Hi,Ringo','hi,Ringo','bot','聆歌']

trigger_reactions=['yo','what up','你好！']



#def update_entries():



def get_quote():
  response=requests.get('https://zenquotes.io/api/random')
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+' -'+json_data[0]['a']
  return (quote)

client=discord.Client()
@client.event
async def on_ready():
  print('hello{0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author==client.user:
    return
  msg=message.content
  if message.content.startswith('$inspire'):
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in trigger_words):
    await message.channel.send(random.choice(trigger_reactions))

client.run('ODk5NTM3OTQ1OTM2MTYyODI3.YW0N_g.SFApUnXDLezIj98EojIURXHcS0Y')