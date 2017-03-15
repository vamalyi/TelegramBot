import conf
import telebot
import logging

bot = telebot.TeleBot(conf.TOKEN)

logger = telebot.logger

if conf.LOG_ON:
    telebot.logger.setLevel(logging.DEBUG)

# command
@bot.message_handler(commands=["dev"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, bot.get_me().first_name)

# regexp
@bot.message_handler(regexp='tst')
def command_help(message):
    bot.send_message(message.chat.id, 'Did someone call for help?')

# any_other
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Error. Can't proccess :/")


if __name__ == '__main__':
    bot.polling(none_stop=True)


"""
Message handler decorator.
This decorator can be used to decorate functions that must handle certain types of messages.
All message handlers are tested in the order they were added.

Example:

bot = TeleBot('TOKEN')

# Handles all messages which text matches regexp.
@bot.message_handler(regexp='someregexp')
def command_help(message):
    bot.send_message(message.chat.id, 'Did someone call for help?')

# Handle all sent documents of type 'text/plain'.
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def command_handle_document(message):
    bot.send_message(message.chat.id, 'Document received, sir!')

# Handle all other commands.
@bot.message_handler(func=lambda message: True, content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def default_command(message):
    bot.send_message(message.chat.id, "This is the default command handler.")

:param regexp: Optional regular expression.
:param func: Optional lambda function. The lambda receives the message to test as the first parameter. It must return True if the command should handle the message.
:param content_types: This commands' supported content types. Must be a list. Defaults to ['text'].
"""