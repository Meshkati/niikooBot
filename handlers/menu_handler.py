"""
    This module provides all of the stuffs about `menu_handler`
"""
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm

# Keyboard buttons
main_keyboard = [[btm.my_code, btm.friends_code, btm.my_credit, btm.new_debt, btm.unpaid_debts, btm.paid_debts, btm.help]]


# This method generates the whole stuffs about start command
# like conversation trigger buttons
def generate_menu_handler():
    return CommandHandler('start', start)


# Displays the menu
def start(bot, update):
    update.message.reply_text(bm.start_message,
                              reply_markup=ReplyKeyboardMarkup(main_keyboard, one_time_keyboard=True))
