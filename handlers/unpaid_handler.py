"""
    This module provides all of the stuffs about `unpaid_handler` list
    It goes through all of the transactions and shows the paid that are still
    unpaid, so the user can pay the debts
"""
from telegram.ext import ConversationHandler, RegexHandler, MessageHandler, Filters
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm

# Generating the states code
GET_ITEM = range(2)


# This method generates the while stuffs about unpaid_handler
def generate_unpaid_handler():
    return ConversationHandler(
        entry_points=[RegexHandler("(" + btm.unpaid_debts + ")$", unpaid_handler_entry)],
        states={
            GET_ITEM: [MessageHandler(Filters.text, get_item)]
        },
        # TODO: Create fallback
        fallbacks=[]
    )


# The entry pint of this handler, it shoes
def unpaid_handler_entry(bot, update):
    user = update.message.from_user
    unpaid_list = fetch_unpaid_list(user)
    # Parsing the list items
    result = ""
    for item in unpaid_list:
        result += str(item[0])
        result += str(item[2])
        result += str(item[1])

    update.message.reply_text(result)

    return GET_ITEM


# Gets the list from DB
def fetch_unpaid_list(user):
    # TODO: Implement it
    return [
        ["Transaction 1", 1200, 200],
        ["Transaction 2", 1300, 1000],
        ["Transaction 3", 2400, 1800]
    ]


# Gets an item
def get_item(bot, update):
    # TODO: Check the database
    return ConversationHandler.END
