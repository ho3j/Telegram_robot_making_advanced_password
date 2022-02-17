"""
Hossein Jalili
feb-17-2022
version 1.0.0
Telegram_robot_making_advanced_password 

"""

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext.filters import Filters
from telegram import Update
from telegram.chataction import ChatAction
from telegram.ext.messagehandler import MessageHandler
import string
from random import *
from datetime import datetime
from datetime import timedelta
 

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
token = "token"
messages = {
    "msg_start": "Hi {0} {1}, \nwelcome to Password creation robot.\n#ho3j",
    "msg_help": "Available Commands :-\n/l - letters\n/d - digits\n/s - symbols\n/ld - letters + digits\n/ls - letters + symbols\n/ds - digits  + symbols\n/lsd - letters + digits + symbols\n",

}


def write_operation(x):
    file_name = "save_time.txt"
    file = open( file_name, "a+" )
    file.write(x+"\n")
    file.close()

def inffo(update):
    update_="update_id: \t\t\t"+str(update.update_id)
    message_id="message_id: \t\t"+str(update.message.message_id)
    from_user="from_user: \t\t\t"+str(update.message.from_user.id)
    is_bot="is_bot: \t\t\t"+str(update.message.from_user.is_bot)
    first_name_from="first_name_from: \t"+str(update.message.from_user.first_name)
    last_name_from="last_name_from: \t"+str(update.message.from_user.last_name)
    username_from="username_from: \t\t"+str(update.message.from_user.username)
    language_code="language_code: \t\t"+str(update.message.from_user.language_code)
    chat_id = "chat_id: \t\t\t"+str(update.message.chat_id)
    first_name ="first_name_chat: \t"+ str(update.message.chat.first_name)
    last_name = "last_name_chat: \t"+str(update.message.chat.last_name)
    username = "username_chat: \t\t"+str(update.message.chat.username)
    type_ = "type_: \t\t\t\t"+str(update.message.chat.type)

    date="date: \t\t\t\t"+str((update.message.date)+timedelta(hours=3,minutes=30))
    text="text: \t\t\t\t"+str(update.message.text)

    length="length: \t\t\t"+str(len(update.message.text))

    write_operation("\n"+str(update_)+"\n"+str(message_id)+"\n"+str(from_user)+"\n"+str(is_bot)+"\n"+str(first_name_from)+"\n"+str(last_name_from)+"\n"+str(username_from)+"\n"+str(language_code)+"\n"+str(chat_id)+"\n"+str(first_name)+"\n"+str(last_name)+"\n"+str(username)+"\n"+str(type_)+"\n"+str(date)+"\n"+str(text)+"\n"+str(length)+"\n")

    # print("update_id: \t\t",update_)
    # print("message_id: \t\t",message_id)
    # print("from_user: \t\t",from_user)
    # print("is_bot: \t\t",is_bot)
    # print("first_name_from: \t",first_name_from)
    # print("last_name_from: \t",last_name_from)
    # print("username_from: \t\t",username_from)
    # print("language_code: \t\t",language_code)
    # print("chat_id: \t\t", chat_id)
    # print("first_name_chat: \t", first_name)
    # print("last_name_chat: \t", last_name)
    # print("username_chat: \t\t", username)
    # print("type_: \t\t\t", type_)
    # print("date: \t", date)
    # print("text: \t\t\t", text)
    # print("length: \t\t", length)



def start_handler(update: Update, context: CallbackContext):
    # when a user start the bot.

    # import pdb; pdb.set_trace()
    write_operation("==================")
    inffo(update)
    write_operation("/start")
    write_operation("==================")
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    chat_id = update.message.chat_id

    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=messages["msg_start"].format(first_name, last_name))

def help(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    write_operation("/help")
    write_operation("==================")
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(messages["msg_help"])


#--------------------------
def l(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(context.args[0])>2 :
        ss=10
    else :
        ss=context.args[0]
    chars = letters  
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
def d(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(str(context.args[0]))>2 :
        ss=10
    else :
        ss=context.args[0]
    chars =  digits  
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
def s(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(context.args[0])>2 :
        ss=10
    else :
        ss=context.args[0]
    chars = symbols 
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
#--------------------------
def ld(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(context.args[0])>2 :
        ss=10
    else :
        ss=context.args[0]
    chars = letters + digits 
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
def ls(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(context.args[0])>2 :
        ss=10
    else :
        ss=context.args[0]
    chars = letters + symbols 
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
def ds(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(context.args[0])>2 :
        ss=10
    else :
        ss=context.args[0]
    chars = digits + symbols 
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
#-----------------------------
def lsd(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] :
        ss=10
    elif len(context.args[0])>2 :
        ss=10
    else :
        ss=context.args[0]
    chars = letters + digits + symbols  
    txt= "".join(choice(chars) for x in range(int(ss)))
    write_operation(txt)
    write_operation("==================")
    # print(ss)
    # print(txt)
    
    update.message.reply_text(txt)
#-----------------------------

def unknown(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    write_operation(update.message.text)
    write_operation("==================")
    
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    write_operation(update.message.text)
    write_operation("==================")
    
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)




def main():
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.dispatcher.add_handler(CommandHandler('l', l, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('d', d, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('s', s, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('ls', ls, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('ld', ld, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('ds', ds, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('lsd', lsd, pass_args=True))

    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 

    updater.start_polling()
    # updater.idle()


main()
