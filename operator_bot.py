# coding: utf-8
import os
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
        global operator_a
        global operatot_d
        s_mess = ""
        if message.author.bot:
            return
        print(message.author.mention,message.content.split())

        # random ope
        if message.content.split()[0] == "/set":
            if message.content.split()[1].isdecimal():
                member = np.arange(int(message.content.split()[1]))
                await message.channel.send('メンバーを'+message.content.split()[1]+"人にセットしました！")
            else:
                await message.channel.send("適切な値を入力して！")
                return

        elif '/at' in message.content:
            random.shuffle(operator_a)
            for op,mem in zip(operator_a,member):
                s_mess += str(mem)+" ---> "+op
            await message.channel.send(s_mess)
        elif '/df' in message.content:
            random.shuffle(operator_d)
            for op,mem in zip(operator_d,member):
                s_mess += str(mem)+" ---> "+op
            await message.channel.send(s_mess)
        else:
            await message.channel.send("適切な値を入力して！")
            return

        if len(member) == 0:
            await message.channel.send("メンバーがいません！")
            return


TOKEN = os.environ.get('DISC_TOKEN')
member = []
with open('ope_a.txt', 'r') as f:
    operetor_a = [line for line in f]
with open('ope_d.txt', 'r') as f:
    operetor_d = [line for line in f]
client.run(TOKEN)
