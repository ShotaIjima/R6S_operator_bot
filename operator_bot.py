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
    if message.author.bot:
        return
    print(message.author.mention,message.content.split())
    if message.content.split()[0] == "/set":
        if message.content.split()[1].isdecimal():
            member = np.arange(int(message.content.split()[1]))
            await message.channel.send('メンバーを'+message.content.split()[1]+"人にセットしました！")
        else:
            await message.channel.send("適切な値を入力して！")
            return
    elif '/at' in message.content:
        random.shuffle(operator_a)
        await message.channel.send(make_mess(operator_a,member))
    elif '/df' in message.content:
        random.shuffle(operator_d)
        await message.channel.send(make_mess(operator_d,member))
    else:
        await message.channel.send("適切な値を入力して！")
        return

    if len(member) == 0:
        await message.channel.send("メンバーがいません！")
        return

def make_mess(operator,member):
    s_mess = ""
    for op,mem in zip(operator,member):
        s_mess += str(mem)+" ---> "+op
    return s_mess

TOKEN = os.environ.get('DISC_TOKEN')
with open('ope_a.txt', 'r') as f:
    operator_a = [line for line in f]
with open('ope_d.txt', 'r') as f:
    operator_d = [line for line in f]
client.run(TOKEN)
