"""
    This module provides all of the stuffs about `display_credit_handler`
    It tries to get the credit balance of a user and display it to him/her
"""
from telegram.ext import RegexHandler
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm


# This method generates the whole stuffs about display_credit command
def generate_display_credit_handler():
    return RegexHandler("(" + btm.my_credit + ")$", display_credit_entry)


# Fetch and displays the user credit
def display_credit_entry(bot, update):
    user = update.message.from_user
    credit = get_credit(user)
    update.message.reply_text(bm.display_credit_message +
                              str(credit) + '\n' +
                              bm.credit_info_message)


# This method gets the credit of a user
# TODO: Move this part to another module
# TODO: Check from the DB
def get_credit(user):
    return 12345
