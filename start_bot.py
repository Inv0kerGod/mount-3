from aiogram import Bot,Dispatcher,types,executor

from config import token

bot = Bot(token = token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Привет студент!")

@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.answer("держи помощь")
    
@dp.message_handler(commands="geeks")
async def geeks(message:types.Message):
    await message.reply("курсы")
    
dp.message_handler(lambda message: message.text.lower()=='привет')
async def hello(message:types.Message):
    await message.reply("привет как дела")
    
@dp.message_handler(commands="photo")
async def photo(message:types.Message):
    await message.answer_photo("https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fcs8.pikabu.ru%2Fpost_img%2F2016%2F04%2F26%2F10%2Fog_og_146169357425958100.jpg&text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA&rpt=simage&lr=10310")

dp.message_handler(commands="location")
async def location(message:types.Message):
    await message.answer_location(0,0)
dp.message_handler(commands="contact")
async def contact(message:types.Message):
    last_name = "isko"
    first_name = "geeks"
    number = +996708381382
    await message.answer_contact(last_name=last_name,first_name=first_name,phone_number=number)
    
executor.start_polling(dp)
