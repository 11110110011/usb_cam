# Raspberry pi setup

## Connecting to an access point
```shell
sudo raspi-config
```
Go to **Network->WiFi**, select the needed access point,
enter the password and connect to it    
To find out your IP address, enter
```shell
hostname -I
```

## Installing dependencies
Updating:
```shell
sudo apt update
sudo apt upgrade
```
Installing the python package manager and supporting packages
```shell
sudo apt install python3-dev python3-pip python3-numpy
```

Installing openCV
```shell
sudo apt install python3-opencv
```

## App launch
Downloading the project repository
```shell
git clone https://github.com/11110110011/webcam.git/
```
and run the app
```shell
cd webcam
python3 app.py -i (ip address raspberry pi) -p (port) -s (serial port)
```
Open a browser and type in
```shell
(ip address raspberry pi):(port)
```
For example:
```shell
192.168.1.25:5000
```     


