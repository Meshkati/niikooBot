"""
    This module provides all of the stuffs about `paid_handler` list
    It goes through all of the user user transactions and shows the payments that are paid before
"""
from telegram.ext import RegexHandler
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm


# This method generates the whole stuffs about paid_handler
def generate_paid_handler():
    return RegexHandler("(" + btm.paid_debts + ")$", paid_handler_entry)


# The entry point of this handler, it shows the lis of items
def paid_handler_entry(bot, update):
    user = update.message.from_user
    paid_list = fetch_paid_list(user)
    # parsing the list items
    result = ""
    for item in paid_list:
        result += str(item[0])
        result += str(item[2])
        result += str(item[1])

    update.message.reply_text(result)


# Gets the list of paid items from DB
def fetch_paid_list(user):
    # TODO: Implement it
    return [
        ["Transaction 1", 1780, 200],
        ["Transaction 2", 2300, 1000],
        ["Transaction 3", 1400, 1800]
    ]
