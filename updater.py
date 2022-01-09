from requests import get 
from socket import gethostbyname
import datetime 
noipURL = "http://dynupdate.no-ip.com/nic/update"
ipCheckURL = "https://api.ipify.org/"


def updateDNS(hostname, auth):
    myip = myIP()
    if IPchanged(hostname, myip):
        params = {'hostname': hostname, 'myip': myip}
        print(f'[{getTime()}] Changing IP in DDNS Sever... ')
        response = get(noipURL, auth=auth, params=params)
        print(f'[{getTime()}] DDNS server response: {response.text}')

def myIP():
    return get(ipCheckURL).text

def IPchanged(hostname,myip):
    try:
        IPresolved = gethostbyname(hostname)
    except Exception as e:
        print(f'[{getTime()}] check IP ERROR:', e)
    diff=(IPresolved!=myip)
    if diff:
        print(f'[{getTime()}] Found the difference. IP assigned to {hostname} in DNS: {IPresolved}. My acctualy IP: {myip}')
    return diff

def getTime():
    return datetime.datetime.now()

