#### import the required module
from aiogram import Bot, Dispatcher, executor, types # telegram bot module
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
import pyttsx3 # text to speech module
 
#### bot token 
bot = Bot(token='6109751518:AAG45Q0qwX2M8QPTF_-G6QHrhb3xjjO-1D4')
dp = Dispatcher(bot)

#### voice setting
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)

#### voice selection
lang1 = KeyboardButton('/Mark-🙋🏼‍♂️🇺🇸')
lang2 = KeyboardButton('/Sarah-🙋🏼‍♀️🇺🇸')
lang3 = KeyboardButton('/George-🙋🏼‍♂️🇬🇧')
lang4 = KeyboardButton('/Susan-🙋🏼‍♀️🇬🇧')
lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(lang1).add(lang2).add(lang3).add(lang4)

#### sends message after start
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Hello! Welcome to tastistus_bot! Please select a voice:', reply_markup = lang_kb)  
    
#### sends message after info
@dp.message_handler(commands=['info'])
async def welcome(message: types.Message):
    await message.answer('TEKNOLOGI MULTIMEDIA B | KELOMPOK 4\nWahyu Andhika Rizaldi - 5027211003\nAndreas Timotius Parhorasan Sihombing - 5027211019\nAndana Satrio Herdiansah - 5027211031\nRidho Husni Indrawan - 5027211043\nVira Datry Maulydina - 5027211050\nAnisa Ghina Salsabila - 5027211062')    
    
#### selecting mark voice
@dp.message_handler(commands=['Mark-🙋🏼‍♂️🇺🇸'])
async def tts_male_handler(message: types.Message):
    engine.setProperty("voice", voices[3].id)  # Set the voice to mark voice
    text = "Please enter the text you want to convert to speech:"
    await message.answer(text)  # Prompt the user to enter text
    
#### selecting sarah voice
@dp.message_handler(commands=['Sarah-🙋🏼‍♀️🇺🇸'])
async def tts_female_handler(message: types.Message):
    engine.setProperty("voice", voices[7].id)  # Set the voice to sarah voice
    text = "Please enter the text you want to convert to speech:"
    await message.answer(text)  # Prompt the user to enter text
    
#### selecting george voice
@dp.message_handler(commands=['George-🙋🏼‍♂️🇬🇧'])
async def tts_female_handler(message: types.Message):
    engine.setProperty("voice", voices[6].id)  # Set the voice to george voice
    text = "Please enter the text you want to convert to speech:"
    await message.answer(text)  # Prompt the user to enter text

#### selecting susan voice
@dp.message_handler(commands=['Susan-🙋🏼‍♀️🇬🇧'])
async def tts_female_handler(message: types.Message):
    engine.setProperty("voice", voices[2].id)  # Set the voice to susan voice
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
            
#### execute
executor.start_polling(dp, skip_updates=True)