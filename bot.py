import discord
from python_aternos import Client
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        # Import


# Create object
    aternos = Client()

# Log in
# with username and password
    aternos.login('', '')

# Get servers list
    servs = aternos.list_servers()

# Get the first server
    myserv = servs[0]

# Start
    myserv.start()
    myserv.stop()




    await message.channel.send('Started.')

client.run('')
