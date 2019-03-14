"""
    This module provides all of the stuffs about `request_debt`
    By this conversation, a user can put a request for loan on the system.
    It first checks the credit of the user and if everything goes well, puts the
    debt request on the system and notifies all of the friends for pay
"""
from telegram.ext import ConversationHandler, RegexHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm
import database.db_handler as db

# Generating the states of this handler
REQUEST_AMOUNT = range(1)

# Notify Debt keyboard
notify_debt_keyboard = [[btm.notify_debt]]


# This method generates the whole stuffs about request_debt_handler
def generate_request_debt_handler():
    return ConversationHandler(
        entry_points=[RegexHandler("(" + btm.new_debt + ")$", request_debt_handler_entry)],
        states={
            REQUEST_AMOUNT: [MessageHandler(Filters.text, get_request_amount)]
        },
        fallbacks=[]
    )


# The entry point of this handler, it starts to get values
def request_debt_handler_entry(bot, update):
    user = update.message.from_user
    left_credit_amount = fetch_left_credit(user)
    update.message.reply_text(bm.request_debt_amount_message +
                              str(left_credit_amount) +
                              "\n" +
                              bm.request_debt_message)

    return REQUEST_AMOUNT


# Gets the desired debt amount from user
def get_request_amount(bot, update):
    requested_amount = int(update.message.text)
    user = update.message.from_user
    # Check if the requested amount is valid
    if requested_amount > fetch_left_credit(user) * 1000:
        update.message.reply_text(bm.request_debt_failed)
        return ConversationHandler.END
    # User has the required credit, so we place the debt request
    debt_result = place_debt(user.id, requested_amount)
    notify_friends(bot, user.id, debt_result)
    if debt_result:
        update.message.reply_text(bm.request_debt_succeed)
    else:
        update.message.reply_text(bm.unknown_error)

    return ConversationHandler.END


# Calculates the credit that user can pay for the debt request
def fetch_left_credit(user):
    # TODO: Implement it
    return 500


# Places a debt request
def place_debt(user_id, amount):
    result = db.insert_debt(user_id, amount)
    return result


# Notifies the friends of a user to pay for him
def notify_friends(bot, user_id, debt_id):
    debt = db.get_debt(debt_id)
    friends = db.get_friend_ids(user_id)

    for friend in friends:
        bot.send_message(chat_id=friend,
                         text=bm.notify_debt_title_1 + str(debt["amount"]) + bm.notify_debt_title_2,
                         reply_markup=ReplyKeyboardMarkup(notify_debt_keyboard, one_time_keyboard=True))
