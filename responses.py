import discord
import requests
import json
from replit import db


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



Random_Word = [
      'Something Random', 'The Pink Alphabet', 'Purple polkadot monkeys!', '123... 456... 78, okay thats enough', 'what? you want a random word? NO!', 'this is an Official Message from <@912504068612698132>', "'This is random message for{0.author.mention}!'.format(message)", 'I will not!',
]

joke_response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,political,racist,sexist,explicit&format=txt")

#If you are updating the responses, instead of updating every number in the sequence below, add an "_" after the number before the new response IE: (Response 3) NEW LINE (Response 3_1) etc. 

res1 = "Awesome!"
res2 = "You are indeed!"
res3 = "Right!"
res4 = "Uh, yes! Yes you are right!"
res5_0 = "<@352658813028925450> Please help!"
res5_1 = '<@707681681074814977> Please help!'
res5_2 = '<@911664002197749893> Please help!'
res6 = '<@911664002197749893>, <@707681681074814977>, and/or <@352658813028925450> Please help {0.author.mention}!'
res7 = "It's {0.author.mention} of course!"
res8 = ' Your current role is: <@&${ROLE_ID}>'
res9_0 = 'Hello {0.author.mention}!'
res9_1 = 'Hi there {0.author.mention}!'
res10 = 'This is not an email server! {0.author.mention} silly!'
res11 = 'Testing 1.2.3.! Yep its working {0.author.mention}'
res12 = 'Happy Birthday! 🎈🎉'