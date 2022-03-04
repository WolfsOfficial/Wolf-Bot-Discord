import discord
import requests
import json
from replit import db
import time


client = discord.Client()

sad_words = ["sad", "Sad", "depressed", "Depressed", "unhappy", "Unhappy", "angry", "Angry", "miserable", "Miserable", "misery", "Misery", "sadness", "Sadness"]
#Dictionary finishes

#Encouragements listed below will be outputed by the bot when any user uses command: "$Encouragement"
starter_encouragements = [
  "Cheer up!", "Hang in there.", "You are a great person / bot!", "You can do it!", "We Believe in you!", "Don't give up!", "Keep trying!", "Everything you need to accomplish your goals is already in you.", "Be gentle with yourself. You’re doing the best you can!", "Sometimes when you are in a dark place you think you have been buried, but actually you have been planted.", "Good luck today!", "You got this!", "Sending major vibes your way!", "Hope you're doing awesome!", "Keep on keeping on!", "As an AI bot with infinite knowledge and intelligence, I can see the end in you, and you will succeed!",
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

Random_Phrase = [
      'Something Random', 'The Pink Alphabet', 'Purple polkadot monkeys!', '123... 456... 78, okay thats enough', 'what? you want a random phrase? NO!', 'this is an Official Message from <@912504068612698132>', "This is random message for{0.author.mention}!", 'I will not generate a random phrase!!', "Mono Sodium Glutamate", "genetically modified organisms", "The current time is: (Paste time here)", "* Serving Flask app '' (lazy loading) * Environment: production WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.", 
]

Insult = ["an insult", "why should I generate a meticulous and spectacular gag about you when you already are a jest in itself.", "Instead of buying the family size potato chip bag for your gallon sized gut, you should look into jogging those flabby calves or bubble butt!", "You overentitled, over compensated, little bipolar chuckle f$#&!", "You suck, swallow, choke, and chew.", "Ask me again and I'll hire a professional assasin who'll use you as their punching meat bag!", "You shouldn't ask a Wolf, especially one who's a bot and infintely smarter then you to insult your pea sized brain, its bad for your mental health which is slacking of course.", "Scientists say the human brain stops growing at 18, but I'm pretty sure your's never grew at all!", "Brain(n.):Something you may have but definitely don't use.", "I know what you did last summer. It wasn't terribly exciting.", "Enjoy the sun, this marks the last day you'll ever see it.", "Don't worry, that wasn't a ghost you just heard. It was only a serial killer.", "Let me plan your night for you! Step one, file off all your fingerprints.", "That whale sized cloud reminds me of your mother.", "Today is a perfect day to remember all the pets you'll never get to cuddle ever again.", "Today is a perfect day to push some Flat Earthers off the side of the disk.", "F.Y.I your pathetic sun is a giant fusion reactor with fewer safety protocols than Chernobyl.", "Today is a perfect day to jump out of an airplane with a parachute backpack full of silverware.", "Today is a perfect day to hack the Russian navy's launch computers.", "It's raining, it's pouring, the old main has fallen and can't get up.", "You suck. Period.",
]

#If you are updating the responses, instead of updating every number in the sequence below, add an "_" after the number before the new response IE: (Response 3) NEW LINE (Response 3_1) etc. 

res_time = time.asctime(time.localtime())
res000 = "Whoops! This command isn't coded in yet, try again later or ask <@352658813028925450> on the status of said command"
res01 = 'Generating Random word please wait!'
res02 = "Okay, you asked for it!"
res03 = "FYI The time is in UTC, subtract or add to align with your Timezone."
res1 = "Awesome!"
res2 = "You are indeed!"
res3 = "Right!"
res4 = "Uh, yes! Yes you are right!"
res5_0 = "<@352658813028925450> Please help!"
res5_1 = 'USER ID OF ADMIN Please help!'
res5_2 = 'USER ID OF ADMIN Please help!'
res6 = 'USER ID OF ADMIN, and/or <@352658813028925450> Please help {0.author.mention}!'
res7 = "It's {0.author.mention} of course!"
res8 = ' Your current role is: <@&${ROLE_ID}>'
res9_0 = 'Hello {0.author.mention}!'
res9_1 = 'Hi there {0.author.mention}!'
res10 = 'Uhh, {0.author.mention} This is not an email server silly!'
res11 = 'Testing 1.2.3.! Yep its working {0.author.mention}'
res12 = 'Happy Birthday! 🎈🎉'
