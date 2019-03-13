"""
    This module provides all o the stuffs about `add_code_handler`
    By this part, the user can add other users code and joins to their
    network for request debts or provide loan
"""
from telegram.ext import ConversationHandler, RegexHandler, MessageHandler, Filters
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm

# Generating the states code
ADD_CODE = range(1)


# This method generates the whole stuffs about add_code command
def generate_add_code_handler():
    return ConversationHandler(
        entry_points=[RegexHandler("(" + btm.friends_code + ")$", add_code_entry)],
        # TODO: Manage states
        states={
            ADD_CODE: [MessageHandler(Filters.text, add_code)]
        },
        # TODO: Create fallback
        fallbacks=[]
    )


# Send the enter code message to the user and then goes to the next state
def add_code_entry(bot, update):
    update.message.reply_text(bm.enter_code_message)

    return ADD_CODE


# Gets the code from user and joins to the network
def add_code(bot, update):
    user = update.message.from_user
    code = update.message
    if join_to_network(user, code):
        update.message.reply_text(bm.enter_code_confirmed)
    else:
        update.message.reply_text(bm.enter_code_failed)

    return ConversationHandler.END


# Joins a user to the network of the other user
def join_to_network(user_id, invite_code):
    # TODO: Implement it later
    return True
