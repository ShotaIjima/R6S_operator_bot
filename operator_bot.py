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
    a_mess = ""
    if message.author.bot:
        return
    print(message.author.mention,message.content.split())
    if message.content.split()[0] == "/set":
        if message.content.split()[1].isdecimal():
            member = np.arange(int(message.content.split()[1]))
            await message.channel.send('メンバーを'+message.content.split()[1]+"人にセットしました！")
            return
        else:
            await message.channel.send("適切な値を入力して！")
            return
    elif len(member) == 0:
        await message.channel.send("メンバーがいません！")
        return
    elif message.content == '/ata':
        for i in range(1,6,2):
            if i == 5:
                a_mess += "延長ラウンド_A\n"
            else:
                a_mess += "ラウンド"+str(i)+"_A\n"
            random.shuffle(operator_a)
            a_mess += make_mess(operator_a,member)
            if i == 5:
                a_mess += "延長ラウンド_D\n"
            else:
                a_mess += "ラウンド"+str(i+1)+"_D\n"
            random.shuffle(operator_d)
            a_mess += make_mess(operator_d,member)
        await message.channel.send(a_mess)
    elif message.content == '/dfa':
        for i in range(1,6,2):
            if i == 5:
                a_mess += "延長ラウンド_D\n"
            else:
                a_mess += "ラウンド"+str(i)+"_D\n"
            random.shuffle(operator_d)
            a_mess += make_mess(operator_d,member)
            if i == 5:
                a_mess += "延長ラウンド_A\n"
            else:
                a_mess += "ラウンド"+str(i+1)+"_A\n"
            random.shuffle(operator_a)
            a_mess += make_mess(operator_a,member)
        await message.channel.send(a_mess)
    elif message.content == '/at':
        random.shuffle(operator_a)
        await message.channel.send(make_mess(operator_a,member))
    elif message.content == '/df':
        random.shuffle(operator_d)
        await message.channel.send(make_mess(operator_d,member))
    else:
        await message.channel.send("適切な値を入力して！")
        return

def make_mess(operator,member):
    s_mess = ""
    for op,mem in zip(operator,member):
        s_mess += str(mem)+" ---> "+op
    s_mess += "\n"
    return s_mess

with open('ope_a.txt', 'r') as f:
    operator_a = [line for line in f]
with open('ope_d.txt', 'r') as f:
    operator_d = [line for line in f]
member = []
TOKEN = os.environ.get('DISC_TOKEN')
client.run(TOKEN)
