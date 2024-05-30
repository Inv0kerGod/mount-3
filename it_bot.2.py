from config import token
from aiogram import Dispatcher,types,Bot,executor
from logging import basicConfig, INFO


bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [types.KeyboardButton('О нас'),
                 types.KeyboardButton('Курсы'),
                 types.KeyboardButton('Адрес'),
                 types.KeyboardButton('Контакты')]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply(f"Здравствуйте,{message.from_user.full_name}!",reply_markup=start_keyboard)
    
@dp.message_handler(text='О нас')
async def about_as(message:types.Message):
    await message.reply("Geeks - это айти курсы в Оше кара балте бишкеке ")
    
@dp.message_handler(text='Контакты')
async def send_contact(message:types.Message):
    await message.answer(f"{message.from_user.first_name},наши контакты ")
    await message.answer_contact("+996708381382,""Nurdan","T")
    await message.answer_contact("+996708381382,""Nurdan","I")

@dp.message_handler(text='Адрес')
async def send_adress(message:types.Message):
    await message.reply("Ош")
    await message.reply_location(40.51931846586533, 72.80297788183063)

curses =[types.KeyboardButton('Backend'),
        types.KeyboardButton('Android'),
        types.KeyboardButton('Frontend'),
        types.KeyboardButton('UX/UI'),
        types.KeyboardButton('Детское программирование'),
        types.KeyboardButton('Основы программирования'),
        types.KeyboardButton('Оставить заявку'),
        types.KeyboardButton('Ios'),
        types.KeyboardButton('Назад')]

curses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*curses)

@dp.message_handler(text="Курсы")
async def all_courses(message:types.Message):
    await message.answer("Вот наши курсы:", reply_markup=curses_keyboard)
    
@dp.message_handler(text='Backend')
async def about_as(message:types.Message):
    await message.reply("Backend = это сервераня сторона сайта или приложения")
    
@dp.message_handler(text='Android')
async def about_as(message:types.Message):
    await message.reply("Android = это мобильная разработка под andoid")
    
@dp.message_handler(text='UX/UI')
async def about_as(message:types.Message):
    await message.reply("UX/UI = это дизайн")
    
@dp.message_handler(text='Frontend')
async def about_as(message:types.Message):
    await message.reply("Fronted = это лицевая сторона сайта или приложения ")
    
@dp.message_handler(text='Ios')
async def about_as(message:types.Message):
    await message.reply("Ios = это мобильная разработка под ios")
    
@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await start(message)
    
@dp.message_handler(text="Оставить заявку")
async def aplication(message:types.Message):
    button = types.KeyboardButton("Отправить контакт",request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста отправьте свой контакт",reply_markup=keyboard)
    

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_start(message:types.Message):
    await message.answer(message)
    await bot.send_message(-4246764571,f"заявка на курсы:\nИмя:{message.contact.first_name}\nФамилия:{message.contact.last_name}\nphone_number:{message.contact.phone_number}\n")
    await message.answer("Спасибо что оставили заявку")
    await start(message)
executor.start_polling(dp,skip_updates=True)