# not required, but nice for predictive text and tab completion
from aiogram import Bot, Dispatcher, executor, types

# importing modules
import asyncio
from datetime import datetime
import credentials
import re, math

async def startMessage(bot, message):
    await bot.send_message(message['from']['id'], "Welcome to this bot.")

async def functionsExample(bot, message, commandargument):
    print('call this function by using\nawait F.functionsExample(bot, message, commandargument')


