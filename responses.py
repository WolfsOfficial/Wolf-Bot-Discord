import discord
import requests
import json
from replit import db
import random

client = discord.Client()

sad_words = ["sad", "Sad", "depressed", "Depressed", "unhappy", "Unhappy", "angry", "Angry", "miserable", "Miserable", "misery", "Misery", "sadness", "Sadness"]
#Dictionary finishes

#Encouragements listed below will be outputed by the bot when any user uses command: "$Encouragement"
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!",
  "You can do it!",
  "We Believe in you!",
  "Don't give up!",
  "Keep trying!",
  "Everything you need to accomplish your goals is already in you.",
  "Be gentle with yourself. You’re doing the best you can!",
  "Sometimes when you are in a dark place you think you have been buried, but actually you have been planted.",
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
async def on_message(message):
  if message.author == client.user:
    return

  Random_Word = [
      'Something Random', 'The Pink Alphabet', 'Purple polkadot monkeys!', '123... 456... 78, okay thats enough', 'what? you want a random word? NO!', 'this is an Official Message from <@912504068612698132>', 'This is random message for{0.author.mention}!'.format(message), 'I will not!',
  ]

  if message.content == '$Random word':
      response = random.choice(Random_Word)
      await message.channel.send(response)