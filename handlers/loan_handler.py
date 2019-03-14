"""
    This module provides all of the stuffs about `loan_handler`
    It gets an loan request and generates a invoice about it
"""
import json
from telegram.ext import ConversationHandler, RegexHandler
from telegram import LabeledPrice
from constants.button_messages import ButtonMessages as btm
from constants.messages import BotMessages as bm
import database.db_handler as db

# Generates states of the loan conversation
INVOICE = range(1)


# This method generates the whole stuff about handling loans
def generate_loan_handler():
    return ConversationHandler(
        entry_points=[RegexHandler("[\d\D]*", loan_entry)],
        states={
            INVOICE: []
        },
        # TODO: Create fallback
        fallbacks=[]
    )


# This method is the entry point of the loan handler, it takes the debt ID
# and fetch it to produce the invoice
def loan_entry(bot, update):
    # FIXME: Fix the logs
    message = update.message.text
    print(message)
    message = message.split(btm.notify_debt)
    print(message)
    message = message[0]
    message = message[:-1]
    print(message)
    # Generating the invoice
    debt = db.get_debt(message)
    bot.send_invoice(chat_id=update.message.chat_id,
                     title=bm.loan_invoice_title,
                     description=bm.loan_invoice_description,
                     payload="payload",
                     provider_token="6104337885264463",
                     start_parameter="",
                     currency="IRR",
                     prices=[LabeledPrice('مبلغ', int(debt["amount"] * 10))])
    return INVOICE


# This step is after generating the invoice
def handle_invoice(bot, update):
    successful_payment = update.message.successful_payment
    print(bm.successful_payment + " %s", successful_payment.invoice_payload)
    invoice_payload = json.loads(successful_payment.invoice_payload)
    update.message.reply_text(bm.failed_payment +
                              " {}".format(invoice_payload.get('traceNo')))
    return ConversationHandler.END
