


#Pokemon

import discord
import random
from discord.embeds import Embed
from discord.ext import commands, tasks
from random import choice
from flask import Flask
from threading import Thread
from webserver import keep_alive
import os 
import asyncio
import requests

from discord.ext.commands.core import command


client = commands.Bot( command_prefix = '?' )

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' PokéMedia/Prefix (?)'))
    print(' Bot iS Online ')






from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return  "Your Bot Is Ready"

def run():
    app.run(host="0.0.0.0", port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()
























#ping 

@client.command(aliases=['Ping','PING'],help='Latency')
async def ping(ctx):
    
    message= await ctx.send('🔌`Intialising connection...`')
    await message.edit(content="🛠️`Processing...`")
    await message.edit(content=f'🟢 **Pong!  {round(client.latency *1000)}ms**')
#pokemon

URL_API = 'https://pokeapi.co/api/v2/pokemon/'

#pokemon
@client.command()
async def pokemon(ctx, *, args):
  
    pokeName = args.lower()
    try:
        r = requests.get(f'{URL_API}{pokeName}')
        packages_json = r.json()
        packages_json.keys()

        embed = discord.Embed(title="Pokemon", color=discord.Color.random())
        embed.add_field(name="Name", value=packages_json['name'], inline=True)
        embed.add_field(name="Pokedex Order", value=packages_json['order'], inline=False)

        embed.set_thumbnail(url= f'https://play.pokemonshowdown.com/sprites/ani/{pokeName}.gif')     
        embed.add_field(name="Weight (kg)", value=packages_json['weight']/10, inline=False)
        embed.add_field(name="Height (m)", value=packages_json['height']/10, inline=False)
   
        embed.add_field(name="Base XP", value=packages_json['base_experience'], inline=False)
        for type in packages_json['types']: #FOR TO GET A TYPE OF A POKEMON
            embed.add_field(name="Types", value= type['type']['name'], inline=False)
        embed.set_footer(text=f"Requested by {ctx.author} , v1.0.2", icon_url=ctx.author.avatar_url )
        await ctx.send(embed=embed)
    except:
        await ctx.send("Pokemon not found!")

#001

@client.command()
async def Bulbasaur(ctx):
    embed = discord.Embed(title="Pokemon #001", description="**Bulbasaur**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    
    embed.set_image(url='https://serebii.net/swordshield/pokemon/001.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#002

@client.command()
async def Ivysaur(ctx):
    embed = discord.Embed(title="Pokemon #002", description="**Ivysaur**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://serebii.net/swordshield/pokemon/002.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)

#003

@client.command()
async def Venusaur(ctx):
    embed = discord.Embed(title="Pokemon #003", description="**Venusaur**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://serebii.net/swordshield/pokemon/003.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#003 Mega
     
@client.command()
async def MegaVenusaur(ctx):
    embed = discord.Embed(title="Pokemon #003 Mega", description="**Mega Venusaur**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867652678887800852/003_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#003 Gigantamax

@client.command()
async def GigantamaxVenusaur(ctx):
    embed = discord.Embed(title="Pokemon #003 Gigantamax", description=" **Gigantamax Venusaur**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867654474469343262/003_f3.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#004 

@client.command()
async def Charmander(ctx):
    embed = discord.Embed(title="Pokemon #004", description=" **Charmander**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867658698327195698/004.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#005

@client.command()
async def Charmeleon(ctx):
    embed = discord.Embed(title="Pokemon #005", description=" **Charmeleon**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867659221047050270/005.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#006

@client.command()
async def Charizard(ctx):
    embed = discord.Embed(title="Pokemon #006", description=" **Charizard**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire/Flying")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867662264928829490/006.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#006 Mega X

@client.command()
async def MegaCharizardX(ctx):
    embed = discord.Embed(title="Pokemon #006 Mega X", description=" **Mega Charizard X**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire/Dragon")
    embed.add_field(name="Weaknesses", value= "Ground/Rock/Dragon")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867663657500147732/006_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#006 Mega Y

@client.command()
async def MegaCharizardY(ctx):
    embed = discord.Embed(title="Pokemon #006 Mega Y", description=" **Mega Charizard Y**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire/Flying")
    embed.add_field(name="Weaknesses", value= "Water/Electric/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867665625023381574/006_f3.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#006 Gigantamax


@client.command()
async def GigantamaxCharizard(ctx):
    embed = discord.Embed(title="Pokemon #006 Gigantamax", description=" **Gigantaxmax Charizard **", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire/Flying")
    embed.add_field(name="Weaknesses", value= "Water/Electric/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867666729123708929/006_f4.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#007


@client.command()
async def Squirtle(ctx):
    embed = discord.Embed(title="Pokemon #007", description=" **Squirtle**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867668406537682984/007.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#008


@client.command()
async def Wartortle(ctx):
    embed = discord.Embed(title="Pokemon #008", description=" **Wartortle**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867669462931734548/008.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#009

@client.command()
async def Blastoise(ctx):
    embed = discord.Embed(title="Pokemon #009", description=" **Blastoise**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867670898327814174/009.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#009 Mega

@client.command()
async def MegaBlastoise(ctx):
    embed = discord.Embed(title="Pokemon #009 Mega", description=" ** Mega Blastoise**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867672223866945536/009_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#009 Gigantamax


@client.command()
async def GigantamaxBlastoise(ctx):
    embed = discord.Embed(title="Pokemon #009 Gigantamax", description=" ** Gigantamax Blastoise**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867673046244524072/009_f3.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#010


@client.command()
async def Caterpie(ctx):
    embed = discord.Embed(title="Pokemon #010", description=" **Caterpie**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867674938629423134/010.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#011

@client.command()
async def Metapod(ctx):
    embed = discord.Embed(title="Pokemon #011", description=" **Metapod**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867675861293858856/011.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#012


@client.command()
async def Butterfree(ctx):
    embed = discord.Embed(title="Pokemon #012", description=" **Butterfree**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Flying")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock/Electric/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867676470670655488/012.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#012 Gigantamax

@client.command()
async def GigantamaxButterfree(ctx):
    embed = discord.Embed(title="Pokemon #012 Gigantamax", description=" ** Gigantamax Butterfree**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Flying")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock/Electric/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867679479845486613/012_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#013

@client.command()
async def Weedle(ctx):
    embed = discord.Embed(title="Pokemon #013", description=" **Weedle**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock/Psychic")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867689132133974026/013.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#014

@client.command()
async def Kakuna(ctx):
    embed = discord.Embed(title="Pokemon #014", description=" **Kakuna**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock/Psychic")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867690464816005200/014.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#015

@client.command()
async def Beedrill(ctx):
    embed = discord.Embed(title="Pokemon #015", description=" **Beedrill**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock/Psychic")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867694827923701760/015.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#015 Mega

@client.command()
async def MegaBeedrill(ctx):
    embed = discord.Embed(title="Pokemon #015 Mega", description=" **Mega Beedrill**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Rock/Psychic")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867694935523065856/015_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#016

@client.command()
async def Pidgey(ctx):
    embed = discord.Embed(title="Pokemon #016", description=" ** Pidgey**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Flying")
    embed.add_field(name="Weaknesses", value= "Electric/Rock/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867696726819602442/016.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#017

@client.command()
async def Pidgeotto(ctx):
    embed = discord.Embed(title="Pokemon #017", description=" **Pidgeotto**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Flying")
    embed.add_field(name="Weaknesses", value= "Electric/Rock/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867697087343886376/017.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#018

@client.command()
async def Pidgeot(ctx):
    embed = discord.Embed(title="Pokemon #018", description=" **Pidgeot**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Flying")
    embed.add_field(name="Weaknesses", value= "Electric/Rock/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867697216890208296/018.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#018 Mega

@client.command()
async def MegaPidgeot(ctx):
    embed = discord.Embed(title="Pokemon #018 Mega", description=" **Mega Pidgeot**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Flying")
    embed.add_field(name="Weaknesses", value= "Electric/Rock/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867697932752125962/018_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)

#019

@client.command()
async def Rattata(ctx):
    embed = discord.Embed(title="Pokemon #019", description=" **Rattata**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal")
    embed.add_field(name="Weaknesses", value= "Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867699941739724800/019.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#019 Alolan

@client.command()
async def AlolanRattata(ctx):
    embed = discord.Embed(title="Pokemon #019 Alolan", description=" ** Alolan Rattata**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Dark")
    embed.add_field(name="Weaknesses", value= "Fairy/Bug/Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867702003174080522/019_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#020

@client.command()
async def Raticate(ctx):
    embed = discord.Embed(title="Pokemon #020", description=" **Raticate**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal")
    embed.add_field(name="Weaknesses", value= "Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867703045190057994/020.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#020 Alolan

@client.command()
async def AlolanRaticate(ctx):
    embed = discord.Embed(title="Pokemon #020 Alolan", description=" ** Alolan Raticate**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Dark")
    embed.add_field(name="Weaknesses", value= "Fairy/Bug/Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/867703530981949450/020_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#021


@client.command()
async def Spearow(ctx):
    embed = discord.Embed(title="Pokemon #021", description=" **Spearow**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Flying")
    embed.add_field(name="Weaknesses", value= "Electric/Rock/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867953847195295804/021.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#022


@client.command()
async def Fearow(ctx):
    embed = discord.Embed(title="Pokemon #022", description=" **Fearow**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Flying")
    embed.add_field(name="Weaknesses", value= "Electric/Rock/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867954507391336458/022.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#023


@client.command()
async def Ekans(ctx):
    embed = discord.Embed(title="Pokemon #023", description=" **Ekans**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison")
    embed.add_field(name="Weaknesses", value= "Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867955409028268032/023.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#024


@client.command()
async def Arbok(ctx):
    embed = discord.Embed(title="Pokemon #024", description=" **Arbok**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison")
    embed.add_field(name="Weaknesses", value= "Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867955457287917638/024.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)






#025


@client.command()
async def Pikachu(ctx):
    embed = discord.Embed(title="Pokemon #025", description=" **Pikachu**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Electric")
    embed.add_field(name="Weaknesses", value= "Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867957987988353074/025.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#025 Gigantamax


@client.command()
async def GigantamaxPikachu(ctx):
    embed = discord.Embed(title="Pokemon #025 Gigantamax", description=" ** Gigantamax Pikachu **", color=discord.Color.random())
    embed.add_field(name="Types", value= "Electric")
    embed.add_field(name="Weaknesses", value= "Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867959076112461915/025_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#026


@client.command()
async def Raichu(ctx):
    embed = discord.Embed(title="Pokemon #026", description=" **Raichu**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Electric")
    embed.add_field(name="Weaknesses", value= "Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867959628074483772/026.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#026 ALolan


@client.command()
async def AlolanRaichu(ctx):
    embed = discord.Embed(title="Pokemon #026 Alolan", description=" **Alolan Raichu**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Electric/Psychic")
    embed.add_field(name="Weaknesses", value= "Ghost/Dark/Bug/   Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867959666846609549/026_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#027


@client.command()
async def Sandshrew(ctx):
    embed = discord.Embed(title="Pokemon #027", description=" **Sandshrew**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ground")
    embed.add_field(name="Weaknesses", value= "Water/Grass/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867962436337147954/027.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#027 Alolan 


@client.command()
async def AlolanSandshrew(ctx):
    embed = discord.Embed(title="Pokemon #027 Alolan", description=" ** Alolan Sandshrew**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ice/Steel")
    embed.add_field(name="Weaknesses", value= "Fire/Fighting/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867962470734651402/027_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#028


@client.command()
async def Sandslash(ctx):
    embed = discord.Embed(title="Pokemon #028", description=" **Sandslash**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ground")
    embed.add_field(name="Weaknesses", value= "Water/Grass/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867966668767371264/028.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#028 Alolan 


@client.command()
async def AlolanSandslash(ctx):
    embed = discord.Embed(title="Pokemon #027 Alolan", description=" ** Alolan Sandslash**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ice/Steel")
    embed.add_field(name="Weaknesses", value= "Fire/Fighting/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/867966704850993192/028_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#029 

@client.command()
async def Nidoran(ctx):
    embed = discord.Embed(title="Pokemon #029", description=" **Nidoran ♀ **", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison")
    embed.add_field(name="Weaknesses", value= "Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868038062326812722/029.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#030

@client.command()
async def Nidorina(ctx):
    embed = discord.Embed(title="Pokemon #030", description=" **Nidorina**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison")
    embed.add_field(name="Weaknesses", value= "Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/868039106725281792/030.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#031

@client.command()
async def Nidoqueen(ctx):
    embed = discord.Embed(title="Pokemon #031", description=" **Nidoqueen**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison/Ground")
    embed.add_field(name="Weaknesses", value= "Water/Ice/Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868039516059996180/031.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#032

@client.command()
async def NidoranMale(ctx):
    embed = discord.Embed(title="Pokemon #032", description=" **Nidoran ♂  **", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison")
    embed.add_field(name="Weaknesses", value= "Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868041386191097886/032.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#033

@client.command()
async def Nidorino(ctx):
    embed = discord.Embed(title="Pokemon #033", description=" **Nidorino**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison")
    embed.add_field(name="Weaknesses", value= "Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/868041417623232523/033.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#034

@client.command()
async def Nidoking(ctx):
    embed = discord.Embed(title="Pokemon #034", description=" **Nidoking**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison/Ground")
    embed.add_field(name="Weaknesses", value= "Water/Ice/Psychic/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/868041450028400640/034.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#035

@client.command()
async def Clefairy(ctx):
    embed = discord.Embed(title="Pokemon #035", description=" **Clefairy**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fairy")
    embed.add_field(name="Weaknesses", value= "Steel/Poison")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868346044184928276/035.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)





#036

@client.command()
async def Clefable(ctx):
    embed = discord.Embed(title="Pokemon #036", description=" **Clefable**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fairy")
    embed.add_field(name="Weaknesses", value= "Steel/Poison")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868346715701407744/036.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#037

@client.command()
async def Vulpix(ctx):
    embed = discord.Embed(title="Pokemon #037", description=" **Vulpix**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868347336097660968/037.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#037 Alolam

@client.command()
async def AlolanVulpix(ctx):
    embed = discord.Embed(title="Pokemon #037 Alolan", description=" ** Alolan Vulpix**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ice")
    embed.add_field(name="Weaknesses", value= "Fire/Steel/Fighting/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868348224539353098/037_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#038

@client.command()
async def Ninetales(ctx):
    embed = discord.Embed(title="Pokemon #038", description=" **Ninetales**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fire")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868348722231259146/038.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#038 Alolam

@client.command()
async def AlolanNinetales(ctx):
    embed = discord.Embed(title="Pokemon #038 Alolan", description=" ** Alolan Ninetales**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ice")
    embed.add_field(name="Weaknesses", value= "Fire/Steel/Fighting/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868349387393339412/038_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#039

@client.command()
async def Jigglypuff(ctx):
    embed = discord.Embed(title="Pokemon #039", description=" **Jigglypuff**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Fairy")
    embed.add_field(name="Weaknesses", value= "Steel/Poison")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868349913237446746/039.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#040

@client.command()
async def Wigglytuff(ctx):
    embed = discord.Embed(title="Pokemon #040", description=" **Wigglytuff**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal/Fairy")
    embed.add_field(name="Weaknesses", value= "Steel/Poison")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868349969814392852/040.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#041

@client.command()
async def Zubat(ctx):
    embed = discord.Embed(title="Pokemon #041", description=" **Zubat**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison/Flying")
    embed.add_field(name="Weaknesses", value= "Psychic/Electric/Ice/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868352614423748638/041.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#042

@client.command()
async def Golbat(ctx):
    embed = discord.Embed(title="Pokemon #042", description=" **Golbat**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Poison/Flying")
    embed.add_field(name="Weaknesses", value= "Psychic/Electric/Ice/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868352670572900392/042.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#043

@client.command()
async def Oddish(ctx):
    embed = discord.Embed(title="Pokemon #043", description=" **Oddish**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868355478265155624/043.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#044

@client.command()
async def Gloom(ctx):
    embed = discord.Embed(title="Pokemon #044", description=" **Gloom**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868355514671726612/044.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#045

@client.command()
async def Vileplume(ctx):
    embed = discord.Embed(title="Pokemon #045", description=" **Vileplume**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Psychic/Flying/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868355570422403072/045.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#046

@client.command()
async def Paras(ctx):
    embed = discord.Embed(title="Pokemon #046", description=" **Paras**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Bug")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Ice/Poison/Rock/Bug")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868357769579864094/046.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#047

@client.command()
async def Parasect(ctx):
    embed = discord.Embed(title="Pokemon #047", description=" **Parasect**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Grass/Bug")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Ice/Poison/Rock/Bug")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868357874785599518/047.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#048

@client.command()
async def Venonat(ctx):
    embed = discord.Embed(title="Pokemon #048", description=" **Venonat**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Psychic/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868360900824948736/048.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#049

@client.command()
async def Venomoth(ctx):
    embed = discord.Embed(title="Pokemon #049", description=" **Venomoth**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Bug/Poison")
    embed.add_field(name="Weaknesses", value= "Fire/Flying/Psychic/Rock")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868361675533848626/049.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




#050

@client.command()
async def Diglett(ctx):
    embed = discord.Embed(title="Pokemon #050", description=" **Diglett**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ground")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868362800643309598/050.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#050 Alolan

@client.command()
async def AlolanDiglett(ctx):
    embed = discord.Embed(title="Pokemon #050 Alolan", description=" **Alolan Diglett**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ground/Steel")
    embed.add_field(name="Weaknesses", value= "Fire/Water/Fighting/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868362862932934688/050_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#051

@client.command()
async def Dugtrio(ctx):
    embed = discord.Embed(title="Pokemon #051", description=" **Dugtrio**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ground")
    embed.add_field(name="Weaknesses", value= "Water/Ground/Ice")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868365005932859452/051.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#051 Alolan

@client.command()
async def AlolanDugtrio(ctx):
    embed = discord.Embed(title="Pokemon #051 Alolan", description=" **Alolan Dugtrio**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Ground/Steel")
    embed.add_field(name="Weaknesses", value= "Fire/Water/Fighting/Ground")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868365047020261406/051_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#052


@client.command()
async def Meowth(ctx):
    embed = discord.Embed(title="Pokemon #052 ", description=" **Meowth**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal")
    embed.add_field(name="Weaknesses", value= "Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868366646933344326/052.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#052 Alolan


@client.command()
async def AlolanMeowth(ctx):
    embed = discord.Embed(title="Pokemon #052 Alolan ", description=" **ALolan Meowth**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Dark")
    embed.add_field(name="Weaknesses", value= "Fairy/Bug/Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868367052463829052/052_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#052 Galarian


@client.command()
async def GalarianMeowth(ctx):
    embed = discord.Embed(title="Pokemon #052 Galarian ", description=" **Galarian Meowth**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Steel")
    embed.add_field(name="Weaknesses", value= "Fire/Ground/Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868367494031769610/052_f3.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#052 Gigantamax


@client.command()
async def GigantamaxMeowth(ctx):
    embed = discord.Embed(title="Pokemon #052 Gigantamax" , description=" **GigantamaxMeowth**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal")
    embed.add_field(name="Weaknesses", value= "Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://cdn.discordapp.com/attachments/866591261640622131/868367971280629770/052_f4.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#053


@client.command()
async def Persian(ctx):
    embed = discord.Embed(title="Pokemon #053 ", description=" **Persian**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Normal")
    embed.add_field(name="Weaknesses", value= "Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/870559771747573770/053.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#053 Alolan


@client.command()
async def AlolanPersian(ctx):
    embed = discord.Embed(title="Pokemon #053 Alolan ", description=" **ALolan Persian**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Dark")
    embed.add_field(name="Weaknesses", value= "Fairy/Bug/Fighting")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/870560442764906526/053_f2.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#054


@client.command()
async def Psyduck(ctx):
    embed = discord.Embed(title="Pokemon #054 ", description=" **Psyduck**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/870563209357180968/054.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)



#055


@client.command()
async def Golduck(ctx):
    embed = discord.Embed(title="Pokemon #055 ", description=" **Golduck**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Water")
    embed.add_field(name="Weaknesses", value= "Grass/Electric")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/871293238760316938/055.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#056


@client.command()
async def Mankey(ctx):
    embed = discord.Embed(title="Pokemon #056 ", description=" **Mankey**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fighting")
    embed.add_field(name="Weaknesses", value= "Psychic/Flying/Fairy")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/871294481792651304/056.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


#057


@client.command()
async def Primeape(ctx):
    embed = discord.Embed(title="Pokemon #057 ", description=" **Primeape**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fighting")
    embed.add_field(name="Weaknesses", value= "Psychic/Flying/Fairy")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/871294524897513482/057.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def Growlithe(ctx):    
    embed = discord.Embed(title="Pokemon #057 ", description=" **Primeape**", color=discord.Color.random())
    embed.add_field(name="Types", value= "Fighting")
    embed.add_field(name="Weaknesses", value= "Psychic/Flying/Fairy")
    embed.add_field(name="Region", value="Kanto" )
    embed.set_image(url='https://media.discordapp.net/attachments/866591261640622131/871294524897513482/057.png')
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


keep_alive()

client.run('Your Bot Token')



