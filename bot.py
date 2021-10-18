import os
from dotenv.main import load_dotenv
from discord.ext import commands


def main():
    token = os.getenv("DISCORD_TOKEN")

    client = commands.Bot(command_prefix="+")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected")

    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")

    client.run(token)


if __name__ == "__main__":
    main()
