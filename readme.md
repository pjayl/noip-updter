
Build script 
``` bash 
./build.sh
```


docker run -d \
  --name=noip-updater \
  -e NOIP_USERNAME=<username> \
  -e NOIP_PASSWORD=<pass> \
  -e NOIP_HOSTNAME=b<Domain Name> \
  -e NOIP_INTERVAL=60 \
  noip-updater:latest


