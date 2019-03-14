"""
    This module provides all of the stuffs about `get_code_handler`
"""
from telegram.ext import ConversationHandler, RegexHandler
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm
import database.db_handler as db
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
    user = update.message.from_user
    code = get_code(user)
    if code is None:
        # There is no code, so we're going to generate one
        code = generate_code(user)
        # Adds the init credit
        db.add_credit(user.id, 100)

    update.message.reply_text(bm.get_code_message + "\n" + code)


# Generates a unique string as user invite code
def generate_code(user):
    # TODO: Generate a unique string
    # TODO: Put the range in config file
    generated_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    result = db.insert_code(user, generated_code)
    print(generated_code)
    print(result)
    if result:
        return generated_code
    else:
        return None


# Checks the DB for the invite code
def get_code(user):
    return db.get_code(user)
