"""
    This module provides all of the stuffs about `get_code_handler`
"""
from telegram.ext import ConversationHandler, RegexHandler
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm
import random
import string


# This method generate the whole stuffs about get_code command
# to get the invitation code and give it to a friend
def generate_get_code_handler():
    return ConversationHandler(
        entry_points=[RegexHandler("(" + btm.my_code + ")$", get_code_or_generate)],
        # TODO: Manage states
        states={

        },
        # TODO: Create fallback
        fallbacks=[]
    )


# Checks if the user has already registered or not
# to return the appropriate invite code
def get_code_or_generate(bot, update):
    code = get_code()
    if code is None:
        # There is no code, so we're going to generate one
        code = generate_code()

    update.message.reply_text(bm.get_code_message + "\n" + code)


# Generates a unique string as user invite code
def generate_code():
    # TODO: Generate a unique string
    # TODO: Put the range in config file
    # TODO: Persist the code
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))


# Checks the DB for the invite code
def get_code():
    # TODO: Check the db for the code
    return None
