from aiogram import Bot, Dispatcher, types
import asyncio

from confidentially import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def yoyo(message:types.Message):
    await message.answer(text='привет')

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))




