from aiogram import Dispatcher, Bot, types, executor

TOKEN = 'YOUR_BOT_TOKEN'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Assalomu alaykum, {message.from_user.full_name} men echo botman!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
