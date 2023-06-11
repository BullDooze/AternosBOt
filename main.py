# Import
from python_aternos import Client

# Create object
aternos = Client()

# Log in
# with username and password
aternos.login('Zeppeline1', 'jashashar')

# Get servers list
servs = aternos.list_servers()

# Get the first server
myserv = servs[0]

# Start
myserv.start()
# Stop
myserv.stop()



