ALBPC2078G
BCAPG7902A

### Blockchain Deployment
> Login to 10.136.220.29
> fabric-binaries -> test3 -> <Repo>

### Setting Proxy
export http_proxy=http://Corpproxy1.tatasteel.com:80
export https_proxy=https://Corpproxy1.tatasteel.com:443

export http_proxy=
export https_proxy=


ps -ef | grep restserver
ps -aux | grep restserver
netstat -ntpl

### Rest Server Deployment
rm restserver-1/restserver1
cp restServer-binaryQA/restserver ./restserver-1/restserver1

rm restserver-2/restserver2
cp restServer-binaryQA/restserver ./restserver-2/restserver2

rm restserver-3/restserver3
cp restServer-binaryQA/restserver ./restserver-3/restserver3


### (OPTIONAL) Rest Server Deployment
rm restserver-1/restserver1
cp TataTubesRESTServer/restserver ./restserver-1/restserver1

rm restserver-2/restserver2
cp TataTubesRESTServer/restserver ./restserver-2/restserver2

rm restserver-3/restserver3
cp TataTubesRESTServer/restserver ./restserver-3/restserver3



# Depoying the front end code

cd
rm -rf restserver-1/build/tubenxt
cp restServer-binaryQA/tubenxt.zip ./restserver-1/build
cd restserver-1/build
unzip tubenxt.zip
rm tubenxt.zip
cd 

rm -rf restserver-2/build/tubenxt
cp restServer-binaryQA/tubenxt.zip ./restserver-2/build
cd restserver-2/build
unzip tubenxt.zip
rm tubenxt.zip
cd 

rm -rf restserver-3/build/tubenxt
cp restServer-binaryQA/tubenxt.zip ./restserver-3/build
cd restserver-3/build
unzip tubenxt.zip
rm tubenxt.zip
cd 


# TC Verification Portal
rm -rf restserver-1/build/tcverification
cp restServer-binaryQA/tcverification.zip ./restserver-1/build
cd restserver-1/build
unzip tcverification.zip
rm tcverification.zip
cd ../..

rm -rf restserver-2/build/tcverification
cp restServer-binaryQA/tcverification.zip ./restserver-2/build
cd restserver-2/build
unzip tcverification.zip
rm tcverification.zip
cd ../..

rm -rf restserver-3/build/tcverification
cp restServer-binaryQA/tcverification.zip ./restserver-3/build
cd restserver-3/build
unzip tcverification.zip
rm tcverification.zip
cd ../..



# Disabling Proxy
export http_proxy=
export https_proxy=


# Killing the running process
ps -aux | grep restserver
kill <PID>

# Starting the server

nohub 



