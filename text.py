# Import the required module for text to speech conversion
from aiogram import Bot, Dispatcher, executor, types # telegram bot module
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
import pyttsx3 # text to speech module
 
 
bot = Bot(token='6109751518:AAG45Q0qwX2M8QPTF_-G6QHrhb3xjjO-1D4')
dp = Dispatcher(bot)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)


#### voice selection
lang1 = KeyboardButton('/male')  
lang2 = KeyboardButton('/female')
lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(lang1).add(lang2)


#### sends welcome message after start
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Hello! Welcome to tastistus_bot! Please select a voice:', reply_markup = lang_kb)    


#### selecting male voice
@dp.message_handler(commands=['male'])
async def tts_male_handler(message: types.Message):
    engine.setProperty("voice", voices[0].id)  # Set the voice to a male voice
    text = "Please enter the text you want to convert to speech:"
    await message.answer(text)  # Prompt the user to enter text


#### selecting female voice
@dp.message_handler(commands=['female'])
async def tts_female_handler(message: types.Message):
    engine.setProperty("voice", voices[1].id)  # Set the voice to a female voice
    text = "Please enter the text you want to convert to speech:"
    await message.answer(text)  # Prompt the user to enter text


#### converting text to speech
@dp.message_handler()
async def text_input_handler(message: types.Message): # get message from what user types
    text = message.text
    engine.save_to_file(text, 'text.mp3') # save it as mp3
    engine.runAndWait()  
    with open("text.mp3", "rb") as voice:
        await bot.send_audio(chat_id=message.chat.id, audio=voice)  # Send the speech as a voice message


#### converting text file to speech
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(message: types.Message): # get message from the document that user sends
    file_id = message.document.file_id
    file = await bot.download_file_by_id(file_id) # save the txt
    with open('text.txt', 'wb') as f: 
        f.write(file.read())
    with open('text.txt', 'r') as f:
        text = f.read()
    engine.save_to_file(text, 'text.mp3') # save it as mp3
    engine.runAndWait()
    with open('text.mp3', 'rb') as voice:
        await bot.send_audio(chat_id=message.chat.id, audio=voice)  # Send audio file to user
            
            
# execute
executor.start_polling(dp, skip_updates=True)