from discord.ext import commands
import random


class Random(commands.Cog, name="Random"):
    """Return random number"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context, n1: str = None, n2: str = None):
        """Rolls a given amount of dice

        Example 1: +roll -> random number from 1 to 100
        Example 2: +roll 54 -> random number from 1 to 54
        Example 3: +roll 60 - 160 -> random number from 60 to 160
        """
        try:
            if n1 == None:
                await ctx.send(random.randint(1, 100))
            elif n2 == None:
                await ctx.send(random.randint(1, int(n1)))
            else:
                await ctx.send(random.randint(int(n1), int(n2)))
        except ValueError:
            await ctx.send("Value must be a positive number")


def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))
