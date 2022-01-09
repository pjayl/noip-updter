from  os import environ
from updater import updateDNS
from time import sleep 

USERNAME=environ.get('NOIP_USERNAME')
PASSWORD=environ.get('NOIP_PASSWORD')
HOSTNAME=environ.get('NOIP_HOSTNAME')
interval=int(environ.get('NOIP_INTERVAL',600))

while True:
    updateDNS(hostname=HOSTNAME,  auth=(USERNAME,PASSWORD))
    sleep(interval)




