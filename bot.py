from discord import Intents,Message,Client
import os
from dotenv import load_dotenv
load_dotenv()
from Components.response import get_response

Token = os.getenv("DISCORD_TOKEN")
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

Operator = "!"

async def send_message(ctx,user_message):
    if not user_message:
        print(f"Não foi possivel acessar a mensagem (Possivel falta de permissão)")
    
    response = get_response(user_message)
    await ctx.channel.send(response)

@client.event
async def on_ready():
    print(f"{client.user} está online")

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    
    username = ctx.author
    user_message = ctx.content
    channel = ctx.channel

    if user_message[0] == Operator:
        user_message = user_message[1:]
        print(f"{username}: {user_message} ({channel})")
        await send_message(ctx,user_message)


def main():
    client.run(Token)

if __name__ == "__main__":
    main()