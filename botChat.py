import discord
import requests
import urllib.parse
from discord.ext import commands
from unidecode import unidecode

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
contador_montanha = 0
contador_cade = 0

def get_temperature(city):
    API_KEY = "Sua chave api"
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print("Complete URL:", complete_url)
    response = requests.get(complete_url)
    data = response.json()
    print("API Response:", data)

    if data["cod"] == "404":
        return None
    else:
        temperature = data["main"]["temp"]
        return temperature

@bot.event
async def on_ready():
    print("Nos logamos como {0.user}".format(bot))

@bot.event
async def on_message(message):
    print("Mensagem recebida:", message.content)
    global contador_montanha
    global contador_cade

    if message.author == bot.user:
        return
    
    content_lower = message.content.lower()
    
    if content_lower.startswith("!montanha"):
        contador_montanha += 1
        await message.channel.send("De novo a palavra {} foi falada em vão, a quantidade de vezes que já foi falada hoje foram: {}".format('"MONTANHA"', contador_montanha))
    
    elif content_lower.startswith("!cade"):
        contador_cade += 1
        await message.channel.send("De novo foi falado o {} a quantidade de vezes que já foi falada hoje foram: {}".format('"CADE"', contador_cade))
    
    elif message.content.startswith("!audio"):
        await message.channel.send(file = discord.File("uola.mp3"))
    
    elif content_lower.startswith("!temperatura"):
        args = content_lower.split(' ')
        if len(args) >= 2: 
            city = ' '.join(args[1:])  
            temperature = get_temperature(city)

            if temperature is not None:
                await message.channel.send("A temperatura atual em {} é de {}°C".format(city.capitalize(), temperature))
            else:
                await message.channel.send("Desculpe, não foi possível encontrar informações de temperatura para a cidade informada.")
        else:
            await message.channel.send("Uso incorreto! O comando deve ser !temperatura nome_da_cidade")


    elif content_lower.startswith("!epic"):
        await message.channel.send('Os jogos da epic de graça estão aqui: {}'.format("https://store.epicgames.com/pt-BR/free-games"))

bot.run("seutoken")

