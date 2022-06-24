# for my friends on telegram, my standard frame
# author: @Lynnsane

# logging
import logging

# telegram
from aiogram import Bot, Dispatcher, executor, types

# import of local files
import credentials
import lib as F

# see attached lib.py for F, credentials.py is a local file with credentials, keep this private, as it contains the bot token

logging.basicConfig(level=logging.INFO)
# token is taken from local credentials file
bot = Bot(token=credentials.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# handle regular messages here
@dp.message_handler()
async def plainMessageHandling(message: types.Message):
    # strip the @usernamebot from incoming commands, to keep this compatible with test bots i saved this username in credentials.
    message.text = message.text.replace(credentials.botUsername, '')
    commandText = message.get_command()
    commandArguments = message.get_args()

    # commands
    if commandText: 
        #user commands
        if '/start' == commandText:
            # await the functions from the library file, pass the bot oject and the message, 
            # in addition to any other params you might need, like commandText or commandArguments
            await F.startMessage(bot, message, other_args)
            
    # forwards
    if message.forward_from:
        if message.forward_from.username == 'Lynnsane' and 'Example Forward' in message.text:
            await F.functionsExample(bot, message, other, args)

            
# handle new joins here
@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    print(message)

    
if __name__ == "__main__":
    # start the dispatcher here
    executor.start_polling(dp)
