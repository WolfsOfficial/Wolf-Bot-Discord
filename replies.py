import discord
import requests
import json
import random
from replit import db

#Dictionary Starts
client = discord.Client()


#Replies Start now
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

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

  if msg.startswith('happy birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if msg.startswith('Happy Birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if msg.startswith('Happy birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

  if msg.startswith('happy Birthday'):
      await message.channel.send('Happy Birthday! 🎈🎉')

#Replies Finish Here

  Random_Word = [
      'Something Random', 'The Pink Alphabet', 'Purple polkadot monkeys!', '123... 456... 78, okay thats enough', 'what? you want a random word? NO!', 'this is an Official Message from <@912504068612698132>', 'This is random message for{0.author.mention}!'.format(message), 'I will not!',
  ]

  if message.content == '$Random word':
      response = random.choice(Random_Word)
      await message.channel.send(response)
