# bot.py
import os
import random
import requests
import json
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Chào mừng đã tới server discord của tao1!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content)
    # Call API for reply beautifull girl
    if message.content == '-girl':
        response = requests.get('https://ketnoi-28.000webhostapp.com/fl_img/index.php#74v26343x2p2u2e4a4u2v2f4t22403v2')
        results = response.json()
        messages = results['messages']
        attact = messages[0]
        url = attact['attachment']['payload']['url']
        await message.channel.send(url)
    # Call API for reply time to sleep
    if message.content.startswith('-wake'):
        timer = message.content
        response = requests.get('https://blogsvhaui.000webhostapp.com/chatFuel/sleepyTime/time-wake.php?time-wake=%s wake' % timer[6:])
        results = response.json()
        messages = results['messages']
        text = messages[0]
        realtext = text['text']
        await message.channel.send(realtext)
    # Call API for cung hoang dao
    if message.content.startswith('-cung'):
        cung_hoang_dao = message.content
        response = requests.get('https://api.kma-chatbot.com/cunghoangdao.php?cung=%s' % cung_hoang_dao[6:])
        results = response.json()
        messages = results['messages']
        text = messages[0]
        realtext = text['text']
        await message.channel.send(realtext)
    if message.content.startswith('-cat'):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        results = response.json()
        JSON_Find = results[0]
        url = JSON_Find['url']
        print(url)
        await message.channel.send(url)

    if message.content.startswith('-predict'):
        Picture = message.content

        from clarifai.rest import ClarifaiApp
        # Get Free API KEY on Clarifai
        app = ClarifaiApp(api_key='API KEY')
        model = app.public_models.general_model
        response = model.predict_by_url(Picture[9:])
        find = response['outputs'][0]['data']['concepts']
        for x in find:
            print(str(x['name']) + ' Khả năng chính xác: ' + (str(x['value'])[0:4]))
            await message.channel.send(str(x['name']) + ' Khả năng chính xác: ' + (str(x['value'])[0:4]))
    
    
client.run(token)


