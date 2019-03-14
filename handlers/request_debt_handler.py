"""
    This module provides all of the stuffs about `request_debt`
    By this conversation, a user can put a request for loan on the system.
    It first checks the credit of the user and if everything goes well, puts the
    debt request on the system and notifies all of the friends for pay
"""
from telegram.ext import ConversationHandler, RegexHandler, MessageHandler, Filters
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm

# Generating the states of this handler
REQUEST_AMOUNT = range(1)


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
                              "\n" +
                              str(left_credit_amount) +
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
    # TODO: Place the debt request
    update.message.reply_text(bm.request_debt_succeed)
    return ConversationHandler.END


# Calculates the credit that user can pay for the debt request
def fetch_left_credit(user):
    # TODO: Implement it
    return 500
