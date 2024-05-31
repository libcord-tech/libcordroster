from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import pagify
import discord


async def has_update_command_role(ctx):
    """
    Checks if the user has the update command role.
    """
    if ctx.guild is None:
        return False
    uc_role = discord.utils.get(ctx.guild.roles, name="Update Command")
    reporter_role = discord.utils.get(ctx.guild.roles, name="Reporter")
    if uc_role is None:
        return False
    return (uc_role in ctx.author.roles) or (reporter_role in ctx.author.roles)


class LibcordRoster(commands.Cog):

    def __init__(self, bot: Red, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    def cog_unload(self):
        pass

    @commands.command()
    @commands.check(has_update_command_role)
    async def roster(self, ctx: commands.Context):
        """Get the names of all users with the Updating role"""
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Updating")
        members = [member for member in guild.members if role in member.roles]
        out = ""
        for member in members:
            if member.nick:
                out += f"{member.nick}\n"
            elif member.name:
                out += f"{member.name}\n"
        out = '\n'.join(sorted(out.splitlines(), key=str.lower))
        for page in pagify(out):
            await ctx.send("```\n" + page + "```")
