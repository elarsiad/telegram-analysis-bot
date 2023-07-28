# SETUP: LOAD bot_local.py
from bot_local import *

# SETUP: FLASK (WEB FRAMEWORK)
from flask import Flask, request
app = Flask(__name__)

# SERVER SIDE: main route
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
   json_string = request.stream.read().decode("utf-8")
   update = telebot.types.Update.de_json(json_string)
   bot.process_new_updates([update])
   return "Bot is running", 200

# SERVER SIDE: webhook
@app.route("/")
def webhook():
   bot.remove_webhook()
   # TO DO: Edit the value of variable railway_public_domain according to the railway public domain
   railway_public_domain = "_____"

   # NOTE: You need to use a publically available URL that the Telegram servers can reach.
   bot.set_webhook(url=f'{railway_public_domain}/{TOKEN}')
   return "Bot is running", 200

if __name__ == "__main__":
    app.run()