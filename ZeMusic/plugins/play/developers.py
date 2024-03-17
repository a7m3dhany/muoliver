import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["اوليفر","راغنار","المبرمج","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f72f51ac813d88b9ee301.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝗦𝗢𝗨𝗥𝗖𝗘 𝗢&𝗥](https://t.me/R1_O9)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @R1_O9 ❫
◉ 𝙸𝙳      : ❪ `2065633490` ❫
◉ 𝙱𝙸𝙾    : ❪ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗢&𝗥 (https://t.me/R1_O9) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗦𝗢𝗨𝗥𝗖𝗘 𝗢&𝗥", url=f"https://t.me/R1_O9"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗢&𝗥", url=f"https://t.me/R1_O9"),
                ],

            ]

        ),

    )
