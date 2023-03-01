import discord
import random

bad_words = ["блять", "сука", "бля"]


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content in bad_words:
            reply_list = ["Shut fuck up!", "Fuck you", "Do not talk"]
            await message.reply(random.choice(reply_list))


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
