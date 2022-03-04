#Not actively used, reserved for future use!
import discord
import random
from replit import db
import responses

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  quote = responses.get_quote()

#Replies for inspire start
  if msg.startswith("$Inspire Me"):
    await message.channel.send(quote)
  if msg.startswith("$inspire Me"):
    await message.channel.send(quote)
  if msg.startswith("$Inspire me"):
    await message.channel.send(quote)
  if msg.startswith("$inspire me"):
    await message.channel.send(quote)

  if db["responding"]:
    options = responses.starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]
    if any(word in msg for word in responses.sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    responses.update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      responses.delete_encouragment(index)
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

#Replies for inspire end

#Replies stated below is what the BOT will output AFTER any USER says what's defined after: "startswith" on the server.

  if msg.startswith('yay'):
      await message.reply(responses.res1)
  if msg.startswith('Yay'):
      await message.reply(responses.res1)
  if msg.startswith('cool'):
      await message.reply(responses.res2)
  if msg.startswith('Cool'):
      await message.reply(responses.res2)
  if msg.startswith('Neato'):
      await message.reply(responses.res3)
  if msg.startswith('Am I Right'):
      await message.reply(responses.res4)
  if msg.startswith('Am I right'):
      await message.reply(responses.res4)
  if msg.startswith('am I right'):
      await message.reply(responses.res4)
  if msg.startswith('am i right'):
      await message.reply(responses.res4)
  if msg.startswith('Am i right'):
      await message.reply(responses.res4)

  if msg.startswith('I need help from Wolf'):
      await message.reply(responses.res5_0)
  if msg.startswith('I need help from France'):
      await message.reply(responses.res5_1)
  if msg.startswith('I need help from Dread'):
      await message.reply(responses.res5_2)
  if msg.startswith('I need help from wolf'):
      await message.reply(responses.res5_0)
  if msg.startswith('I need help from france'):
      await message.reply(responses.res5_1)
  if msg.startswith('I need help from dread'):
      await message.reply(responses.res5_2) 
  if msg.startswith('I need help from mods'):
      await message.reply(responses.res6.format(message))

  if msg.startswith("What's my name"):
      await message.reply(responses.res7.format(message))
  if msg.startswith('Whats my name'):
      await message.reply(responses.res7.format(message))
  if msg.startswith("what's my name"):
      await message.reply(responses.res7.format(message))
  if msg.startswith('whats my name'):
      await message.reply(responses.res7.format(message))
  if msg.startswith("What's my role"):
      await message.reply(responses.res8.format(message))
  if msg.startswith("Hi there"):
      await message.reply(responses.res9_0.format(message))
  if msg.startswith("hi there"):
      await message.reply(responses.res9_0.format(message))
  if msg.startswith('Hello'):
      await message.reply(responses.res9_1.format(message))
  if msg.startswith('hello'):
      await message.reply(responses.res9_1.format(message))
  if msg.startswith('helo'):
      await message.reply(responses.res10.format(message))
  if msg.startswith('Helo'):
      await message.reply(responses.res10.format(message))
  if msg.startswith('$Testing'):
      await message.channel.send(responses.res11.format(message))
  if msg.startswith('$testing'):
      await message.channel.send(responses.res11.format(message))      

  if msg.startswith('happy birthday'):
      await message.channel.send(responses.res12)
  if msg.startswith('Happy Birthday'):
      await message.channel.send(responses.res12)
  if msg.startswith('Happy birthday'):
      await message.channel.send(responses.res12)
  if msg.startswith('happy Birthday'):
      await message.channel.send(responses.res12)

  if msg.startswith('testingabc'):
      await message.reply(responses.res1)

  if message.content == '$Random word':
      response = random.choice(responses.Random_Word)
      await message.channel.send(response)
  if message.content == '$random Word':
      response = random.choice(responses.Random_Word)
      await message.channel.send(response)
  if message.content == '$Random Word':
      response = random.choice(responses.Random_Word)
      await message.channel.send(response)
  if message.content == '$Random Word':
      response = random.choice(responses.Random_Word)
      await message.channel.send(response)

#Replies Finish Here


#Joke Generator starts now

  if message.content == '$Generate joke':
      await message.reply(responses.joke_response.text)
  if message.content == '$generate joke':
      await message.reply(responses.joke_response.text)
  if message.content == 'tell me a joke':
      await message.reply(responses.joke_response.text)
  if message.content == 'Tell me a joke':
      await message.reply(responses.joke_response.text)

#Joke Generator ends now

#Tell time starts now
  if msg.startswith('Tell me the time'):
    await message.reply('Whoops! This command isn\'t coded in yet, try again later or ask <@352658813028925450> on the status of said command')
  if msg.startswith('tell me the time'):
    await message.reply('Whoops! This command isn\'t coded in yet, try again later or ask <@352658813028925450> on the status of said command')