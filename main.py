"""
    This is the main file of the project
    Everything starts from here
"""
from telegram import Bot
from telegram.ext import Updater
import logging
from handlers.menu_handler import *
from handlers.get_code_handler import *
from handlers.add_code_handler import *
from handlers.display_credit_handler import *

# Config logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


def main():
    # Creating the bot
    bot = Bot(token="1594290762:ef296b218893de4f303fe2ae96d47835cb2ff03b",
              base_url="https://tapi.bale.ai/",
              base_file_url="https://tapi.bale.ai/file/")
    updater = Updater(bot=bot)
    # Creating the dispatcher
    dp = updater.dispatcher
    # Adding the handlers
    dp.add_handler(generate_menu_handler())
    dp.add_handler(generate_get_code_handler())
    dp.add_handler(generate_add_code_handler())
    dp.add_handler(generate_display_credit_handler())
    # Starting the bot
    updater.start_polling(poll_interval=2)
    # For terminating the bot
    updater.idle()


if __name__ == '__main__':
    main()
