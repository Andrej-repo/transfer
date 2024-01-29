from app import bot
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import Router
from database import users
from aiogram import F
from aiogram.types import BufferedInputFile
from model import image_data
import os

router = Router()
@router.message(Command("transfer_style"))
async def cmd_transfer_style(message: Message):
    await message.answer("Загрузите фото, в котором хотите поменять стиль")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Выберите в меню команду transfer_style и следуйте инструкции")

@router.message(F.photo)
async def cmd_photo1(message:Message):
    if message.chat.id in users:
        file2 = await bot.get_file(message.photo[-1].file_id)
        photo2 = await bot.download(file2)
        users[message.chat.id].append(photo2)
        await message.answer('Дождитесь выполнения программы')
        img = image_data(users[message.chat.id])
        img.save(f'image{message.chat.id}.png')
        with open(f'image{message.chat.id}.png', 'rb') as file:
            input_file = BufferedInputFile(file.read(), 'any_filename')
        file_path = f'image{message.chat.id}.png'
        if os.path.exists(file_path):
            os.remove(file_path)
        await message.answer_photo(photo=input_file, caption='ваше обработанное фото')
        del users[message.chat.id]


    else:
        file1 = await bot.get_file(message.photo[-1].file_id)
        photo1 = await bot.download(file1)
        users[message.chat.id] = [photo1]
        await message.answer('Загрузите фото со стилем')
