"""
    This module holds the stuff about unknown commands or messages
"""
from telegram.ext import MessageHandler, Filters
from constants.messages import BotMessages as bm
from handlers.menu_handler import start


# This method generates the whole stuffs about unknown commands
def generate_unknown_handler():
    return MessageHandler(Filters.command | Filters.text, unknown_entry)


# Entry point, displays the unknown command message
def unknown_entry(bot, update):
    update.message.reply_text(bm.unknown_command_message)
    # Displays the main menu
    return start(bot, update)
