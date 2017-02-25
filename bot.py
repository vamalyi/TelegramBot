import conf
import telebot
import logging

bot = telebot.TeleBot(conf.TOKEN)

logger = telebot.logger

if conf.LOG_ON:
    telebot.logger.setLevel(logging.DEBUG)

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, bot)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Error. Can't proccess :/")


if __name__ == '__main__':
    bot.polling(none_stop=True)