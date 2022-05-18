import disnake
from disnake.ext.commands import Bot

import os
import logging
import platform

from dotenv import load_dotenv
from os import environ as env


load_dotenv()

intents = disnake.Intents.all()
DEFAULTPREFIX = "ed"

bot = Bot(
    command_prefix={DEFAULTPREFIX},
    case_insensitive=True,
    owner_id=760426797418151937,
    help_command=None,
    intents=intents,
    AllowedMentions=False,
)

bot.version = "1.0"

bot.colors = {
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xFFB500,
    "RED": 0xE74C3C,
}
bot.color_list = [c for c in bot.colors.values()]

logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():

    # Collect stat data on firing up the bot and make it a global var
    global pythonVersion, disnakeVersion, serverCount, memberCount
    pythonVersion = platform.python_version()
    disnakeVersion = disnake.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))

    # On ready, print some details to standard out
    print(
        f"\n\n{'='*30}\n\nReady to Deploy\n\n- Stats :\nCurrently in {serverCount} servers\nWatching over {memberCount} users\n\n- Running on :\nDisnake v{disnakeVersion}\nPython {pythonVersion}\n\n{'='*30}\n"
    )

    # Change the bot's activity
    await bot.change_presence(
        activity=disnake.Activity(
            type=disnake.ActivityType.watching, name="over Hub of Football"
        ),
        status=disnake.Status.dnd,
    )


@bot.event
async def on_message(message):

    # Ignore messages sent by the bot
    if message.author.bot:
        return

    # Whenever the bot is tagged, respond with its prefix
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(
        f"<@!{bot.user.id}>"
    ):
        await message.reply(
            f"<:frogeez:879789528511025214> Need any help? My prefix is `/`and you can do `/help` to see a list of all the commands programmed in my System",
            delete_after=15,
            mention_author=False,
        )


bot.load_extensions("./ext")

bot.run(env["TOKEN"])

"""
TODO:
    - Try to make on_ready print with colorama cause looks cool :)
"""
