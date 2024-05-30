from config import token
from aiogram import Dispatcher,types,Bot,executor
from logging import basicConfig, INFO


bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [types.KeyboardButton('О нас'),
                 types.KeyboardButton('Товары'),
                 types.KeyboardButton('Заказать'),
                 types.KeyboardButton('Контакты')]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply(f"Здравствуйте,{message.from_user.full_name}!",reply_markup=start_keyboard)
    
@dp.message_handler(text='О нас')
async def about_as(message:types.Message):
    await message.reply("Интернет Магазин TECHSHOP.KG Цены не актуальны! Уточняйте! КУПИТЬ. Покупайте по выгодным ценам. ДоставкаВсего 200 сом по городу! Рассрочка Товары в рассрочку. Кредит Возьми в кредит!")

tovars =[types.KeyboardButton('Водонагреватель EDISSON ER 100 V'),  
        types.KeyboardButton('Xiaomi Mi A2 Lite 3'),
        types.KeyboardButton('Бритва BRAUN 300S RED'),
        types.KeyboardButton('Чайник электрический VITEK VT-1122 TR стекло'),
]

tovar_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*tovars)

@dp.message_handler(text="Товары")
async def all_courses(message:types.Message):
    await message.answer("Вот наши товары:", reply_markup=tovar_keyboard)

@dp.message_handler(text='Водонагреватель EDISSON ER 100 V')
async def about_as(message:types.Message):
    await message.answer_photo("https://i0.wp.com/techshop.kg/wp-content/uploads/2018/09/1999b5d04742a3441894e53ce0687621.jpg?zoom=1.2625000476837158&fit=350%2C500&ssl=1")
    await message.answer("Водонагреватель EDISSON ER 100 V = Накопительный водонагреватель EDISSON ER 100 V – это современный бытовой электрический бойлер, исполненный из качественных и долговечных материалов и представленный в компактном и элегантном корпусе с европейским дизайном. Прибор вмещает 100 л воды, и способен обеспечить горячей водой в любое время всю семью дома, в саду или на даче. Он обладает высокой мощностью нагревания в 1,5 кВт. Время, которое требуется для достижения максимально возможной температуры жидкости в 75°С, составляет примерно 2,5 часа. Давление воды варьируется от 0,5 до 6 атмосфер. Внутренняя часть бака покрыта эмалированной сталью, а корпус произведен из долговечной эмалированной стали. Модель оснащена трубчатым нагревательным элементом, который является самым надежным при эксплуатации. Встроенная функция “Автоотключение” срабатывает при достижении предельной температуры. Включается прибор сам по мере необходимости, то есть при остывании воды. За безопасность отвечают функция ограничения температуры нагрева и обратный клапан. Крепится прибор к стене строго в вертикальном положении. Подводка трубы осуществляется только с нижней стороны.")
    await message.answer("8.037 сом")
    await message.answer("https://techshop.kg/product/%d0%b2%d0%be%d0%b4%d0%be%d0%bd%d0%b0%d0%b3%d1%80%d0%b5%d0%b2%d0%b0%d1%82%d0%b5%d0%bb%d1%8c-edisson-er-100-v/")

@dp.message_handler(text='Xiaomi Mi A2 Lite 3')
async def about_as(message:types.Message):
    await message.answer_photo("https://i1.wp.com/techshop.kg/wp-content/uploads/2018/09/2Mi-A2.jpg?zoom=1.2625000476837158&fit=1750%2C1000&ssl=1")
    await message.reply("Xiaomi Mi A2 Lite — бюджетный смартфон с безрамочным дизайном и «монобровью». Его отличительной особенностью представляется наличие платформы Android One от Google. Анонс данного гаджета состоялся в июле 2018 года.")
    await message.answer("10,580 сом")
    await message.answer("https://techshop.kg/product/xiaomi-mi-a2-lite/")
    
@dp.message_handler(text='Бритва BRAUN 300S RED')
async def about_as(message:types.Message):
    await message.answer_photo("https://i2.wp.com/techshop.kg/wp-content/uploads/2018/09/series-3-300s-red-1000x1000.jpg?zoom=1.2625000476837158&fit=1000%2C1000&ssl=1")
    await message.reply("В новой линейке бритв Braun Series 3 компания Braun представила свою технологию MicroComb. Она включает два ряда тонких равномерных лезвий, окружающих независимо двигающийся промежуточный триммер. Эта технология захватывает и срезает большее количество волосков каждым движением, что обеспечивает более быстрое бритье. Различие с другими бритвами значительное, особенно при испытании бритвы на жесткой 3-дневной щетине.Тройная бритвенная система. Идеальная работа двух сеточек и встроенный независимо двигающийся промежуточный триммер с технологией MicroComb обеспечивают более гладкое бритье. Вместе они эффективно срезают длинные и короткие волоски каждым движением — испытано даже на жесткой 3-дневной щетине.")
    await message.answer("3,900 сом")
    await message.answer("https://techshop.kg/product/%d0%b1%d1%80%d0%b8%d1%82%d0%b2%d0%b0-braun-300s-red/")
    
@dp.message_handler(text='Чайник электрический VITEK VT-1122 TR стекло')
async def about_as(message:types.Message):
    await message.answer_photo("https://i0.wp.com/techshop.kg/wp-content/uploads/2018/09/ecxHOoPrt95e44BXThuIg.jpg?zoom=1.2625000476837158&fit=394%2C515&ssl=1")
    await message.reply("Чайник VITEK VT-1122 TR станет стильным дополнением вашей кухни и секретом вашего вкусного чая. Доверьтесь прибору и спокойно готовьте завтрак: прибор автоматически выключится при закипании, отсутствии воды и перегреве.")
    await message.answer("2,227 сом")
    await message.answer("https://techshop.kg/product/%d1%87%d0%b0%d0%b9%d0%bd%d0%b8%d0%ba-%d1%8d%d0%bb%d0%b5%d0%ba%d1%82%d1%80%d0%b8%d1%87%d0%b5%d1%81%d0%ba%d0%b8%d0%b9-vitek-vt-1122-tr-%d1%81%d1%82%d0%b5%d0%ba%d0%bb%d0%be/")

@dp.message_handler(text='Контакты')
async def send_contact(message:types.Message):
    await message.answer(f"{message.from_user.first_name},наши контакты ")
    await message.answer_contact("+996 777326080,""Tech","shop")
    await message.answer_contact("+996 555507503,""Tech","shop")
    # await bot.send_message(-4269502098, )

spicok = ['https://techshop.kg/product/%d0%b2%d0%be%d0%b4%d0%be%d0%bd%d0%b0%d0%b3%d1%80%d0%b5%d0%b2%d0%b0%d1%82%d0%b5%d0%bb%d1%8c-edisson-er-100-v/','https://techshop.kg/product/xiaomi-mi-a2-lite/','https://techshop.kg/product/%d0%b1%d1%80%d0%b8%d1%82%d0%b2%d0%b0-braun-300s-red/','https://techshop.kg/product/%d1%87%d0%b0%d0%b9%d0%bd%d0%b8%d0%ba-%d1%8d%d0%bb%d0%b5%d0%ba%d1%82%d1%80%d0%b8%d1%87%d0%b5%d1%81%d0%ba%d0%b8%d0%b9-vitek-vt-1122-tr-%d1%81%d1%82%d0%b5%d0%ba%d0%bb%d0%be/']

@dp.message_handler(text='Заказать')
async def send_zakazat(message:types.Message):
    await message.answer(f"Введите ссылку на товар:")
@dp.message_handler()
async def number_handler(message: types.Message):
                print(True)
                if message:
                    user_number = (message.text)
                    print(user_number)
                    # if spicok in user_number:
                    for i in spicok:
                        if i == user_number:
                            print(True)
                            await bot.send_message( -4269502098,f'Ссылка на товар: {user_number}')
                            contact_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Отправить контакт', request_contact=True))
                            await message.reply('Ссылка отправлена', reply_markup=contact_button)
                            
@dp.message_handler(text="Отправить контакт")
async def aplication(message:types.Message):
    print(True)
    button = types.KeyboardButton("Отправить контакт",request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button)
    
    await message.answer("Пожалуйста отправьте свой контакт",reply_markup=keyboard)
    
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_start(message:types.Message):
    await bot.send_message( -4269502098,f"Контакт:\nИмя:{message.contact.first_name}\nФамилия:{message.contact.last_name}\nphone_number:{message.contact.phone_number}\n")
    await message.answer("Спасибо за покупку")
    await start(message)
    
executor.start_polling(dp)






    