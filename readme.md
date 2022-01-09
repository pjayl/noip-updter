
Container that updates the assigment ip to a domain name in Noip.com based on the value returned by https://api.ipify.org/.

Build script 
``` bash 
./build.sh
```

Run container 
``` bash
docker run -d \
  --name=noip-updater \
  -e NOIP_USERNAME=<username> \
  -e NOIP_PASSWORD=<pass> \
  -e NOIP_HOSTNAME=<Domain Name> \
  -e NOIP_INTERVAL=60 \
  noip-updater:latest

```


