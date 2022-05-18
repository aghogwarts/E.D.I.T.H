from disnake import CommandInteraction
from disnake.ext.commands import Bot, Cog, slash_command


class Help(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="help", description="A simple slash-help command.")
    async def help(self, inter: CommandInteraction) -> None:
        await inter.send(f"Pong! {self.bot.latency * 1000:.2f}ms")


def setup(bot: Bot) -> None:
    bot.add_cog(Help(bot))
