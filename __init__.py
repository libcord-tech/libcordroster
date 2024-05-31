from redbot.core.bot import Red
from .libcordroster import LibcordRoster


async def setup(bot: Red):
    cog = LibcordRoster(bot)
    await bot.add_cog(cog)
