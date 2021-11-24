import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import logging

client = discord.Client()

sad_words = ["sad", "Sad", "depressed", "Depressed", "unhappy", "Unhappy", "angry", "Angry", "miserable", "Miserable", "misery", "Misery"]

#Encouragements listed below will be outputed by the bot when any user uses command: "$Encouragement"
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
  "You can do it!"
  "We Believe in you!"
  "Don't give up!"
  "Keep trying!" 
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user} Please wait while we boot up!".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

#Anything stated below but also before "msg = message.content" is what the Bot will output when any user says said words on the server.

  if msg.startswith('yay'):
      await message.reply('Awesome!')
        
  if msg.startswith('yay!'):
      await message.reply('Awesome!')

  if msg.startswith('Yay'):
      await message.reply('Awesome!')

  if msg.startswith('Yay!'):
      await message.reply('Awesome!')
    
  if msg.startswith('cool!'):
      await message.reply('You are ineed!')
    
  if msg.startswith('Cool!'):
      await message.reply('You are ineed!')

  if msg.startswith('I need help from Wolf!'):
      await message.reply('<@352658813028925450> Please help!')

  if msg.startswith('I need help from France!'):
      await message.reply('<@707681681074814977> Please help!')

  if msg.startswith('I need help from Dread!'):
      await message.reply('<@911664002197749893> Please help!')

  if msg.startswith('I need help from wolf!'):
      await message.reply('<@352658813028925450> Please help!')

  if msg.startswith('I need help from france!'):
      await message.reply('<@707681681074814977> Please help!')

  if msg.startswith('I need help from dread!'):
      await message.reply('<@911664002197749893> Please help!')
  
  if msg.startswith('I need help from Wolf'):
      await message.reply('<@352658813028925450> Please help!')

  if msg.startswith('I need help from France'):
      await message.reply('<@707681681074814977> Please help!')

  if msg.startswith('I need help from Dread'):
      await message.reply('<@911664002197749893> Please help!')
  
  if msg.startswith('I need help from wolf'):
      await message.reply('<@352658813028925450> Please help!')

  if msg.startswith('I need help from france'):
      await message.reply('<@707681681074814977> Please help!')

  if msg.startswith('I need help from dread'):
      await message.reply('<@911664002197749893> Please help!')

  if msg.startswith('Neato!'):
      await message.replyd('Right!')  
            
  if msg.startswith('What\'s my name?'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))
            
  if msg.startswith('What\'s my role?'):
      await message.reply(' Your current role is: <@&${ROLE_ID}>')


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

keep_alive()
client.run(os.getenv('TOKEN'))