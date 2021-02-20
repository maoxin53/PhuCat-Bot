import random
from quotesInArray import quotes, authors
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from Catclass import lolcat  # translate, cat_pic
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os

TOKEN = <Telebot Token>

reply_keyboard = [
    ['I nid your wisdom'],
    ['Tell me sumthin', 'Can you speak ?'],
    ['Done']
]

reply_keyboard2 = [
    ['I nid your wisdom'],
    ['Tell me sumthin else', 'Can you speak ?'],
    ['Feed', 'Pat'],
    ['Done']
]

reply_keyboard3 = [
    ['I nid moar wisdom'],
    ['Tell me sumthin', 'Can you speak ?'],
    ['Feed', 'Pat'],
    ['Done']
]

reply_keyboard4 = [
    ['Tell me sumthin'],
    ['I nid your wisdom']
]

reply_keyboard5 = [
    ['I nid your wisdom'],
    ['Tell me sumthin', 'Can you speak ?'],
    ['Feed', 'Pat'],
    ['Done']
]


welcome_message = "Herrow I am a Cat Bot, I send photos of my feline friends and pretentious quotes only if I like you. \n\n" + "To get help send /help.\n" + "To enjoy quality content press da buttons!"

reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
reply_markup2 = ReplyKeyboardMarkup(reply_keyboard2, resize_keyboard=True, one_time_keyboard=True)
reply_markup3 = ReplyKeyboardMarkup(reply_keyboard3, resize_keyboard=True, one_time_keyboard=True)
reply_markup4 = ReplyKeyboardMarkup(reply_keyboard4, resize_keyboard=True, one_time_keyboard=True)
reply_markup5 = ReplyKeyboardMarkup(reply_keyboard5, resize_keyboard=True, one_time_keyboard=True)

# -------------------------- COMMANDS -----------------------------#
def start_command(update, context):
    update.message.reply_text(welcome_message, reply_markup = reply_markup)


fed = ["Sanks for ur offering!", "*Chomp*", "I'm not hungry, meow"]
def feed_command(update, context):
    le_msg = random.choice(fed)
    if (le_msg == "Sanks for ur offering!"):
        update.message.reply_animation('https://media.giphy.com/media/9V5kjx3MRcVyE3kYpN/giphy.gif')
        update.message.reply_text(le_msg, reply_markup = reply_markup5)
    elif (le_msg == "*Chomp*"):
        update.message.reply_animation('https://media.giphy.com/media/dZ4bQpRdpg6C0G5obl/giphy.gif')
        update.message.reply_text(le_msg, reply_markup = reply_markup5)
    else:
        update.message.reply_animation('https://media.giphy.com/media/3Xw6TGuAa39J2X3a1q/giphy.gif')
        update.message.reply_text(le_msg, reply_markup = reply_markup5)


pat = ["*Scratch* Hisssss", "Tats the spot "]
def pat_command(update, context):
    the_msg = random.choice(pat)
    if (the_msg == pat[0]):
        update.message.reply_photo("https://i.imgflip.com/2eg63l.jpg", reply_markup = reply_markup5)
        update.message.reply_text(pat[0])
    if (the_msg == pat[1]):
        update.message.reply_photo("https://filmdaily.co/wp-content/uploads/2020/05/coughing-cat-meme-lede.jpg", reply_markup = reply_markup5)
        update.message.reply_text(pat[1])



def help_command(update, context):
    update.message.reply_photo("https://knowyourmeme.com/photos/1878329", reply_markup = reply_markup5)
    update.message.reply_text("Help yourself, I'm a cat")


cat = lolcat()


def done_command(update, context):
    photo_link = cat.cat_pic()
    update.message.reply_photo(photo_link)
    update.message.reply_text("I don't care 😾😾\n Bye!")


def need_wisdom_command(update, context): #quote command
    num = random.randint(0,len(quotes))
    text = cat.translate(quotes[num]) + " \n\n - 😸"+ authors[num] + "😸"
    meow = '🐾meow meowww mraorr🐾 ' * random.randint(1, 2)
    keyboard = [[InlineKeyboardButton("Translate", callback_data = meow)]]

    photo_link = cat.cat_pic()
    update.message.reply_photo(photo_link, reply_markup = reply_markup3)
    update.message.reply_text(text, reply_markup = InlineKeyboardMarkup(keyboard))


def button(update, context): #for Inline Keyboard
    query = update.callback_query
    query.edit_message_text(text=query.data)


def rng():
    a,b = random.randint(1,100),random.randint(30, 40)
    return a,b


def tell_me_command(update, context):
    a,b = rng()
    if (a==b):
        photo_link = cat.cat_pic()
        update.message.reply_photo(photo_link, reply_markup = reply_markup2)
        update.message.reply_text("In ways you don't know yet, this is a lucky cat!")

    elif (a<b): #higher probability
        num = random.randint(0,len(quotes))
        text = cat.translate(quotes[num]) + " \n\n - 😸"+ authors[num] + "😸"
        meow = '🐾meow meowww mraorr🐾 ' * random.randint(1, 2)
        keyboard = [[InlineKeyboardButton("Translate", callback_data = meow)]]
        photo_link = cat.cat_pic()
        update.message.reply_photo(photo_link, reply_markup = reply_markup2)
        update.message.reply_text(text, reply_markup = InlineKeyboardMarkup(keyboard))

    else:
        update.message.reply_text("The cat is uninterested...", reply_markup = reply_markup4)


languages = [ 'Yes I can speak English 🇬🇧', '是的，我会说中文 🇨🇳', 'はい、日本語が話せます 🇯🇵',
            '네 한국어를 할 수 있습니다 🇰🇷', 'Ya saya boleh berbahasa Melayu 🇲🇾',
            'ஆம் என்னால் மலாய் பேச முடியும் 🇮🇳',
            'Oui je peux parler français 🇫🇷',
            'Si puedo hablar español 🇪🇸',
            'Ja ich kann deutsch sprechen 🇩🇪', 'ใช่ฉันพูดภาษาไทยได้ 🇹🇭',
            'Да я могу говорить по русски 🇷🇺']


def can_u_speak_command(update, context):
    if len(languages) == 0:
        update.message.reply_text('meowww', reply_markup = reply_markup2)
    update.message.reply_text(random.choice(languages), reply_markup = reply_markup2)


def echo_command(update, context):
    if (update.message['text'] == 'Feed'):
        feed_command(update, context)
    elif (update.message['text'] == 'Pat'):
        pat_command(update, context)
    elif (update.message['text'] == 'Done'):
        done_command(update, context)
    elif (update.message['text'] == 'Tell me sumthin') or (update.message['text'] == 'Tell me sumthin else'):
        tell_me_command(update, context)
    elif (update.message['text'] == 'Can you speak ?' ):
        can_u_speak_command(update, context)
    elif (update.message['text'] == 'I nid your wisdom') or (update.message['text'] == 'I nid moar wisdom'):
        need_wisdom_command(update, context)
    else:
        update.message.reply_text("Use da buttons f00L", reply_markup = reply_markup)


def main():
    
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)
    # add handlers
    

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CallbackQueryHandler(button))

    # on noncommand i.e message - echo the message on Telegram ----- ONLY CAN 1 (I think)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo_command))
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN)
    updater.bot.set_webhook("https://phucat-bot.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

"""
Authors: Mervyn Ho, Poh Mao Xin, Luo Xiao yang
Credits to: https://speaklolcat.com/,
            https://api.thecatapi.com/v1/images/search,
            https://type.fit/api/quotes
Referred to: https://www.youtube.com/watch?v=5nhdxpoicW4&t,
             https://www.mindk.com/blog/how-to-develop-a-chat-bot/,
             https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot2.py
"""
