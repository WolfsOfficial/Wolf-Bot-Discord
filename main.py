import discord
import os
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import logging
from dotenv import load_dotenv
import responses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Dictionary Starts
client = discord.Client()
bot = commands.Bot(command_prefix = '#')

#When bot is ready, it prints out the declaring it is ready
@client.event
async def on_ready():
  print("We have logged in as {0.user} Please wait while we boot up!".format(client))
  print(f'{client.user.name} has connected to Discord!')

@bot.command()
async def whereAmI(ctx, *, messageContents):
    link = await ctx.channel.create_invite(max_age = 300)
    message = f'You are in {ctx.message.guild.name} in the {ctx.message.channel.mention} channel with an invite link of ' + link
    await ctx.message.author.send(message)


#Replies Start now
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

#Replies for inspire start
  if msg.startswith("$Inspire me!"):
    quote = responses.get_quote()
    await message.channel.send(quote)
  if msg.startswith("$inspire me!"):
    quote = responses.get_quote()
    await message.channel.send(quote)
  if msg.startswith("$Inspire me"):
    quote = responses.get_quote()
    await message.channel.send(quote)
  if msg.startswith("$inspire me"):
    quote = responses.get_quote()
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
      await message.reply('Awesome!')
  if msg.startswith('Yay'):
      await message.reply('Awesome!')
  if msg.startswith('cool'):
      await message.reply('You are ineed!')
  if msg.startswith('Cool'):
      await message.reply('You are ineed!')
  if msg.startswith('Neato'):
      await message.reply('Right!')
  if msg.startswith('Am I Right'):
      await message.reply('Uh, yes! Yes you are right!')
  if msg.startswith('Am I right'):
      await message.reply('Uh, yes! Yes you are right!')
  if msg.startswith('am I right'):
      await message.reply('Uh, yes! Yes you are right!')              

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

  if msg.startswith('What\'s my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))
  if msg.startswith('Whats my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))
  if msg.startswith('what\'s my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))
  if msg.startswith('whats my name'):
      await message.reply('It\'s {0.author.mention} of course!'.format(message))
  if msg.startswith('What\'s my role'):
      await message.reply(' Your current role is: <@&${ROLE_ID}>'.format(message))
  if msg.startswith("Hi there"):
      await message.reply('Hello {0.author.mention}!'.format(message))
  if msg.startswith("hi there"):
      await message.reply('Hello {0.author.mention}!'.format(message))
  if msg.startswith('Hello'):
      await message.reply('Hi there {0.author.mention}!'.format(message))
  if msg.startswith('hello'):
      await message.reply('Hi there {0.author.mention}!'.format(message))
  if msg.startswith('helo'):
      await message.reply('Awaiting response from email server! {0.author.mention}!'.format(message))
  if msg.startswith('Helo'):
      await message.reply('Awaiting response from email server! {0.author.mention}!'.format(message))
  if msg.startswith('$Testing'):
      await message.channel.send('Testing 1.2.3.! Yep its working {0.author.mention}'.format(message))
  if msg.startswith('$testing'):
      await message.channel.send('Testing 1.2.3.! Yep its working {0.author.mention}'.format(message))      

  if msg.startswith('happy birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')
  if msg.startswith('Happy Birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')
  if msg.startswith('Happy birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')
  if msg.startswith('happy Birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if message.content == '$Random word':
      response = random.choice(responses.Random_Word)
      await message.channel.send(response)

#Replies Finish Here


#Joke Generator starts now

#WIP

#Joke Generator ends now

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

keep_alive()

client.run(os.getenv('TOKEN'))