# coding: utf-8
import discord
import random
import numpy as np

client = discord.Client()

@client.event
async def on_ready():
    print('ログイン')

@client.event
async def on_message(message):
        global member
        global operetor_a
        global operetot_d
        s_mess = ""
        if message.author.bot:
            return
        print(message.author.mention,message.content.split())
        if 'リージョン' in message.content:
            await message.channel.send('いぐぱい')
            return
        if "@312972540907880449" in message.author.mention:
            await message.channel.send('お前リージョンだな？？')

        # random ope
        if message.content.split()[0] == "/set":
            if message.content.split()[1].isdecimal():
                member = np.arange(int(message.content.split()[1]))
                await message.channel.send('メンバーを'+message.content.split()[1]+"人にセットしました！")
            else:
                await message.channel.send("適切な値を入力して！")
                return

        elif '/at' in message.content:
            random.shuffle(operetor_a)
            for op,mem in zip(operetor_a,member):
                s_mess += str(mem)+" ---> "+op
            await message.channel.send(s_mess)
        elif '/df' in message.content:
            random.shuffle(operetor_d)
            for op,mem in zip(operetor_d,member):
                s_mess += str(mem)+" ---> "+op
            await message.channel.send(s_mess)
        else:
            await message.channel.send("適切な値を入力して！")
            return

        if len(member) == 0:
            await message.channel.send("メンバーがいません！")
            return


TOKEN = "NTc0NDM2MzM2NjY5NDI1Njg3.XM5Xog.klfidIQI731FJgXY7wkvY2p21Lg"
member = []
with open('ope_a.txt', 'r') as f:
    operetor_a = [line for line in f]
with open('ope_d.txt', 'r') as f:
    operetor_d = [line for line in f]
client.run(TOKEN)

