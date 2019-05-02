from flask import render_template,request,redirect,jsonify
from app.main import main
from app.handlers import DialogFlowHandler
from app.handlers import pusher_client
from app.handlers import BotCommandsHandler

dialogflow_handler=DialogFlowHandler()
bot_commands_handler=BotCommandsHandler()

@main.route("/")
def index():
    return render_template("./index.html")

@main.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    h_r=bot_commands_handler.handle(message)
    if h_r[0]:
        fulfillment_text=h_r[1]
    else:
        fulfillment_text=dialogflow_handler.detect_user_intent(message)
   
    response_text = { "message":  fulfillment_text }
    socketId = request.form['socketId']
    pusher_client.trigger('MOJO', 'new_message', 
                             {'human_message': message, 'bot_message': fulfillment_text},
                             socketId)
    return jsonify(response_text)