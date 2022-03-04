from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am WolfBot! I have booted up and am fully functional! My commands are as followed: $inspire me; generates a random quote | What's my name?; Replies with your username. | I need help from Wolf (Wolfs_Official), or other Admins! | "

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()