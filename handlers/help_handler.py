"""
    This module provides all of the stuffs about `help_handler`
    It shows the basic terms of use of this bot
"""
from telegram.ext import RegexHandler
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm


# This method generates the whole stuffs about help_handler
def generate_help_handler():
    return RegexHandler("(" + btm.help + ")$", help_handler_entry)


# The entry point of this handler, it shoes the terms of use
def help_handler_entry(bot, update):
    update.message.reply_text(bm.terms_of_use)
